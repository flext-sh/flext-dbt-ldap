# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports

if _t.TYPE_CHECKING:
    import tests.conftest as _tests_conftest

    conftest = _tests_conftest
    import tests.constants as _tests_constants
    from tests.conftest import (
        MockLdapConnection,
        MockLdapDbtAdapter,
        pytest_configure,
        pytest_plugins,
    )

    constants = _tests_constants
    import tests.models as _tests_models
    from tests.constants import (
        FlextDbtLdapTestConstants,
        FlextDbtLdapTestConstants as c,
    )
    from tests.e2e.conftest import (
        POSTGRES_READY_MAX_RETRIES,
        count_rows,
        get_column_names,
        logger,
        psycopg,
        query_database,
        run_dbt_command,
        sql,
        table_exists,
    )

    models = _tests_models
    import tests.protocols as _tests_protocols
    from tests.models import FlextDbtLdapTestModels, FlextDbtLdapTestModels as m

    protocols = _tests_protocols
    import tests.typings as _tests_typings
    from tests.protocols import (
        FlextDbtLdapTestProtocols,
        FlextDbtLdapTestProtocols as p,
    )

    typings = _tests_typings
    import tests.utilities as _tests_utilities
    from tests.typings import FlextDbtLdapTestTypes, FlextDbtLdapTestTypes as t

    utilities = _tests_utilities
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
    from tests.utilities import (
        FlextDbtLdapTestUtilities,
        FlextDbtLdapTestUtilities as u,
    )
_LAZY_IMPORTS = {
    "FlextDbtLdapTestConstants": ("tests.constants", "FlextDbtLdapTestConstants"),
    "FlextDbtLdapTestModels": ("tests.models", "FlextDbtLdapTestModels"),
    "FlextDbtLdapTestProtocols": ("tests.protocols", "FlextDbtLdapTestProtocols"),
    "FlextDbtLdapTestTypes": ("tests.typings", "FlextDbtLdapTestTypes"),
    "FlextDbtLdapTestUtilities": ("tests.utilities", "FlextDbtLdapTestUtilities"),
    "MockLdapConnection": ("tests.conftest", "MockLdapConnection"),
    "MockLdapDbtAdapter": ("tests.conftest", "MockLdapDbtAdapter"),
    "POSTGRES_READY_MAX_RETRIES": ("tests.e2e.conftest", "POSTGRES_READY_MAX_RETRIES"),
    "c": ("tests.constants", "FlextDbtLdapTestConstants"),
    "conftest": "tests.conftest",
    "constants": "tests.constants",
    "count_rows": ("tests.e2e.conftest", "count_rows"),
    "d": ("flext_core.decorators", "FlextDecorators"),
    "e": ("flext_core.exceptions", "FlextExceptions"),
    "get_column_names": ("tests.e2e.conftest", "get_column_names"),
    "h": ("flext_core.handlers", "FlextHandlers"),
    "logger": ("tests.e2e.conftest", "logger"),
    "m": ("tests.models", "FlextDbtLdapTestModels"),
    "models": "tests.models",
    "p": ("tests.protocols", "FlextDbtLdapTestProtocols"),
    "protocols": "tests.protocols",
    "psycopg": ("tests.e2e.conftest", "psycopg"),
    "pytest_configure": ("tests.conftest", "pytest_configure"),
    "pytest_plugins": ("tests.conftest", "pytest_plugins"),
    "query_database": ("tests.e2e.conftest", "query_database"),
    "r": ("flext_core.result", "FlextResult"),
    "run_dbt_command": ("tests.e2e.conftest", "run_dbt_command"),
    "s": ("flext_core.service", "FlextService"),
    "sql": ("tests.e2e.conftest", "sql"),
    "t": ("tests.typings", "FlextDbtLdapTestTypes"),
    "table_exists": ("tests.e2e.conftest", "table_exists"),
    "typings": "tests.typings",
    "u": ("tests.utilities", "FlextDbtLdapTestUtilities"),
    "utilities": "tests.utilities",
    "x": ("flext_core.mixins", "FlextMixins"),
}

__all__ = [
    "POSTGRES_READY_MAX_RETRIES",
    "FlextDbtLdapTestConstants",
    "FlextDbtLdapTestModels",
    "FlextDbtLdapTestProtocols",
    "FlextDbtLdapTestTypes",
    "FlextDbtLdapTestUtilities",
    "MockLdapConnection",
    "MockLdapDbtAdapter",
    "c",
    "conftest",
    "constants",
    "count_rows",
    "d",
    "e",
    "get_column_names",
    "h",
    "logger",
    "m",
    "models",
    "p",
    "protocols",
    "psycopg",
    "pytest_configure",
    "pytest_plugins",
    "query_database",
    "r",
    "run_dbt_command",
    "s",
    "sql",
    "t",
    "table_exists",
    "typings",
    "u",
    "utilities",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
