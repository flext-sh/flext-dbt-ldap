"""Behavior contract for FlextDbtLdap sync methods — public API only."""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

import pytest
from flext_tests import tm

from flext_dbt_ldap import FlextDbtLdap, FlextDbtLdapSettings
from tests import c, m, p, r, t, u

type _SyncState = t.MutableMappingKV[str, str] | None
type _SyncFactory = Callable[[Path, _SyncState], t.Pair[FlextDbtLdap, Path]]


def _read_sync_state(state_file: Path) -> t.JsonMapping:
    read_result = u.Cli.json_read(state_file)
    if read_result.failure:
        pytest.fail(read_result.error or "Failed to read sync state")
    payload: t.JsonMapping = t.json_mapping_adapter().validate_python(
        read_result.value or {}
    )
    return payload


def _read_bookmark(state_file: Path, sync_key: str) -> str:
    value = _read_sync_state(state_file)[sync_key]
    return str(value)


def _install_successful_pipeline_stub(
    monkeypatch: pytest.MonkeyPatch,
) -> t.MutableMappingKV[str, str | t.StrSequence | None]:
    call_kwargs: t.MutableMappingKV[str, str | t.StrSequence | None] = {}

    def fake_run_full_pipeline(
        _self: FlextDbtLdap,
        *,
        search_base: str | None = None,
        search_filter: str,
        attributes: t.StrSequence | None = None,
        model_names: t.StrSequence | None = None,
    ) -> p.Result[m.DbtLdap.DbtLdapPipelineResult]:
        call_kwargs.update({
            "search_base": search_base,
            "search_filter": search_filter,
            "attributes": attributes,
            "model_names": model_names,
        })
        return r[m.DbtLdap.DbtLdapPipelineResult](
            value=m.DbtLdap.DbtLdapPipelineResult(extracted_entries=1),
            success=True,
        )

    monkeypatch.setattr(FlextDbtLdap, "run_full_pipeline", fake_run_full_pipeline)
    return call_kwargs


class TestsFlextDbtLdapServicesSync:
    """Behavior contract for FlextDbtLdap sync_users/sync_groups/run_dbt_models."""

    def test_sync_users_applies_incremental_bookmark_and_persists_new_state(
        self,
        tmp_path: Path,
        dbt_ldap_service_factory: _SyncFactory,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        service, state_file = dbt_ldap_service_factory(
            tmp_path,
            {"users": "20250101000000Z"},
        )
        call_kwargs = _install_successful_pipeline_stub(monkeypatch)
        result = service.sync_users_to_warehouse(incremental=True)
        tm.ok(result)
        tm.that(
            call_kwargs["search_filter"],
            eq="(&(objectClass=person)(modifyTimestamp>=20250101000000Z))",
        )
        persisted = _read_bookmark(state_file, "users")
        tm.that(persisted.endswith("Z"), eq=True)
        tm.that(persisted, gt="20250101000000Z")

    def test_sync_groups_applies_incremental_bookmark_and_persists_new_state(
        self,
        tmp_path: Path,
        dbt_ldap_service_factory: _SyncFactory,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        service, state_file = dbt_ldap_service_factory(
            tmp_path,
            {"groups": "20250101000000Z"},
        )
        call_kwargs = _install_successful_pipeline_stub(monkeypatch)
        result = service.sync_groups_to_warehouse(incremental=True)
        tm.ok(result)
        tm.that(
            call_kwargs["search_filter"],
            eq=f"(&{c.DbtLdap.FILTER_GROUP}(modifyTimestamp>=20250101000000Z))",
        )
        persisted = _read_bookmark(state_file, "groups")
        tm.that(persisted.endswith("Z"), eq=True)
        tm.that(persisted, gt="20250101000000Z")

    def test_sync_users_fails_when_state_persistence_raises(
        self,
        tmp_path: Path,
        dbt_ldap_service_factory: _SyncFactory,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        service, state_file = dbt_ldap_service_factory(tmp_path, None)
        _ = _install_successful_pipeline_stub(monkeypatch)

        def fake_json_write(
            path: Path,
            payload: t.JsonPayload,
            options: m.Cli.JsonWriteOptions | None = None,
        ) -> p.Result[bool]:
            _ = (path, payload, options)
            return r[bool].fail("json_write: disk full")

        monkeypatch.setattr(u.Cli, "json_write", fake_json_write)

        result = service.sync_users_to_warehouse(incremental=True)
        tm.fail(result)
        tm.that(result.error, eq="json_write: disk full")
        tm.that(state_file.exists(), eq=False)

    def test_service_init_rejects_non_string_sync_state_values(
        self,
        tmp_path: Path,
        dbt_ldap_service_factory: _SyncFactory,
    ) -> None:
        _ = dbt_ldap_service_factory
        state_file = tmp_path / ".flext_dbt_ldap_sync_state.json"
        state_file.write_text('{"users": 1}\n', encoding=c.Cli.ENCODING_DEFAULT)
        settings = FlextDbtLdapSettings.model_validate({
            "ldap_base_dn": "dc=example,dc=com",
            "dbt_project_dir": str(tmp_path),
        })

        with pytest.raises(TypeError, match="Sync state file values must be strings"):
            _ = FlextDbtLdap(settings=settings)

    def test_run_dbt_models_propagates_underlying_run_models_failure(
        self,
        tmp_path: Path,
        dbt_ldap_service_factory: _SyncFactory,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        service, _ = dbt_ldap_service_factory(tmp_path, None)

        def fake_run_models(
            _self: FlextDbtLdap,
            models: t.StrSequence | None = None,
        ) -> p.Result[str]:
            _ = models
            return r[str].fail("dbt failed")

        monkeypatch.setattr(FlextDbtLdap, "run_models", fake_run_models)

        result = service.run_dbt_models([c.DbtLdap.DIM_USERS])
        tm.fail(result)
        tm.that(result.error, eq="dbt failed")
