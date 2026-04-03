# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Utilities package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if _TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_dbt_ldap import client, integration, macros, sync
    from flext_dbt_ldap.client import FlextDbtLdapUtilitiesClient
    from flext_dbt_ldap.integration import FlextDbtLdapUtilitiesIntegration
    from flext_dbt_ldap.macros import FlextDbtLdapUtilitiesMacros
    from flext_dbt_ldap.sync import FlextDbtLdapUtilitiesSync

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = {
    "FlextDbtLdapUtilitiesClient": "flext_dbt_ldap.client",
    "FlextDbtLdapUtilitiesIntegration": "flext_dbt_ldap.integration",
    "FlextDbtLdapUtilitiesMacros": "flext_dbt_ldap.macros",
    "FlextDbtLdapUtilitiesSync": "flext_dbt_ldap.sync",
    "client": "flext_dbt_ldap.client",
    "integration": "flext_dbt_ldap.integration",
    "macros": "flext_dbt_ldap.macros",
    "sync": "flext_dbt_ldap.sync",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
