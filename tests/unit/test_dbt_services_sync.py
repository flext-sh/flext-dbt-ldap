"""Tests for DbtLdapService sync methods.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path
from unittest.mock import Mock

from flext_core import r
from pydantic import TypeAdapter

from flext_dbt_ldap import m
from flext_dbt_ldap.dbt_services import FlextDbtLdapService
from flext_dbt_ldap.settings import FlextDbtLdapSettings

_BOOKMARKS_ADAPTER: TypeAdapter[Mapping[str, str]] = TypeAdapter(Mapping[str, str])


def test_sync_users_uses_incremental_bookmark_and_persists_state(
    tmp_path: Path,
) -> None:
    state_file = tmp_path / "sync-state.json"
    state_file.write_bytes(_BOOKMARKS_ADAPTER.dump_json({"users": "20250101000000Z"}))
    service = object.__new__(FlextDbtLdapService)
    service.config = FlextDbtLdapSettings.model_validate({
        "ldap_base_dn": "dc=example,dc=com",
    })
    service.client = Mock()
    service.client.run_full_pipeline.return_value = r[
        m.DbtLdap.DbtLdapPipelineResult
    ].ok(
        m.DbtLdap.DbtLdapPipelineResult(extracted_entries=1),
    )
    service._sync_state_file = state_file
    service._sync_bookmarks = service._load_sync_state()
    service._bookmark_now = lambda: "20260101000000Z"
    result = service.sync_users_to_warehouse(incremental=True)
    assert result.is_success
    call_kwargs = service.client.run_full_pipeline.call_args.kwargs
    assert (
        call_kwargs["search_filter"]
        == "(&(objectClass=person)(modifyTimestamp>=20250101000000Z))"
    )
    persisted_state = _BOOKMARKS_ADAPTER.validate_json(state_file.read_bytes())
    assert persisted_state["users"] == "20260101000000Z"
