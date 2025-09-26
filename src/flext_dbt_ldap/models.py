"""FLEXT dbt LDAP Models - DBT LDAP data transformation models.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_dbt_ldap.dbt_models import FlextDbtLdapModels
from flext_dbt_ldap.typings import FlextDbtLdapTypes

# Direct export of unified models class - no aliases
__all__: FlextDbtLdapTypes.Core.StringList = [
    "FlextDbtLdapModels",
]
