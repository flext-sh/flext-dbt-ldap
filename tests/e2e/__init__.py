# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""E2e package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports

if _t.TYPE_CHECKING:
    import tests.e2e.conftest as _tests_e2e_conftest

    conftest = _tests_e2e_conftest
    from flext_core.constants import FlextConstants as c
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.models import FlextModels as m
    from flext_core.protocols import FlextProtocols as p
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
    from flext_core.typings import FlextTypes as t
    from flext_core.utilities import FlextUtilities as u
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
_LAZY_IMPORTS = {
    "POSTGRES_READY_MAX_RETRIES": "tests.e2e.conftest",
    "c": ("flext_core.constants", "FlextConstants"),
    "conftest": "tests.e2e.conftest",
    "count_rows": "tests.e2e.conftest",
    "d": ("flext_core.decorators", "FlextDecorators"),
    "db_connection": "tests.e2e.conftest",
    "dbt_profiles_dir": "tests.e2e.conftest",
    "dbt_project_dir": "tests.e2e.conftest",
    "e": ("flext_core.exceptions", "FlextExceptions"),
    "flext_docker": "tests.e2e.conftest",
    "get_column_names": "tests.e2e.conftest",
    "h": ("flext_core.handlers", "FlextHandlers"),
    "logger": "tests.e2e.conftest",
    "m": ("flext_core.models", "FlextModels"),
    "p": ("flext_core.protocols", "FlextProtocols"),
    "postgres_container": "tests.e2e.conftest",
    "project_root": "tests.e2e.conftest",
    "psycopg": "tests.e2e.conftest",
    "query_database": "tests.e2e.conftest",
    "r": ("flext_core.result", "FlextResult"),
    "run_dbt_command": "tests.e2e.conftest",
    "s": ("flext_core.service", "FlextService"),
    "sql": "tests.e2e.conftest",
    "t": ("flext_core.typings", "FlextTypes"),
    "table_exists": "tests.e2e.conftest",
    "u": ("flext_core.utilities", "FlextUtilities"),
    "x": ("flext_core.mixins", "FlextMixins"),
}

__all__ = [
    "POSTGRES_READY_MAX_RETRIES",
    "c",
    "conftest",
    "count_rows",
    "d",
    "db_connection",
    "dbt_profiles_dir",
    "dbt_project_dir",
    "e",
    "flext_docker",
    "get_column_names",
    "h",
    "logger",
    "m",
    "p",
    "postgres_container",
    "project_root",
    "psycopg",
    "query_database",
    "r",
    "run_dbt_command",
    "s",
    "sql",
    "t",
    "table_exists",
    "u",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
