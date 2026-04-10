"""Tests for DbtLdapService sync methods.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

import pytest

from flext_dbt_ldap import FlextDbtLdap, FlextDbtLdapSettings
from tests import c, m, r, t, u

type _SyncState = t.MutableMappingKV[str, str] | None
type _SyncFactory = Callable[[Path, _SyncState], t.Pair[FlextDbtLdap, Path]]


def _read_sync_state(state_file: Path) -> t.Cli.JsonMapping:
    read_result = u.Cli.json_read(state_file)
    if read_result.is_failure:
        pytest.fail(read_result.error or "Failed to read sync state")
    return read_result.unwrap()


def _read_bookmark(state_file: Path, sync_key: str) -> str:
    value = _read_sync_state(state_file)[sync_key]
    if not isinstance(value, str):
        msg = f"Expected bookmark value for {sync_key} to be a string"
        pytest.fail(msg)
    return value


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
    ) -> r[m.DbtLdap.DbtLdapPipelineResult]:
        call_kwargs.update({
            "search_base": search_base,
            "search_filter": search_filter,
            "attributes": attributes,
            "model_names": model_names,
        })
        return r[m.DbtLdap.DbtLdapPipelineResult](
            value=m.DbtLdap.DbtLdapPipelineResult(extracted_entries=1),
            is_success=True,
        )

    monkeypatch.setattr(FlextDbtLdap, "run_full_pipeline", fake_run_full_pipeline)
    return call_kwargs


def test_sync_users_uses_incremental_bookmark_and_persists_state(
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
    assert result.is_success
    assert (
        call_kwargs["search_filter"]
        == "(&(objectClass=person)(modifyTimestamp>=20250101000000Z))"
    )
    persisted = _read_bookmark(state_file, "users")
    assert persisted.endswith("Z")
    assert persisted > "20250101000000Z"


def test_sync_groups_uses_incremental_bookmark_and_persists_state(
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
    assert result.is_success
    assert (
        call_kwargs["search_filter"]
        == f"(&{c.DbtLdap.FILTER_GROUP}(modifyTimestamp>=20250101000000Z))"
    )
    persisted = _read_bookmark(state_file, "groups")
    assert persisted.endswith("Z")
    assert persisted > "20250101000000Z"


def test_sync_users_fails_when_sync_state_persistence_fails(
    tmp_path: Path,
    dbt_ldap_service_factory: _SyncFactory,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    service, state_file = dbt_ldap_service_factory(tmp_path, None)
    _ = _install_successful_pipeline_stub(monkeypatch)

    def fake_json_write(
        path: Path,
        payload: t.Cli.JsonPayload,
        *,
        sort_keys: bool = False,
        ensure_ascii: bool = False,
        indent: int = 2,
    ) -> r[bool]:
        _ = (path, payload, sort_keys, ensure_ascii, indent)
        return r[bool].fail("json_write: disk full")

    monkeypatch.setattr(u.Cli, "json_write", fake_json_write)

    result = service.sync_users_to_warehouse(incremental=True)
    assert result.is_failure
    assert result.error == "json_write: disk full"
    assert not state_file.exists()


def test_service_init_fails_fast_when_sync_state_is_invalid(
    tmp_path: Path,
    dbt_ldap_service_factory: _SyncFactory,
) -> None:
    _ = dbt_ldap_service_factory
    state_file = tmp_path / ".flext_dbt_ldap_sync_state.json"
    state_file.write_text('{"users": 1}\n', encoding=c.Cli.Encoding.DEFAULT)
    settings = FlextDbtLdapSettings.model_validate({
        "ldap_base_dn": "dc=example,dc=com",
        "dbt_project_dir": str(tmp_path),
    })

    with pytest.raises(TypeError, match="Sync state file values must be strings"):
        _ = FlextDbtLdap(config=settings)


def test_run_dbt_models_propagates_run_models_failure(
    tmp_path: Path,
    dbt_ldap_service_factory: _SyncFactory,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    service, _ = dbt_ldap_service_factory(tmp_path, None)

    def fake_run_models(
        _self: FlextDbtLdap,
        models: t.StrSequence | None = None,
    ) -> r[str]:
        _ = models
        return r[str].fail("dbt failed")

    monkeypatch.setattr(FlextDbtLdap, "run_models", fake_run_models)

    result = service.run_dbt_models([c.DbtLdap.DIM_USERS])
    assert result.is_failure
    assert result.error == "dbt failed"
