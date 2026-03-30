# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""End-to-end tests for flext-dbt-ldap.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from tests.e2e import conftest as conftest
    from tests.e2e.conftest import (
        POSTGRES_READY_MAX_RETRIES as POSTGRES_READY_MAX_RETRIES,
        count_rows as count_rows,
        db_connection as db_connection,
        dbt_profiles_dir as dbt_profiles_dir,
        dbt_project_dir as dbt_project_dir,
        flext_docker as flext_docker,
        get_column_names as get_column_names,
        logger as logger,
        postgres_container as postgres_container,
        project_root as project_root,
        psycopg as psycopg,
        query_database as query_database,
        run_dbt_command as run_dbt_command,
        sql as sql,
        table_exists as table_exists,
    )

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "POSTGRES_READY_MAX_RETRIES": ["tests.e2e.conftest", "POSTGRES_READY_MAX_RETRIES"],
    "conftest": ["tests.e2e.conftest", ""],
    "count_rows": ["tests.e2e.conftest", "count_rows"],
    "db_connection": ["tests.e2e.conftest", "db_connection"],
    "dbt_profiles_dir": ["tests.e2e.conftest", "dbt_profiles_dir"],
    "dbt_project_dir": ["tests.e2e.conftest", "dbt_project_dir"],
    "flext_docker": ["tests.e2e.conftest", "flext_docker"],
    "get_column_names": ["tests.e2e.conftest", "get_column_names"],
    "logger": ["tests.e2e.conftest", "logger"],
    "postgres_container": ["tests.e2e.conftest", "postgres_container"],
    "project_root": ["tests.e2e.conftest", "project_root"],
    "psycopg": ["tests.e2e.conftest", "psycopg"],
    "query_database": ["tests.e2e.conftest", "query_database"],
    "run_dbt_command": ["tests.e2e.conftest", "run_dbt_command"],
    "sql": ["tests.e2e.conftest", "sql"],
    "table_exists": ["tests.e2e.conftest", "table_exists"],
}

_EXPORTS: Sequence[str] = [
    "POSTGRES_READY_MAX_RETRIES",
    "conftest",
    "count_rows",
    "db_connection",
    "dbt_profiles_dir",
    "dbt_project_dir",
    "flext_docker",
    "get_column_names",
    "logger",
    "postgres_container",
    "project_root",
    "psycopg",
    "query_database",
    "run_dbt_command",
    "sql",
    "table_exists",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, _EXPORTS)
