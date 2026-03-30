# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_tests import *

    from tests import conftest, constants, models, protocols, typings, utilities
    from tests.conftest import *
    from tests.constants import *
    from tests.e2e import *
    from tests.models import *
    from tests.protocols import *
    from tests.typings import *
    from tests.unit import *
    from tests.utilities import *

_LAZY_IMPORTS: Mapping[str, str | Sequence[str]] = {
    "FlextDbtLdapTestConstants": "tests.constants",
    "FlextDbtLdapTestModels": "tests.models",
    "FlextDbtLdapTestProtocols": "tests.protocols",
    "FlextDbtLdapTestTypes": "tests.typings",
    "FlextDbtLdapTestUtilities": "tests.utilities",
    "MockLdapConnection": "tests.conftest",
    "MockLdapDbtAdapter": "tests.conftest",
    "POSTGRES_READY_MAX_RETRIES": "tests.e2e.conftest",
    "c": ["tests.constants", "FlextDbtLdapTestConstants"],
    "conftest": "tests.conftest",
    "constants": "tests.constants",
    "count_rows": "tests.e2e.conftest",
    "d": "flext_tests",
    "db_connection": "tests.e2e.conftest",
    "dbt_ldap_macros": "tests.conftest",
    "dbt_ldap_models": "tests.conftest",
    "dbt_ldap_profile": "tests.conftest",
    "dbt_ldap_project_config": "tests.conftest",
    "dbt_ldap_sources": "tests.conftest",
    "dbt_ldap_tests": "tests.conftest",
    "dbt_profiles_dir": "tests.e2e.conftest",
    "dbt_project_dir": "tests.e2e.conftest",
    "e": "flext_tests",
    "e2e": "tests.e2e",
    "flext_docker": "tests.e2e.conftest",
    "get_column_names": "tests.e2e.conftest",
    "h": "flext_tests",
    "ldap_performance_config": "tests.conftest",
    "ldap_source_config": "tests.conftest",
    "ldap_validation_rules": "tests.conftest",
    "logger": "tests.e2e.conftest",
    "m": ["tests.models", "FlextDbtLdapTestModels"],
    "mock_ldap_connection": "tests.conftest",
    "mock_ldap_dbt_adapter": "tests.conftest",
    "models": "tests.models",
    "p": ["tests.protocols", "FlextDbtLdapTestProtocols"],
    "postgres_container": "tests.e2e.conftest",
    "project_root": "tests.e2e.conftest",
    "protocols": "tests.protocols",
    "psycopg": "tests.e2e.conftest",
    "pytest_configure": "tests.conftest",
    "query_database": "tests.e2e.conftest",
    "r": "flext_tests",
    "run_dbt_command": "tests.e2e.conftest",
    "s": "flext_tests",
    "sample_ldap_entries": "tests.conftest",
    "set_test_environment": "tests.conftest",
    "shared_ldap_config": "tests.conftest",
    "shared_ldap_container": "tests.conftest",
    "sql": "tests.e2e.conftest",
    "t": ["tests.typings", "FlextDbtLdapTestTypes"],
    "table_exists": "tests.e2e.conftest",
    "test_dbt_services_sync": "tests.unit.test_dbt_services_sync",
    "test_dunder_alignment": "tests.unit.test_version",
    "test_incremental_groups_sync_applies_bookmark_filter": "tests.unit.test_version",
    "test_incremental_users_sync_applies_bookmark_filter": "tests.unit.test_version",
    "test_sync_users_uses_incremental_bookmark_and_persists_state": "tests.unit.test_dbt_services_sync",
    "test_version": "tests.unit.test_version",
    "test_version_metadata_integrity": "tests.unit.test_version",
    "test_version_properties": "tests.unit.test_version",
    "typings": "tests.typings",
    "u": ["tests.utilities", "FlextDbtLdapTestUtilities"],
    "unit": "tests.unit",
    "utilities": "tests.utilities",
    "x": "flext_tests",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, sorted(_LAZY_IMPORTS))
