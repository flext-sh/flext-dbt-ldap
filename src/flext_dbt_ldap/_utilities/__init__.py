# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Utilities package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports
from flext_dbt_ldap._utilities.client import FlextDbtLdapUtilitiesClient
from flext_dbt_ldap._utilities.integration import FlextDbtLdapUtilitiesIntegration
from flext_dbt_ldap._utilities.macros import FlextDbtLdapUtilitiesMacros
from flext_dbt_ldap._utilities.sync import FlextDbtLdapUtilitiesSync

if _t.TYPE_CHECKING:
    import flext_dbt_ldap._utilities.client as _flext_dbt_ldap__utilities_client

    client = _flext_dbt_ldap__utilities_client
    import flext_dbt_ldap._utilities.integration as _flext_dbt_ldap__utilities_integration

    integration = _flext_dbt_ldap__utilities_integration
    import flext_dbt_ldap._utilities.macros as _flext_dbt_ldap__utilities_macros

    macros = _flext_dbt_ldap__utilities_macros
    import flext_dbt_ldap._utilities.sync as _flext_dbt_ldap__utilities_sync

    sync = _flext_dbt_ldap__utilities_sync

    _ = (
        FlextDbtLdapUtilitiesClient,
        FlextDbtLdapUtilitiesIntegration,
        FlextDbtLdapUtilitiesMacros,
        FlextDbtLdapUtilitiesSync,
        client,
        integration,
        macros,
        sync,
    )
_LAZY_IMPORTS = {
    "FlextDbtLdapUtilitiesClient": "flext_dbt_ldap._utilities.client",
    "FlextDbtLdapUtilitiesIntegration": "flext_dbt_ldap._utilities.integration",
    "FlextDbtLdapUtilitiesMacros": "flext_dbt_ldap._utilities.macros",
    "FlextDbtLdapUtilitiesSync": "flext_dbt_ldap._utilities.sync",
    "client": "flext_dbt_ldap._utilities.client",
    "integration": "flext_dbt_ldap._utilities.integration",
    "macros": "flext_dbt_ldap._utilities.macros",
    "sync": "flext_dbt_ldap._utilities.sync",
}

__all__ = [
    "FlextDbtLdapUtilitiesClient",
    "FlextDbtLdapUtilitiesIntegration",
    "FlextDbtLdapUtilitiesMacros",
    "FlextDbtLdapUtilitiesSync",
    "client",
    "integration",
    "macros",
    "sync",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
