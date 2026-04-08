# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Utilities package."""

from __future__ import annotations

from flext_core.lazy import install_lazy_exports

_LAZY_IMPORTS = {
    "FlextDbtLdapUtilitiesClient": (
        "flext_dbt_ldap._utilities.client",
        "FlextDbtLdapUtilitiesClient",
    ),
    "FlextDbtLdapUtilitiesIntegration": (
        "flext_dbt_ldap._utilities.integration",
        "FlextDbtLdapUtilitiesIntegration",
    ),
    "FlextDbtLdapUtilitiesMacros": (
        "flext_dbt_ldap._utilities.macros",
        "FlextDbtLdapUtilitiesMacros",
    ),
    "FlextDbtLdapUtilitiesSync": (
        "flext_dbt_ldap._utilities.sync",
        "FlextDbtLdapUtilitiesSync",
    ),
    "client": "flext_dbt_ldap._utilities.client",
    "integration": "flext_dbt_ldap._utilities.integration",
    "macros": "flext_dbt_ldap._utilities.macros",
    "sync": "flext_dbt_ldap._utilities.sync",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, publish_all=False)
