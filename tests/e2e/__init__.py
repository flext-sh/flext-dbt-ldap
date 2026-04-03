# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""E2e package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if _TYPE_CHECKING:
    from flext_core import FlextTypes
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
    from flext_dbt_ldap import conftest
    from flext_dbt_ldap.conftest import (
        POSTGRES_READY_MAX_RETRIES,
        capture_output,
        check,
        cmd,
        cwd,
        db_connection,
        dbt_profiles_dir,
        dbt_project_dir,
        env,
        flext_docker,
        logger,
        postgres_container,
        project_root,
        psycopg,
        query_database,
        result,
        sql,
        table_exists,
        text,
        var_string,
    )

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = {
    "POSTGRES_READY_MAX_RETRIES": "flext_dbt_ldap.conftest",
    "c": ("flext_core.constants", "FlextConstants"),
    "capture_output": "flext_dbt_ldap.conftest",
    "check": "flext_dbt_ldap.conftest",
    "cmd": "flext_dbt_ldap.conftest",
    "conftest": "flext_dbt_ldap.conftest",
    "cwd": "flext_dbt_ldap.conftest",
    "d": ("flext_core.decorators", "FlextDecorators"),
    "db_connection": "flext_dbt_ldap.conftest",
    "dbt_profiles_dir": "flext_dbt_ldap.conftest",
    "dbt_project_dir": "flext_dbt_ldap.conftest",
    "e": ("flext_core.exceptions", "FlextExceptions"),
    "env": "flext_dbt_ldap.conftest",
    "flext_docker": "flext_dbt_ldap.conftest",
    "h": ("flext_core.handlers", "FlextHandlers"),
    "logger": "flext_dbt_ldap.conftest",
    "m": ("flext_core.models", "FlextModels"),
    "p": ("flext_core.protocols", "FlextProtocols"),
    "postgres_container": "flext_dbt_ldap.conftest",
    "project_root": "flext_dbt_ldap.conftest",
    "psycopg": "flext_dbt_ldap.conftest",
    "query_database": "flext_dbt_ldap.conftest",
    "r": ("flext_core.result", "FlextResult"),
    "result": "flext_dbt_ldap.conftest",
    "s": ("flext_core.service", "FlextService"),
    "sql": "flext_dbt_ldap.conftest",
    "t": ("flext_core.typings", "FlextTypes"),
    "table_exists": "flext_dbt_ldap.conftest",
    "text": "flext_dbt_ldap.conftest",
    "u": ("flext_core.utilities", "FlextUtilities"),
    "var_string": "flext_dbt_ldap.conftest",
    "x": ("flext_core.mixins", "FlextMixins"),
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
