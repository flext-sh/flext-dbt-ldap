# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""End-to-end tests for flext-dbt-ldap.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if _TYPE_CHECKING:
    from flext_core import FlextTypes
    from tests.e2e import conftest
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
        psycopg,
        query_database,
        run_dbt_command,
        sql,
        table_exists,
    )

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = {
    "POSTGRES_READY_MAX_RETRIES": "tests.e2e.conftest",
    "conftest": "tests.e2e.conftest",
    "count_rows": "tests.e2e.conftest",
    "db_connection": "tests.e2e.conftest",
    "dbt_profiles_dir": "tests.e2e.conftest",
    "dbt_project_dir": "tests.e2e.conftest",
    "flext_docker": "tests.e2e.conftest",
    "get_column_names": "tests.e2e.conftest",
    "logger": "tests.e2e.conftest",
    "postgres_container": "tests.e2e.conftest",
    "project_root": "tests.e2e.conftest",
    "psycopg": "tests.e2e.conftest",
    "query_database": "tests.e2e.conftest",
    "run_dbt_command": "tests.e2e.conftest",
    "sql": "tests.e2e.conftest",
    "table_exists": "tests.e2e.conftest",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
