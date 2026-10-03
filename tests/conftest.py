"""Test configuration and fixtures for flext-dbt-ldap.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import contextlib
import pathlib

import pytest
from flext_tests import tf, tm

from flext_dbt_ldap import FlextDbtLdapSettings
from tests import c, t, u

_env_stack_key: pytest.StashKey[contextlib.ExitStack] = pytest.StashKey()


def pytest_runtest_setup(item: pytest.Item) -> None:
    """Set per-test environment variables and temporary directory."""
    stack = item.stash[_env_stack_key] = contextlib.ExitStack()
    temp_dir = stack.enter_context(tf().temporary_directory())
    stack.enter_context(
        u.Tests.env_vars_context({
            "FLEXT_ENV": "test",
            "FLEXT_LOG_LEVEL": "DEBUG",
            "DBT_PROFILES_DIR": temp_dir,
            "LDAP_TEST_MODE": "true",
        })
    )


def pytest_runtest_teardown(item: pytest.Item) -> None:
    """Clean up per-test environment."""
    stack = item.stash.get(_env_stack_key, None)
    if stack is not None:
        stack.close()
        del item.stash[_env_stack_key]


@pytest.fixture
def dbt_ldap_service_factory() -> t.DbtLdap.Tests.ServiceFactory:
    """Build a real public facade instance with isolated sync-state storage."""

    def factory(
        dbt_project_dir: pathlib.Path, initial_state: t.DbtLdap.Tests.SyncState = None
    ) -> t.Pair[u.DbtLdap.Tests.InMemoryDbtRunnerLdap, pathlib.Path]:
        # NOTE (multi-agent): mro-rn88 — project fields live under the nested DbtLdap
        # namespace; a flat dict is dropped by extra="ignore" (no isolation).
        settings = FlextDbtLdapSettings.model_validate({
            "DbtLdap": {
                "ldap_base_dn": c.DbtLdap.Tests.DIRECTORY_BASE_DN,
                "dbt_project_dir": str(dbt_project_dir),
            }
        })
        state_file = dbt_project_dir / ".flext_dbt_ldap_sync_state.json"
        if initial_state is not None:
            write_result = u.Cli.json_write(state_file, initial_state)
            tm.ok(write_result)
        return u.DbtLdap.Tests.InMemoryDbtRunnerLdap(settings=settings), state_file

    return factory
