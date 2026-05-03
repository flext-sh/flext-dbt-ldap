"""Test configuration and fixtures for flext-dbt-ldap.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import os
import pathlib
import tempfile
from collections.abc import (
    Callable,
    Generator,
)
from unittest.mock import Mock

import pytest

from flext_dbt_ldap import FlextDbtLdap, FlextDbtLdapSettings
from tests import t, u

type _SyncState = t.MutableMappingKV[str, str] | None
type _ServiceFactory = Callable[
    [pathlib.Path, _SyncState],
    t.Pair[FlextDbtLdap, pathlib.Path],
]


def _fake_create_ldap_api(_settings: FlextDbtLdapSettings) -> t.JsonValue:
    return Mock()


@pytest.fixture
def dbt_ldap_service_factory(
    monkeypatch: pytest.MonkeyPatch,
) -> _ServiceFactory:
    """Build a real public facade instance with isolated sync-state storage."""
    monkeypatch.setattr(
        FlextDbtLdap,
        "create_ldap_api",
        staticmethod(_fake_create_ldap_api),
    )

    def factory(
        dbt_project_dir: pathlib.Path,
        initial_state: _SyncState = None,
    ) -> t.Pair[FlextDbtLdap, pathlib.Path]:
        settings = FlextDbtLdapSettings.model_validate({
            "ldap_base_dn": "dc=example,dc=com",
            "dbt_project_dir": str(dbt_project_dir),
        })
        state_file = dbt_project_dir / ".flext_dbt_ldap_sync_state.json"
        if initial_state is not None:
            write_result = u.Cli.json_write(state_file, initial_state)
            assert write_result.success, write_result.error
        return FlextDbtLdap(settings=settings), state_file

    return factory


@pytest.fixture(autouse=True)
def set_test_environment() -> Generator[None]:
    """Set test environment variables."""
    os.environ["FLEXT_ENV"] = "test"
    os.environ["FLEXT_LOG_LEVEL"] = "DEBUG"
    temp_dir = tempfile.mkdtemp(prefix="dbt_profiles_")
    os.environ["DBT_PROFILES_DIR"] = temp_dir
    os.environ["LDAP_TEST_MODE"] = "true"
    yield
    _ = os.environ.pop("FLEXT_ENV", None)
    _ = os.environ.pop("FLEXT_LOG_LEVEL", None)
    _ = os.environ.pop("DBT_PROFILES_DIR", None)
    _ = os.environ.pop("LDAP_TEST_MODE", None)
