"""Tests for DbtLdapService sync methods.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from pathlib import Path
from unittest.mock import Mock

import pytest
from flext_cli import t as cli_t, u as cli_u

from flext_core import r
from flext_dbt_ldap import (
    FlextDbtLdapSettings,
    FlextDbtLdapUtilitiesSync as FlextDbtLdapService,
    m,
)


def test_sync_users_uses_incremental_bookmark_and_persists_state(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    state_file = tmp_path / "sync-state.json"
    cli_u.Cli.json_write(state_file, {"users": "20250101000000Z"})
    service = object.__new__(FlextDbtLdapService)
    service._dbt_ldap_config = FlextDbtLdapSettings.model_validate({
        "ldap_base_dn": "dc=example,dc=com",
    })
    mock_pipeline = Mock(
        return_value=r[m.DbtLdap.DbtLdapPipelineResult].ok(
            m.DbtLdap.DbtLdapPipelineResult(extracted_entries=1),
        ),
    )
    object.__setattr__(service, "run_full_pipeline", mock_pipeline)
    service._sync_state_file = state_file
    service._sync_bookmarks = service._load_sync_state()
    monkeypatch.setattr(service, "_bookmark_now", lambda: "20260101000000Z")
    result = service.sync_users_to_warehouse(incremental=True)
    assert result.is_success
    call_kwargs = mock_pipeline.call_args.kwargs
    assert (
        call_kwargs["search_filter"]
        == "(&(objectClass=person)(modifyTimestamp>=20250101000000Z))"
    )
    persisted: cli_t.Cli.JsonMapping = cli_u.Cli.json_read(state_file).unwrap_or({})
    assert persisted["users"] == "20260101000000Z"
