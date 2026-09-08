"""Behavior contract for FlextDbtLdap sync methods — public API only.

These tests drive the public facade end to end against test-owned real
boundaries:

* the LDAP directory is the in-memory ``FlextLdap`` client produced by the
  facade's own ``create_ldap_api`` hook — every outgoing search request is
  recorded verbatim and answered with real ``m.Ldif.Entry`` models;
* the dbt runner executes in memory inside the facade subclass, recording
  every requested model list and answering with real command-execution
  models;
* the sync-state file lives on the real filesystem under ``tmp_path``.

No production method is replaced at runtime: the incremental-filter, bookmark
and pipeline logic all execute for real and are observed through the returned
``r[T]`` outcome, the recorded directory requests and the persisted state file.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from flext_dbt_ldap import FlextDbtLdap, FlextDbtLdapSettings
from flext_tests import tm
from tests import c, m, t, u

if TYPE_CHECKING:
    from pathlib import Path


class TestsFlextDbtLdapServicesSync:
    """Behavior contract for FlextDbtLdap sync/run/report public methods."""

    # ------------------------------------------------------------------ #
    # External-boundary helpers
    # ------------------------------------------------------------------ #

    @staticmethod
    def _directory_entries(entry_count: int) -> list[m.Ldif.Entry]:
        """Build real directory entries served by the in-memory LDAP client."""
        base_dn = c.DbtLdap.Tests.DIRECTORY_BASE_DN
        return [
            m.Ldif.Entry(
                dn=m.Ldif.DN(value=f"uid=user{index},{base_dn}"),
                attributes=m.Ldif.Attributes(
                    attributes={"uid": [f"user{index}"]}, attribute_metadata={}
                ),
            )
            for index in range(entry_count)
        ]

    @staticmethod
    def _sent_filter(directory: u.DbtLdap.Tests.InMemoryLdapDirectory) -> str:
        """Return the ``filter_str`` of the last search sent to the directory."""
        return directory.last_search_request().filter_str

    @staticmethod
    def _read_sync_state(state_file: Path) -> t.JsonMapping:
        read_result = u.Cli.json_read(state_file)
        if read_result.failure:
            pytest.fail(read_result.error or "Failed to read sync state")
        payload: t.JsonMapping = t.json_mapping_adapter().validate_python(
            read_result.value or {}
        )
        return payload

    # ------------------------------------------------------------------ #
    # Incremental bookmark → outgoing filter + persisted state
    # ------------------------------------------------------------------ #

    @pytest.mark.parametrize(
        ("sync_method", "sync_key", "expected_filter"),
        [
            (
                "sync_users_to_warehouse",
                c.DbtLdap.USERS,
                f"(&{c.DbtLdap.FILTER_USER}(modifyTimestamp>=20250101000000Z))",
            ),
            (
                "sync_groups_to_warehouse",
                c.DbtLdap.GROUPS,
                f"(&{c.DbtLdap.FILTER_GROUP}(modifyTimestamp>=20250101000000Z))",
            ),
        ],
    )
    def test_incremental_sync_applies_prior_bookmark_to_filter_and_advances_state(
        self,
        tmp_path: Path,
        dbt_ldap_service_factory: t.DbtLdap.Tests.ServiceFactory,
        sync_method: str,
        sync_key: str,
        expected_filter: str,
    ) -> None:
        service, state_file = dbt_ldap_service_factory(
            tmp_path, {sync_key: "20250101000000Z"}
        )
        service.directory().serve(self._directory_entries(1))

        result = getattr(service, sync_method)(incremental=True)

        tm.ok(result)
        tm.that(self._sent_filter(service.directory()), eq=expected_filter)
        persisted = str(self._read_sync_state(state_file)[sync_key])
        tm.that(persisted.endswith("Z"), eq=True)
        tm.that(persisted, gt="20250101000000Z")

    @pytest.mark.parametrize(
        ("sync_method", "sync_key", "base_filter"),
        [
            ("sync_users_to_warehouse", c.DbtLdap.USERS, c.DbtLdap.FILTER_USER),
            ("sync_groups_to_warehouse", c.DbtLdap.GROUPS, c.DbtLdap.FILTER_GROUP),
        ],
    )
    def test_first_incremental_run_scans_with_base_filter_then_records_bookmark(
        self,
        tmp_path: Path,
        dbt_ldap_service_factory: t.DbtLdap.Tests.ServiceFactory,
        sync_method: str,
        sync_key: str,
        base_filter: str,
    ) -> None:
        service, state_file = dbt_ldap_service_factory(tmp_path, None)
        service.directory().serve(self._directory_entries(1))

        result = getattr(service, sync_method)(incremental=True)

        tm.ok(result)
        # No prior bookmark → full scan with the bare object-class filter.
        tm.that(self._sent_filter(service.directory()), eq=base_filter)
        # A fresh bookmark is recorded so the next run can be incremental.
        recorded = str(self._read_sync_state(state_file)[sync_key])
        tm.that(recorded.endswith("Z"), eq=True)

    def test_successful_sync_reports_extracted_entry_count(
        self, tmp_path: Path, dbt_ldap_service_factory: t.DbtLdap.Tests.ServiceFactory
    ) -> None:
        service, _ = dbt_ldap_service_factory(tmp_path, None)
        service.directory().serve(self._directory_entries(3))

        result = service.sync_users_to_warehouse()

        tm.ok(result)
        tm.that(result.value.extracted_entries, eq=3)

    def test_full_warehouse_sync_succeeds_across_all_components(
        self, tmp_path: Path, dbt_ldap_service_factory: t.DbtLdap.Tests.ServiceFactory
    ) -> None:
        service, _ = dbt_ldap_service_factory(tmp_path, None)
        service.directory().serve(self._directory_entries(2))

        result = service.run_full_data_warehouse_sync()

        tm.ok(result)
        tm.that(result.value.overall_success, eq=True)
        tm.that(result.value.successful_components, eq=result.value.total_components)

    # ------------------------------------------------------------------ #
    # Error propagation from external boundaries
    # ------------------------------------------------------------------ #

    def test_sync_users_fails_when_state_persistence_fails(
        self, tmp_path: Path, dbt_ldap_service_factory: t.DbtLdap.Tests.ServiceFactory
    ) -> None:
        service, state_file = dbt_ldap_service_factory(tmp_path, None)
        service.directory().serve(self._directory_entries(1))
        # A directory occupying the state-file path makes the real filesystem
        # write fail, so the genuine persistence path raises.
        state_file.mkdir()

        result = service.sync_users_to_warehouse(incremental=True)

        tm.fail(result)
        tm.that(state_file.is_file(), eq=False)

    def test_sync_users_fails_when_ldap_extraction_fails(
        self, tmp_path: Path, dbt_ldap_service_factory: t.DbtLdap.Tests.ServiceFactory
    ) -> None:
        service, state_file = dbt_ldap_service_factory(tmp_path, None)
        service.directory().mark_unreachable()

        result = service.sync_users_to_warehouse()

        tm.fail(result)
        # A failed extraction must not persist any bookmark state.
        tm.that(state_file.exists(), eq=False)

    def test_run_dbt_models_propagates_underlying_run_models_failure(
        self, tmp_path: Path, dbt_ldap_service_factory: t.DbtLdap.Tests.ServiceFactory
    ) -> None:
        service, _ = dbt_ldap_service_factory(tmp_path, None)
        service.mark_dbt_failure("dbt failed")

        result = service.run_dbt_models([c.DbtLdap.DIM_USERS])

        tm.fail(result)
        tm.that(result.error, eq="dbt failed")

    def test_run_dbt_models_reports_selected_models_on_success(
        self, tmp_path: Path, dbt_ldap_service_factory: t.DbtLdap.Tests.ServiceFactory
    ) -> None:
        service, _ = dbt_ldap_service_factory(tmp_path, None)

        result = service.run_dbt_models([c.DbtLdap.DIM_USERS])

        tm.ok(result)
        tm.that(list(result.value.models_run), eq=[c.DbtLdap.DIM_USERS])
        # The runner received exactly the selected model list.
        tm.that(service.dbt_requests(), eq=((c.DbtLdap.DIM_USERS,),))

    # ------------------------------------------------------------------ #
    # Construction contract
    # ------------------------------------------------------------------ #

    def test_service_init_rejects_non_string_sync_state_values(
        self, tmp_path: Path, dbt_ldap_service_factory: t.DbtLdap.Tests.ServiceFactory
    ) -> None:
        _ = dbt_ldap_service_factory
        state_file = tmp_path / ".flext_dbt_ldap_sync_state.json"
        state_file.write_text('{"users": 1}\n', encoding=c.Cli.ENCODING_DEFAULT)
        # NOTE (multi-agent): mro-rn88 — project fields nest under DbtLdap namespace.
        settings = FlextDbtLdapSettings.model_validate({
            "DbtLdap": {
                "ldap_base_dn": c.DbtLdap.Tests.DIRECTORY_BASE_DN,
                "dbt_project_dir": str(tmp_path),
            }
        })

        with pytest.raises(TypeError, match="Sync state file values must be strings"):
            _ = FlextDbtLdap(settings=settings)

    # ------------------------------------------------------------------ #
    # Analytics report (pure, no external boundary)
    # ------------------------------------------------------------------ #

    def test_generate_analytics_report_returns_requested_report_type(self) -> None:
        result = FlextDbtLdap.generate_analytics_report("membership")

        tm.ok(result)
        tm.that(result.value.report_type, eq="membership")


__all__: list[str] = ["TestsFlextDbtLdapServicesSync"]
