"""FlextDbtLdapConstantsAttributes - LDAP attribute and schema constants.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import ClassVar

from flext_ldap import FlextLdapConstants


class FlextDbtLdapConstantsAttributes:
    """Project-specific LDAP attributes and schema mappings."""

    UID: ClassVar[str] = "uid"
    CN: ClassVar[str] = FlextLdapConstants.Ldap.AttributeName.COMMON_NAME
    MAIL: ClassVar[str] = "mail"
    DISPLAY_NAME: ClassVar[str] = "displayName"
    DEPARTMENT: ClassVar[str] = "department"
    MANAGER: ClassVar[str] = "manager"
    DESCRIPTION: ClassVar[str] = "description"
    MEMBER: ClassVar[str] = "member"
    GROUP_TYPE: ClassVar[str] = "groupType"
    MEMBER_OF: ClassVar[str] = "memberOf"
    UNIQUE_MEMBER: ClassVar[str] = "uniqueMember"
    SAM_ACCOUNT_NAME: ClassVar[str] = "samaccountname"
    EMPLOYEE_NUMBER: ClassVar[str] = "employeeNumber"
    TELEPHONE_NUMBER: ClassVar[str] = "telephoneNumber"
    USER_ACCOUNT_CONTROL: ClassVar[str] = "userAccountControl"
    CREATE_TIMESTAMP: ClassVar[str] = "createTimestamp"
    MODIFY_TIMESTAMP: ClassVar[str] = "modifyTimestamp"
    MEMBER_UID: ClassVar[str] = "memberUid"
    MEMBERSHIP_ATTRIBUTES: ClassVar[tuple[str, ...]] = (
        MEMBER,
        UNIQUE_MEMBER,
        MEMBER_UID,
    )
    USERS_CLASSES: ClassVar[tuple[str, ...]] = (
        "person",
        "user",
        "inetOrgPerson",
    )
    GROUPS_CLASSES: ClassVar[tuple[str, ...]] = (
        "group",
        "groupOfNames",
        "groupOfUniqueNames",
    )
    ORG_UNITS_CLASSES: ClassVar[tuple[str, ...]] = (
        "organizationalUnit",
        "organization",
    )
    USERS: ClassVar[str] = "users"
    GROUPS: ClassVar[str] = "groups"
    ORG_UNITS: ClassVar[str] = "org_units"


__all__: list[str] = ["FlextDbtLdapConstantsAttributes"]
