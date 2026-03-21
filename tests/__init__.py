# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make codegen
#
"""Tests package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core.typings import FlextTypes

    from . import e2e as e2e, unit as unit
    from .conftest import (
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
        sample_ldap_entries,
        set_test_environment,
        shared_ldap_config,
        shared_ldap_container,
    )
    from .constants import TestsFlextDbtLdapConstants, TestsFlextDbtLdapConstants as c
    from .e2e.conftest import (
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
    from .models import TestsFlextDbtLdapModels, TestsFlextDbtLdapModels as m
    from .protocols import TestsFlextDbtLdapProtocols, TestsFlextDbtLdapProtocols as p
    from .typings import TestsFlextDbtLdapTypes, TestsFlextDbtLdapTypes as t
    from .unit.test_dbt_services_sync import (
        test_sync_users_uses_incremental_bookmark_and_persists_state,
    )
    from .unit.test_version import (
        test_dunder_alignment,
        test_incremental_groups_sync_applies_bookmark_filter,
        test_incremental_users_sync_applies_bookmark_filter,
        test_version_metadata_integrity,
        test_version_properties,
    )
    from .utilities import TestsFlextDbtLdapUtilities, TestsFlextDbtLdapUtilities as u

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "MockLdapConnection": ("tests.conftest", "MockLdapConnection"),
    "MockLdapDbtAdapter": ("tests.conftest", "MockLdapDbtAdapter"),
    "POSTGRES_READY_MAX_RETRIES": ("tests.e2e.conftest", "POSTGRES_READY_MAX_RETRIES"),
    "TestsFlextDbtLdapConstants": ("tests.constants", "TestsFlextDbtLdapConstants"),
    "TestsFlextDbtLdapModels": ("tests.models", "TestsFlextDbtLdapModels"),
    "TestsFlextDbtLdapProtocols": ("tests.protocols", "TestsFlextDbtLdapProtocols"),
    "TestsFlextDbtLdapTypes": ("tests.typings", "TestsFlextDbtLdapTypes"),
    "TestsFlextDbtLdapUtilities": ("tests.utilities", "TestsFlextDbtLdapUtilities"),
    "c": ("tests.constants", "TestsFlextDbtLdapConstants"),
    "count_rows": ("tests.e2e.conftest", "count_rows"),
    "db_connection": ("tests.e2e.conftest", "db_connection"),
    "dbt_ldap_macros": ("tests.conftest", "dbt_ldap_macros"),
    "dbt_ldap_models": ("tests.conftest", "dbt_ldap_models"),
    "dbt_ldap_profile": ("tests.conftest", "dbt_ldap_profile"),
    "dbt_ldap_project_config": ("tests.conftest", "dbt_ldap_project_config"),
    "dbt_ldap_sources": ("tests.conftest", "dbt_ldap_sources"),
    "dbt_ldap_tests": ("tests.conftest", "dbt_ldap_tests"),
    "dbt_profiles_dir": ("tests.e2e.conftest", "dbt_profiles_dir"),
    "dbt_project_dir": ("tests.e2e.conftest", "dbt_project_dir"),
    "e2e": ("tests.e2e", ""),
    "flext_docker": ("tests.e2e.conftest", "flext_docker"),
    "get_column_names": ("tests.e2e.conftest", "get_column_names"),
    "ldap_performance_config": ("tests.conftest", "ldap_performance_config"),
    "ldap_source_config": ("tests.conftest", "ldap_source_config"),
    "ldap_validation_rules": ("tests.conftest", "ldap_validation_rules"),
    "logger": ("tests.e2e.conftest", "logger"),
    "m": ("tests.models", "TestsFlextDbtLdapModels"),
    "mock_ldap_connection": ("tests.conftest", "mock_ldap_connection"),
    "mock_ldap_dbt_adapter": ("tests.conftest", "mock_ldap_dbt_adapter"),
    "p": ("tests.protocols", "TestsFlextDbtLdapProtocols"),
    "postgres_container": ("tests.e2e.conftest", "postgres_container"),
    "project_root": ("tests.e2e.conftest", "project_root"),
    "pytest_configure": ("tests.conftest", "pytest_configure"),
    "query_database": ("tests.e2e.conftest", "query_database"),
    "run_dbt_command": ("tests.e2e.conftest", "run_dbt_command"),
    "sample_ldap_entries": ("tests.conftest", "sample_ldap_entries"),
    "set_test_environment": ("tests.conftest", "set_test_environment"),
    "shared_ldap_config": ("tests.conftest", "shared_ldap_config"),
    "shared_ldap_container": ("tests.conftest", "shared_ldap_container"),
    "t": ("tests.typings", "TestsFlextDbtLdapTypes"),
    "table_exists": ("tests.e2e.conftest", "table_exists"),
    "test_dunder_alignment": ("tests.unit.test_version", "test_dunder_alignment"),
    "test_incremental_groups_sync_applies_bookmark_filter": (
        "tests.unit.test_version",
        "test_incremental_groups_sync_applies_bookmark_filter",
    ),
    "test_incremental_users_sync_applies_bookmark_filter": (
        "tests.unit.test_version",
        "test_incremental_users_sync_applies_bookmark_filter",
    ),
    "test_sync_users_uses_incremental_bookmark_and_persists_state": (
        "tests.unit.test_dbt_services_sync",
        "test_sync_users_uses_incremental_bookmark_and_persists_state",
    ),
    "test_version_metadata_integrity": (
        "tests.unit.test_version",
        "test_version_metadata_integrity",
    ),
    "test_version_properties": ("tests.unit.test_version", "test_version_properties"),
    "u": ("tests.utilities", "TestsFlextDbtLdapUtilities"),
    "unit": ("tests.unit", ""),
}

__all__ = [
    "POSTGRES_READY_MAX_RETRIES",
    "MockLdapConnection",
    "MockLdapDbtAdapter",
    "TestsFlextDbtLdapConstants",
    "TestsFlextDbtLdapModels",
    "TestsFlextDbtLdapProtocols",
    "TestsFlextDbtLdapTypes",
    "TestsFlextDbtLdapUtilities",
    "c",
    "count_rows",
    "db_connection",
    "dbt_ldap_macros",
    "dbt_ldap_models",
    "dbt_ldap_profile",
    "dbt_ldap_project_config",
    "dbt_ldap_sources",
    "dbt_ldap_tests",
    "dbt_profiles_dir",
    "dbt_project_dir",
    "e2e",
    "flext_docker",
    "get_column_names",
    "ldap_performance_config",
    "ldap_source_config",
    "ldap_validation_rules",
    "logger",
    "m",
    "mock_ldap_connection",
    "mock_ldap_dbt_adapter",
    "p",
    "postgres_container",
    "project_root",
    "pytest_configure",
    "query_database",
    "run_dbt_command",
    "sample_ldap_entries",
    "set_test_environment",
    "shared_ldap_config",
    "shared_ldap_container",
    "t",
    "table_exists",
    "test_dunder_alignment",
    "test_incremental_groups_sync_applies_bookmark_filter",
    "test_incremental_users_sync_applies_bookmark_filter",
    "test_sync_users_uses_incremental_bookmark_and_persists_state",
    "test_version_metadata_integrity",
    "test_version_properties",
    "u",
    "unit",
]


def __getattr__(name: str) -> FlextTypes.ModuleExport:
    """Lazy-load module attributes on first access (PEP 562)."""
    return lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete."""
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
