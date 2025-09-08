"""FLEXT DBT LDAP Models - Backward compatibility module.

Re-exports from dbt_models for backward compatibility.
All actual models are now in dbt_models module.

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
    FlextLDAPCreateUserRequest,
    FlextLDAPDistinguishedName,
    FlextLDAPEntry,
    FlextLDAPGroup,
    FlextLDAPUser,
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
    "FlextLDAPCreateUserRequest",
    "FlextLDAPDistinguishedName",
    "FlextLDAPEntry",
    "FlextLDAPGroup",
    "FlextLDAPUser",
    "GroupDimension",
    "LDAPTransformer",
    "UserDimension",
]
