# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports, merge_lazy_imports

if _t.TYPE_CHECKING:
    import tests.conftest as _tests_conftest

    conftest = _tests_conftest
    import tests.constants as _tests_constants
    from tests.conftest import (
        MockLdapConnection,
        MockLdapDbtAdapter,
        dbt_ldap_macros,
        dbt_ldap_models,
        dbt_ldap_profile,
        dbt_ldap_project_config,
        dbt_ldap_sources,
        dbt_ldap_tests,
        ldap_performance_config,
        ldap_source_config,
        ldap_validation_rules,
        mock_ldap_connection,
        mock_ldap_dbt_adapter,
        pytest_configure,
        pytest_plugins,
        sample_ldap_entries,
        set_test_environment,
        shared_ldap_config,
        shared_ldap_container,
    )

    constants = _tests_constants
    import tests.e2e as _tests_e2e
    from tests.constants import (
        FlextDbtLdapTestConstants,
        FlextDbtLdapTestConstants as c,
    )

    e2e = _tests_e2e
    import tests.models as _tests_models
    from tests.e2e import (
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
    import tests.unit as _tests_unit
    from tests.typings import FlextDbtLdapTestTypes, FlextDbtLdapTestTypes as t

    unit = _tests_unit
    import tests.utilities as _tests_utilities
    from tests.unit import (
        test_dbt_services_sync,
        test_dunder_alignment,
        test_incremental_groups_sync_applies_bookmark_filter,
        test_incremental_users_sync_applies_bookmark_filter,
        test_sync_users_uses_incremental_bookmark_and_persists_state,
        test_version,
        test_version_metadata_integrity,
        test_version_properties,
    )

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
_LAZY_IMPORTS = merge_lazy_imports(
    (
        "tests.e2e",
        "tests.unit",
    ),
    {
        "FlextDbtLdapTestConstants": "tests.constants",
        "FlextDbtLdapTestModels": "tests.models",
        "FlextDbtLdapTestProtocols": "tests.protocols",
        "FlextDbtLdapTestTypes": "tests.typings",
        "FlextDbtLdapTestUtilities": "tests.utilities",
        "MockLdapConnection": "tests.conftest",
        "MockLdapDbtAdapter": "tests.conftest",
        "c": ("tests.constants", "FlextDbtLdapTestConstants"),
        "conftest": "tests.conftest",
        "constants": "tests.constants",
        "d": ("flext_core.decorators", "FlextDecorators"),
        "dbt_ldap_macros": "tests.conftest",
        "dbt_ldap_models": "tests.conftest",
        "dbt_ldap_profile": "tests.conftest",
        "dbt_ldap_project_config": "tests.conftest",
        "dbt_ldap_sources": "tests.conftest",
        "dbt_ldap_tests": "tests.conftest",
        "e": ("flext_core.exceptions", "FlextExceptions"),
        "e2e": "tests.e2e",
        "h": ("flext_core.handlers", "FlextHandlers"),
        "ldap_performance_config": "tests.conftest",
        "ldap_source_config": "tests.conftest",
        "ldap_validation_rules": "tests.conftest",
        "m": ("tests.models", "FlextDbtLdapTestModels"),
        "mock_ldap_connection": "tests.conftest",
        "mock_ldap_dbt_adapter": "tests.conftest",
        "models": "tests.models",
        "p": ("tests.protocols", "FlextDbtLdapTestProtocols"),
        "protocols": "tests.protocols",
        "pytest_configure": "tests.conftest",
        "pytest_plugins": "tests.conftest",
        "r": ("flext_core.result", "FlextResult"),
        "s": ("flext_core.service", "FlextService"),
        "sample_ldap_entries": "tests.conftest",
        "set_test_environment": "tests.conftest",
        "shared_ldap_config": "tests.conftest",
        "shared_ldap_container": "tests.conftest",
        "t": ("tests.typings", "FlextDbtLdapTestTypes"),
        "typings": "tests.typings",
        "u": ("tests.utilities", "FlextDbtLdapTestUtilities"),
        "unit": "tests.unit",
        "utilities": "tests.utilities",
        "x": ("flext_core.mixins", "FlextMixins"),
    },
)

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
    "db_connection",
    "dbt_ldap_macros",
    "dbt_ldap_models",
    "dbt_ldap_profile",
    "dbt_ldap_project_config",
    "dbt_ldap_sources",
    "dbt_ldap_tests",
    "dbt_profiles_dir",
    "dbt_project_dir",
    "e",
    "e2e",
    "flext_docker",
    "get_column_names",
    "h",
    "ldap_performance_config",
    "ldap_source_config",
    "ldap_validation_rules",
    "logger",
    "m",
    "mock_ldap_connection",
    "mock_ldap_dbt_adapter",
    "models",
    "p",
    "postgres_container",
    "project_root",
    "protocols",
    "psycopg",
    "pytest_configure",
    "pytest_plugins",
    "query_database",
    "r",
    "run_dbt_command",
    "s",
    "sample_ldap_entries",
    "set_test_environment",
    "shared_ldap_config",
    "shared_ldap_container",
    "sql",
    "t",
    "table_exists",
    "test_dbt_services_sync",
    "test_dunder_alignment",
    "test_incremental_groups_sync_applies_bookmark_filter",
    "test_incremental_users_sync_applies_bookmark_filter",
    "test_sync_users_uses_incremental_bookmark_and_persists_state",
    "test_version",
    "test_version_metadata_integrity",
    "test_version_properties",
    "typings",
    "u",
    "unit",
    "utilities",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
