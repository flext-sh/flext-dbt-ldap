"""FLEXT DBT LDAP Models - Placeholder module for MyPy compatibility.

This module exists to satisfy MyPy import checking.
All actual models are imported from flext-ldap library.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_ldap import (
    FlextLdapCreateUserRequest,
    FlextLdapDistinguishedName,
    FlextLdapEntry,
    FlextLdapGroup,
    FlextLdapUser,
)


# Placeholder classes for missing imports
class GroupDimension:
    """Placeholder for GroupDimension."""


class LDAPTransformer:
    """Placeholder for LDAPTransformer."""


class UserDimension:
    """Placeholder for UserDimension."""


# Re-export for backwards compatibility
__all__: list[str] = [
    "FlextLdapCreateUserRequest",
    "FlextLdapDistinguishedName",
    "FlextLdapEntry",
    "FlextLdapGroup",
    "FlextLdapUser",
    "GroupDimension",
    "LDAPTransformer",
    "UserDimension",
]
