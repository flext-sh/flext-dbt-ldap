"""FlextDbtLdapConstantsAttributes - LDAP attribute and schema constants.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import ClassVar, Final

from flext_dbt_ldap import t
from flext_ldap import FlextLdapConstants


class FlextDbtLdapConstantsAttributes:
    """Project-specific LDAP attributes and schema mappings."""

    UID: Final[str] = "uid"
    CN: Final[str] = FlextLdapConstants.Ldap.AttributeName.COMMON_NAME
    MAIL: Final[str] = "mail"
    DISPLAY_NAME: Final[str] = "displayName"
    DEPARTMENT: Final[str] = "department"
    MANAGER: Final[str] = "manager"
    DESCRIPTION: Final[str] = "description"
    MEMBER: Final[str] = "member"
    GROUP_TYPE: Final[str] = "groupType"
    MEMBER_OF: Final[str] = "memberOf"
    UNIQUE_MEMBER: Final[str] = "uniqueMember"
    SAM_ACCOUNT_NAME: Final[str] = "samaccountname"
    EMPLOYEE_NUMBER: Final[str] = "employeeNumber"
    TELEPHONE_NUMBER: Final[str] = "telephoneNumber"
    USER_ACCOUNT_CONTROL: Final[str] = "userAccountControl"
    CREATE_TIMESTAMP: Final[str] = "createTimestamp"
    MODIFY_TIMESTAMP: Final[str] = "modifyTimestamp"
    MEMBER_UID: Final[str] = "memberUid"
    USER_ID_ATTRIBUTES: ClassVar[t.VariadicTuple[str]] = (
        UID,
        CN,
        SAM_ACCOUNT_NAME,
    )
    MEMBERSHIP_ATTRIBUTES: ClassVar[t.VariadicTuple[str]] = (
        MEMBER,
        UNIQUE_MEMBER,
        MEMBER_UID,
    )
    USERS_CLASSES: ClassVar[t.VariadicTuple[str]] = (
        "person",
        "user",
        "inetOrgPerson",
    )
    GROUPS_CLASSES: ClassVar[t.VariadicTuple[str]] = (
        "group",
        "groupOfNames",
        "groupOfUniqueNames",
    )
    ORG_UNITS_CLASSES: ClassVar[t.VariadicTuple[str]] = (
        "organizationalUnit",
        "organization",
    )
    USERS: Final[str] = "users"
    GROUPS: Final[str] = "groups"
    ORG_UNITS: Final[str] = "org_units"
