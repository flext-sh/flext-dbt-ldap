# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports, merge_lazy_imports

if _TYPE_CHECKING:
    from flext_tests import d, e, h, r, s, x

    from tests.conftest import *
    from tests.constants import *
    from tests.e2e import *
    from tests.models import *
    from tests.protocols import *
    from tests.typings import *
    from tests.unit import *
    from tests.utilities import *

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
