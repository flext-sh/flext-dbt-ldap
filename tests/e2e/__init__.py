# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make codegen
#
"""End-to-end tests for flext-dbt-ldap.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core.typings import FlextTypes

    from tests.e2e.conftest import (
        POSTGRES_READY_MAX_RETRIES,
        count_rows,
        db_connection,
        dbt_profiles_dir,
        dbt_project_dir,
        flext_docker,
        get_column_names,
        logger,
        postgres_container,
        project_root,
        query_database,
        run_dbt_command,
        table_exists,
    )

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "POSTGRES_READY_MAX_RETRIES": ("tests.e2e.conftest", "POSTGRES_READY_MAX_RETRIES"),
    "count_rows": ("tests.e2e.conftest", "count_rows"),
    "db_connection": ("tests.e2e.conftest", "db_connection"),
    "dbt_profiles_dir": ("tests.e2e.conftest", "dbt_profiles_dir"),
    "dbt_project_dir": ("tests.e2e.conftest", "dbt_project_dir"),
    "flext_docker": ("tests.e2e.conftest", "flext_docker"),
    "get_column_names": ("tests.e2e.conftest", "get_column_names"),
    "logger": ("tests.e2e.conftest", "logger"),
    "postgres_container": ("tests.e2e.conftest", "postgres_container"),
    "project_root": ("tests.e2e.conftest", "project_root"),
    "query_database": ("tests.e2e.conftest", "query_database"),
    "run_dbt_command": ("tests.e2e.conftest", "run_dbt_command"),
    "table_exists": ("tests.e2e.conftest", "table_exists"),
}

__all__ = [
    "POSTGRES_READY_MAX_RETRIES",
    "count_rows",
    "db_connection",
    "dbt_profiles_dir",
    "dbt_project_dir",
    "flext_docker",
    "get_column_names",
    "logger",
    "postgres_container",
    "project_root",
    "query_database",
    "run_dbt_command",
    "table_exists",
]


def __getattr__(name: str) -> FlextTypes.ModuleExport:
    """Lazy-load module attributes on first access (PEP 562)."""
    return lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete."""
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
