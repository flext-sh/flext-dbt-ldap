"""Tests for DbtLdapService sync methods.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

import pytest

from flext_dbt_ldap import FlextDbtLdap
from tests import c, m, r, t, u


def _fixed_bookmark(_service: FlextDbtLdap) -> str:
    return "20260101000000Z"


def _install_successful_pipeline_stub(
    monkeypatch: pytest.MonkeyPatch,
) -> dict[str, str | t.StrSequence | None]:
    call_kwargs: dict[str, str | t.StrSequence | None] = {}

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
        return r[m.DbtLdap.DbtLdapPipelineResult].ok(
            m.DbtLdap.DbtLdapPipelineResult(extracted_entries=1),
        )

    monkeypatch.setattr(FlextDbtLdap, "run_full_pipeline", fake_run_full_pipeline)
    return call_kwargs


def test_sync_users_uses_incremental_bookmark_and_persists_state(
    tmp_path: Path,
    dbt_ldap_service_factory: Callable[
        [Path, dict[str, str] | None],
        tuple[FlextDbtLdap, Path],
    ],
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    service, state_file = dbt_ldap_service_factory(
        tmp_path,
        {"users": "20250101000000Z"},
    )
    call_kwargs = _install_successful_pipeline_stub(monkeypatch)
    monkeypatch.setattr(FlextDbtLdap, "_bookmark_now", _fixed_bookmark)
    result = service.sync_users_to_warehouse(incremental=True)
    assert result.is_success
    assert (
        call_kwargs["search_filter"]
        == "(&(objectClass=person)(modifyTimestamp>=20250101000000Z))"
    )
    persisted: t.Cli.JsonMapping = u.Cli.json_read(state_file).unwrap_or({})
    assert persisted["users"] == "20260101000000Z"


def test_sync_groups_uses_incremental_bookmark_and_persists_state(
    tmp_path: Path,
    dbt_ldap_service_factory: Callable[
        [Path, dict[str, str] | None],
        tuple[FlextDbtLdap, Path],
    ],
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    service, state_file = dbt_ldap_service_factory(
        tmp_path,
        {"groups": "20250101000000Z"},
    )
    call_kwargs = _install_successful_pipeline_stub(monkeypatch)
    monkeypatch.setattr(FlextDbtLdap, "_bookmark_now", _fixed_bookmark)
    result = service.sync_groups_to_warehouse(incremental=True)
    assert result.is_success
    assert (
        call_kwargs["search_filter"]
        == f"(&{c.DbtLdap.FILTER_GROUP}(modifyTimestamp>=20250101000000Z))"
    )
    persisted: t.Cli.JsonMapping = u.Cli.json_read(state_file).unwrap_or({})
    assert persisted["groups"] == "20260101000000Z"


def test_run_dbt_models_propagates_run_models_failure(
    tmp_path: Path,
    dbt_ldap_service_factory: Callable[
        [Path, dict[str, str] | None],
        tuple[FlextDbtLdap, Path],
    ],
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
