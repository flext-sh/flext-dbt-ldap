"""Behavior contract for FlextDbtLdap sync methods — public API only.

These tests drive the public facade end to end and control ONLY the genuine
external boundaries the facade depends on:

* the LDAP client (``FlextLdap``) injected via the public ``create_ldap_api``
  factory hook — the outgoing search request is the facade's contract with the
  directory server;
* the dbt runner (``run_models``, inherited from ``flext_meltano``) — the
  external command-execution boundary;
* the sync-state file on disk (via ``u.Cli.json_write``) — an IO boundary.

No method defined inside flext-dbt-ldap is patched: the incremental-filter,
bookmark and pipeline logic all execute for real and are observed through the
returned ``r[T]`` outcome and the persisted state file.
"""

from __future__ import annotations

from pathlib import Path
from unittest.mock import Mock

import pytest
from flext_tests import r, tm

from flext_dbt_ldap import FlextDbtLdap, FlextDbtLdapSettings
from tests import c, m, p, t, u


class TestsFlextDbtLdapServicesSync:
    """Behavior contract for FlextDbtLdap sync/run/report public methods."""

    # ------------------------------------------------------------------ #
    # External-boundary helpers
    # ------------------------------------------------------------------ #

    @staticmethod
    def _ldap_api_with_entries(entry_count: int) -> Mock:
        """Build an LDAP client double that returns ``entry_count`` entries."""
        entries: list[Mock] = []
        for index in range(entry_count):
            entry = Mock()
            entry.dn = f"uid=user{index},dc=example,dc=com"
            entry.attributes_dict = {"uid": [f"user{index}"]}
            entries.append(entry)
        search_value = Mock()
        search_value.entries = entries
        search_result = Mock()
        search_result.success = True
        search_result.value = search_value
        api = Mock()
        api.search.return_value = search_result
        return api

    def _install_boundaries(
        self,
        monkeypatch: pytest.MonkeyPatch,
        *,
        entry_count: int = 1,
    ) -> Mock:
        """Wire the LDAP + dbt external boundaries; return the LDAP double."""
        api = self._ldap_api_with_entries(entry_count)

        def fake_create_ldap_api(_settings: FlextDbtLdapSettings) -> Mock:
            return api

        def fake_run_models(
            _self: FlextDbtLdap,
            models: t.StrSequence | None = None,
        ) -> p.Result[t.StrSequence]:
            return r[t.StrSequence].ok(list(models) if models else [])

        monkeypatch.setattr(
            FlextDbtLdap,
            "create_ldap_api",
            staticmethod(fake_create_ldap_api),
        )
        monkeypatch.setattr(FlextDbtLdap, "run_models", fake_run_models)
        return api

    @staticmethod
    def _sent_filter(api: Mock) -> str:
        """Return the ``filter_str`` of the last search sent to the directory."""
        search_options = api.search.call_args.kwargs["search_options"]
        return str(search_options.filter_str)

    @staticmethod
    def _read_sync_state(state_file: Path) -> t.JsonMapping:
        read_result = u.Cli.json_read(state_file)
        if read_result.failure:
            pytest.fail(read_result.error or "Failed to read sync state")
        payload: t.JsonMapping = t.json_mapping_adapter().validate_python(
            read_result.value or {},
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
        monkeypatch: pytest.MonkeyPatch,
        sync_method: str,
        sync_key: str,
        expected_filter: str,
    ) -> None:
        api = self._install_boundaries(monkeypatch)
        service, state_file = dbt_ldap_service_factory(
            tmp_path,
            {sync_key: "20250101000000Z"},
        )

        result = getattr(service, sync_method)(incremental=True)

        tm.ok(result)
        tm.that(self._sent_filter(api), eq=expected_filter)
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
        monkeypatch: pytest.MonkeyPatch,
        sync_method: str,
        sync_key: str,
        base_filter: str,
    ) -> None:
        api = self._install_boundaries(monkeypatch)
        service, state_file = dbt_ldap_service_factory(tmp_path, None)

        result = getattr(service, sync_method)(incremental=True)

        tm.ok(result)
        # No prior bookmark → full scan with the bare object-class filter.
        tm.that(self._sent_filter(api), eq=base_filter)
        # A fresh bookmark is recorded so the next run can be incremental.
        recorded = str(self._read_sync_state(state_file)[sync_key])
        tm.that(recorded.endswith("Z"), eq=True)

    def test_successful_sync_reports_extracted_entry_count(
        self,
        tmp_path: Path,
        dbt_ldap_service_factory: t.DbtLdap.Tests.ServiceFactory,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        self._install_boundaries(monkeypatch, entry_count=3)
        service, _ = dbt_ldap_service_factory(tmp_path, None)

        result = service.sync_users_to_warehouse()

        tm.ok(result)
        tm.that(result.value.extracted_entries, eq=3)

    def test_full_warehouse_sync_succeeds_across_all_components(
        self,
        tmp_path: Path,
        dbt_ldap_service_factory: t.DbtLdap.Tests.ServiceFactory,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        self._install_boundaries(monkeypatch, entry_count=2)
        service, _ = dbt_ldap_service_factory(tmp_path, None)

        result = service.run_full_data_warehouse_sync()

        tm.ok(result)
        tm.that(result.value.overall_success, eq=True)
        tm.that(result.value.successful_components, eq=result.value.total_components)

    # ------------------------------------------------------------------ #
    # Error propagation from external boundaries
    # ------------------------------------------------------------------ #

    def test_sync_users_fails_when_state_persistence_raises(
        self,
        tmp_path: Path,
        dbt_ldap_service_factory: t.DbtLdap.Tests.ServiceFactory,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        self._install_boundaries(monkeypatch)

        def fake_json_write(
            path: Path,
            payload: t.JsonPayload,
            options: m.Cli.JsonWriteOptions | None = None,
        ) -> p.Result[bool]:
            _ = (path, payload, options)
            return r[bool].fail("json_write: disk full")

        monkeypatch.setattr(u.Cli, "json_write", fake_json_write)
        service, state_file = dbt_ldap_service_factory(tmp_path, None)

        result = service.sync_users_to_warehouse(incremental=True)

        tm.fail(result)
        tm.that(result.error, eq="json_write: disk full")
        tm.that(state_file.exists(), eq=False)

    def test_sync_users_fails_when_ldap_extraction_fails(
        self,
        tmp_path: Path,
        dbt_ldap_service_factory: t.DbtLdap.Tests.ServiceFactory,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        api = self._install_boundaries(monkeypatch)
        failed_search = Mock()
        failed_search.success = False
        failed_search.value = None
        failed_search.error = "directory unreachable"
        api.search.return_value = failed_search
        service, state_file = dbt_ldap_service_factory(tmp_path, None)

        result = service.sync_users_to_warehouse()

        tm.fail(result)
        # A failed extraction must not persist any bookmark state.
        tm.that(state_file.exists(), eq=False)

    def test_run_dbt_models_propagates_underlying_run_models_failure(
        self,
        tmp_path: Path,
        dbt_ldap_service_factory: t.DbtLdap.Tests.ServiceFactory,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        self._install_boundaries(monkeypatch)

        def fake_run_models(
            _self: FlextDbtLdap,
            models: t.StrSequence | None = None,
        ) -> p.Result[t.StrSequence]:
            _ = models
            return r[t.StrSequence].fail("dbt failed")

        monkeypatch.setattr(FlextDbtLdap, "run_models", fake_run_models)
        service, _ = dbt_ldap_service_factory(tmp_path, None)

        result = service.run_dbt_models([c.DbtLdap.DIM_USERS])

        tm.fail(result)
        tm.that(result.error, eq="dbt failed")

    def test_run_dbt_models_reports_selected_models_on_success(
        self,
        tmp_path: Path,
        dbt_ldap_service_factory: t.DbtLdap.Tests.ServiceFactory,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        self._install_boundaries(monkeypatch)
        service, _ = dbt_ldap_service_factory(tmp_path, None)

        result = service.run_dbt_models([c.DbtLdap.DIM_USERS])

        tm.ok(result)
        tm.that(list(result.value.models_run), eq=[c.DbtLdap.DIM_USERS])

    # ------------------------------------------------------------------ #
    # Construction contract
    # ------------------------------------------------------------------ #

    def test_service_init_rejects_non_string_sync_state_values(
        self,
        tmp_path: Path,
        dbt_ldap_service_factory: t.DbtLdap.Tests.ServiceFactory,
    ) -> None:
        _ = dbt_ldap_service_factory
        state_file = tmp_path / ".flext_dbt_ldap_sync_state.json"
        state_file.write_text('{"users": 1}\n', encoding=c.Cli.ENCODING_DEFAULT)
        # NOTE (multi-agent): mro-rn88 — project fields nest under DbtLdap namespace.
        settings = FlextDbtLdapSettings.model_validate({
            "DbtLdap": {
                "ldap_base_dn": "dc=example,dc=com",
                "dbt_project_dir": str(tmp_path),
            },
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
