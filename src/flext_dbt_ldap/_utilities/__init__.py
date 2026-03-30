# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""FLEXT DBT LDAP Utilities subpackage.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_dbt_ldap._utilities import (
        client as client,
        integration as integration,
        macros as macros,
        sync as sync,
    )
    from flext_dbt_ldap._utilities.client import (
        FlextDbtLdapUtilitiesClient as FlextDbtLdapUtilitiesClient,
    )
    from flext_dbt_ldap._utilities.integration import (
        FlextDbtLdapUtilitiesIntegration as FlextDbtLdapUtilitiesIntegration,
    )
    from flext_dbt_ldap._utilities.macros import (
        FlextDbtLdapUtilitiesMacros as FlextDbtLdapUtilitiesMacros,
    )
    from flext_dbt_ldap._utilities.sync import (
        FlextDbtLdapUtilitiesSync as FlextDbtLdapUtilitiesSync,
        logger as logger,
    )

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "FlextDbtLdapUtilitiesClient": [
        "flext_dbt_ldap._utilities.client",
        "FlextDbtLdapUtilitiesClient",
    ],
    "FlextDbtLdapUtilitiesIntegration": [
        "flext_dbt_ldap._utilities.integration",
        "FlextDbtLdapUtilitiesIntegration",
    ],
    "FlextDbtLdapUtilitiesMacros": [
        "flext_dbt_ldap._utilities.macros",
        "FlextDbtLdapUtilitiesMacros",
    ],
    "FlextDbtLdapUtilitiesSync": [
        "flext_dbt_ldap._utilities.sync",
        "FlextDbtLdapUtilitiesSync",
    ],
    "client": ["flext_dbt_ldap._utilities.client", ""],
    "integration": ["flext_dbt_ldap._utilities.integration", ""],
    "logger": ["flext_dbt_ldap._utilities.sync", "logger"],
    "macros": ["flext_dbt_ldap._utilities.macros", ""],
    "sync": ["flext_dbt_ldap._utilities.sync", ""],
}

_EXPORTS: Sequence[str] = [
    "FlextDbtLdapUtilitiesClient",
    "FlextDbtLdapUtilitiesIntegration",
    "FlextDbtLdapUtilitiesMacros",
    "FlextDbtLdapUtilitiesSync",
    "client",
    "integration",
    "logger",
    "macros",
    "sync",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, _EXPORTS)
