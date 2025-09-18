"""FLEXT dbt LDAP Models - DBT LDAP data transformation models.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_core import FlextTypes
from flext_dbt_ldap.dbt_models import (
    FlextDbtLdapModels,
    FlextLdapCreateUserRequest,
    FlextLdapDistinguishedName,
    FlextLdapEntities,
    FlextLdapGroup,
    FlextLdapUser,
    GroupDimension,
    LDAPTransformer,
    MembershipFact,
    UserDimension,
)

# Backward compatibility aliases - now using correct imports
FlextDbtLdapGroupDimension = GroupDimension
FlextDbtLdapTransformer = LDAPTransformer
FlextDbtLdapUserDimension = UserDimension
FlextDbtLdapMembershipFact = MembershipFact

# Re-export for backwards compatibility
__all__: FlextTypes.Core.StringList = [
    "FlextDbtLdapGroupDimension",
    "FlextDbtLdapMembershipFact",
    "FlextDbtLdapModels",
    "FlextDbtLdapTransformer",
    "FlextDbtLdapUserDimension",
    "FlextLdapCreateUserRequest",
    "FlextLdapDistinguishedName",
    "FlextLdapEntities",
    "FlextLdapGroup",
    "FlextLdapUser",
    "GroupDimension",
    "LDAPTransformer",
    "MembershipFact",
    "UserDimension",
]
