# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports, merge_lazy_imports

if _TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_tests import d, e, h, r, s, x

    from tests import (
        conftest,
        constants,
        e2e,
        models,
        protocols,
        typings,
        unit,
        utilities,
    )
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
        sample_ldap_entries,
        set_test_environment,
        shared_ldap_config,
        shared_ldap_container,
    )
    from tests.constants import (
        FlextDbtLdapTestConstants,
        FlextDbtLdapTestConstants as c,
    )
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
    from tests.models import FlextDbtLdapTestModels, FlextDbtLdapTestModels as m
    from tests.protocols import (
        FlextDbtLdapTestProtocols,
        FlextDbtLdapTestProtocols as p,
    )
    from tests.typings import FlextDbtLdapTestTypes, FlextDbtLdapTestTypes as t
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
    from tests.utilities import (
        FlextDbtLdapTestUtilities,
        FlextDbtLdapTestUtilities as u,
    )

_LAZY_IMPORTS: Mapping[str, str | Sequence[str]] = merge_lazy_imports(
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
        "d": "flext_tests",
        "dbt_ldap_macros": "tests.conftest",
        "dbt_ldap_models": "tests.conftest",
        "dbt_ldap_profile": "tests.conftest",
        "dbt_ldap_project_config": "tests.conftest",
        "dbt_ldap_sources": "tests.conftest",
        "dbt_ldap_tests": "tests.conftest",
        "e": "flext_tests",
        "e2e": "tests.e2e",
        "h": "flext_tests",
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
        "r": "flext_tests",
        "s": "flext_tests",
        "sample_ldap_entries": "tests.conftest",
        "set_test_environment": "tests.conftest",
        "shared_ldap_config": "tests.conftest",
        "shared_ldap_container": "tests.conftest",
        "t": ("tests.typings", "FlextDbtLdapTestTypes"),
        "typings": "tests.typings",
        "u": ("tests.utilities", "FlextDbtLdapTestUtilities"),
        "unit": "tests.unit",
        "utilities": "tests.utilities",
        "x": "flext_tests",
    },
)


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
