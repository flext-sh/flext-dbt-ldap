"""FLEXT DBT LDAP Models - Backward compatibility module.

Re-exports from dbt_models for backward compatibility.
All actual models are now in dbt_models module.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_dbt_ldap.dbt_models import (
    FlextDbtLdapGroupDimension,
    FlextDbtLdapMembershipFact,
    FlextDbtLdapTransformer,
    FlextDbtLdapUserDimension,
    FlextLdapCreateUserRequest,
    FlextLdapDistinguishedName,
    FlextLdapEntry,
    FlextLdapGroup,
    FlextLdapUser,
)

# Backward compatibility aliases
GroupDimension = FlextDbtLdapGroupDimension
LDAPTransformer = FlextDbtLdapTransformer
UserDimension = FlextDbtLdapUserDimension

# Re-export for backwards compatibility
__all__: list[str] = [
    "FlextDbtLdapGroupDimension",
    "FlextDbtLdapMembershipFact",
    "FlextDbtLdapTransformer",
    "FlextDbtLdapUserDimension",
    "FlextLdapCreateUserRequest",
    "FlextLdapDistinguishedName",
    "FlextLdapEntry",
    "FlextLdapGroup",
    "FlextLdapUser",
    "GroupDimension",
    "LDAPTransformer",
    "UserDimension",
]
