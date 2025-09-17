"""FLEXT dbt LDAP Models - DBT LDAP data transformation models.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_core import FlextTypes
from flext_dbt_ldap.dbt_models import (
    FlextDbtLdapGroupDimension,
    FlextDbtLdapMembershipFact,
    FlextDbtLdapTransformer,
    FlextDbtLdapUserDimension,
    FlextLdapCreateUserRequest,
    FlextLdapDistinguishedName,
    FlextLdapEntities,
    FlextLdapGroup,
    FlextLdapUser,
)

# Backward compatibility aliases
GroupDimension = FlextDbtLdapGroupDimension
LDAPTransformer = FlextDbtLdapTransformer
UserDimension = FlextDbtLdapUserDimension

# Re-export for backwards compatibility
__all__: FlextTypes.Core.StringList = [
    "FlextDbtLdapGroupDimension",
    "FlextDbtLdapMembershipFact",
    "FlextDbtLdapTransformer",
    "FlextDbtLdapUserDimension",
    "FlextLdapCreateUserRequest",
    "FlextLdapDistinguishedName",
    "FlextLdapEntities",
    "FlextLdapGroup",
    "FlextLdapUser",
    "GroupDimension",
    "LDAPTransformer",
    "UserDimension",
]
