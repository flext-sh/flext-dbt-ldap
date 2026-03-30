# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""FLEXT DBT LDAP Utilities subpackage.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if _TYPE_CHECKING:
    from flext_dbt_ldap._utilities.client import *
    from flext_dbt_ldap._utilities.integration import *
    from flext_dbt_ldap._utilities.macros import *
    from flext_dbt_ldap._utilities.sync import *

_LAZY_IMPORTS: Mapping[str, str | Sequence[str]] = {
    "FlextDbtLdapUtilitiesClient": "flext_dbt_ldap._utilities.client",
    "FlextDbtLdapUtilitiesIntegration": "flext_dbt_ldap._utilities.integration",
    "FlextDbtLdapUtilitiesMacros": "flext_dbt_ldap._utilities.macros",
    "FlextDbtLdapUtilitiesSync": "flext_dbt_ldap._utilities.sync",
    "client": "flext_dbt_ldap._utilities.client",
    "integration": "flext_dbt_ldap._utilities.integration",
    "logger": "flext_dbt_ldap._utilities.sync",
    "macros": "flext_dbt_ldap._utilities.macros",
    "sync": "flext_dbt_ldap._utilities.sync",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
