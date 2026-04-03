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
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
    from flext_dbt_ldap import (
        conftest,
        constants,
        e2e,
        models,
        protocols,
        test_dbt_services_sync,
        test_version,
        typings,
        unit,
        utilities,
    )
    from flext_dbt_ldap.conftest import (
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
        sample_ldap_entries,
        set_test_environment,
        shared_ldap_config,
        shared_ldap_container,
    )
    from flext_dbt_ldap.constants import (
        FlextDbtLdapTestConstants,
        FlextDbtLdapTestConstants as c,
    )
    from flext_dbt_ldap.e2e import (
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
        sql,
        table_exists,
        text,
        var_string,
    )
    from flext_dbt_ldap.models import (
        FlextDbtLdapTestModels,
        FlextDbtLdapTestModels as m,
    )
    from flext_dbt_ldap.protocols import (
        FlextDbtLdapTestProtocols,
        FlextDbtLdapTestProtocols as p,
    )
    from flext_dbt_ldap.typings import FlextDbtLdapTestTypes, FlextDbtLdapTestTypes as t
    from flext_dbt_ldap.unit import (
        call_kwargs,
        mock_pipeline,
        persisted,
        result,
        return_value,
        service,
        state_file,
        test_dunder_alignment,
        test_sync_users_uses_incremental_bookmark_and_persists_state,
    )
    from flext_dbt_ldap.utilities import (
        FlextDbtLdapTestUtilities,
        FlextDbtLdapTestUtilities as u,
    )

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = merge_lazy_imports(
    (
        "flext_dbt_ldap.e2e",
        "flext_dbt_ldap.unit",
    ),
    {
        "FlextDbtLdapTestConstants": "flext_dbt_ldap.constants",
        "FlextDbtLdapTestModels": "flext_dbt_ldap.models",
        "FlextDbtLdapTestProtocols": "flext_dbt_ldap.protocols",
        "FlextDbtLdapTestTypes": "flext_dbt_ldap.typings",
        "FlextDbtLdapTestUtilities": "flext_dbt_ldap.utilities",
        "c": ("flext_dbt_ldap.constants", "FlextDbtLdapTestConstants"),
        "conftest": "flext_dbt_ldap.conftest",
        "constants": "flext_dbt_ldap.constants",
        "d": ("flext_core.decorators", "FlextDecorators"),
        "dbt_ldap_macros": "flext_dbt_ldap.conftest",
        "dbt_ldap_models": "flext_dbt_ldap.conftest",
        "dbt_ldap_profile": "flext_dbt_ldap.conftest",
        "dbt_ldap_project_config": "flext_dbt_ldap.conftest",
        "dbt_ldap_sources": "flext_dbt_ldap.conftest",
        "dbt_ldap_tests": "flext_dbt_ldap.conftest",
        "e": ("flext_core.exceptions", "FlextExceptions"),
        "e2e": "flext_dbt_ldap.e2e",
        "h": ("flext_core.handlers", "FlextHandlers"),
        "ldap_performance_config": "flext_dbt_ldap.conftest",
        "ldap_source_config": "flext_dbt_ldap.conftest",
        "ldap_validation_rules": "flext_dbt_ldap.conftest",
        "m": ("flext_dbt_ldap.models", "FlextDbtLdapTestModels"),
        "mock_ldap_connection": "flext_dbt_ldap.conftest",
        "mock_ldap_dbt_adapter": "flext_dbt_ldap.conftest",
        "models": "flext_dbt_ldap.models",
        "p": ("flext_dbt_ldap.protocols", "FlextDbtLdapTestProtocols"),
        "protocols": "flext_dbt_ldap.protocols",
        "r": ("flext_core.result", "FlextResult"),
        "s": ("flext_core.service", "FlextService"),
        "sample_ldap_entries": "flext_dbt_ldap.conftest",
        "set_test_environment": "flext_dbt_ldap.conftest",
        "shared_ldap_config": "flext_dbt_ldap.conftest",
        "shared_ldap_container": "flext_dbt_ldap.conftest",
        "t": ("flext_dbt_ldap.typings", "FlextDbtLdapTestTypes"),
        "test_dbt_services_sync": "flext_dbt_ldap.test_dbt_services_sync",
        "test_version": "flext_dbt_ldap.test_version",
        "typings": "flext_dbt_ldap.typings",
        "u": ("flext_dbt_ldap.utilities", "FlextDbtLdapTestUtilities"),
        "unit": "flext_dbt_ldap.unit",
        "utilities": "flext_dbt_ldap.utilities",
        "x": ("flext_core.mixins", "FlextMixins"),
    },
)


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
