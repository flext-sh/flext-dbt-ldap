"""FLEXT DBT LDAP Constants - LDAP DBT transformation constants.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar, Final

from flext_ldap import FlextLdapConstants
from flext_meltano import FlextMeltanoConstants

if TYPE_CHECKING:
    from flext_dbt_ldap import t


class FlextDbtLdapConstants(FlextMeltanoConstants, FlextLdapConstants):
    """LDAP DBT transformation-specific constants following FLEXT unified pattern with nested domains.

    LDAP protocol constants are inherited from c.Ldap via MRO:
    - c.Ldap.ConnectionDefaults (PORT, TIMEOUT)
    - c.Ldap.LdapAttributeNames (DN, OBJECT_CLASS, COMMON_NAME — protocol-only)
    - c.Ldap.Filters.ALL_ENTRIES_FILTER (protocol-level wildcard)
    - c.Ldap.OperationType / c.Ldap.LdapOperationNames

    Domain-specific LDAP constants (attributes, filters, schema mappings, entity types)
    live in c.DbtLdap.LdapAttributes, c.DbtLdap.Filters, etc.
    """

    class DbtLdap:
        """DBT-LDAP-specific constants (not available in parent c.Ldap)."""

        class LdapAttributes:
            """Project-specific LDAP attribute selections for dbt transformations.

            LDAP attributes are dynamic (hundreds possible per schema).
            These are this project's CONFIGURED attribute set, not universal constants.
            """

            UID: Final[str] = "uid"
            CN: Final[str] = "cn"
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
            OBJECT_CLASS: Final[str] = "objectClass"
            EMPLOYEE_NUMBER: Final[str] = "employeeNumber"
            TELEPHONE_NUMBER: Final[str] = "telephoneNumber"
            USER_ACCOUNT_CONTROL: Final[str] = "userAccountControl"
            CREATE_TIMESTAMP: Final[str] = "createTimestamp"
            MODIFY_TIMESTAMP: Final[str] = "modifyTimestamp"
            MEMBER_UID: Final[str] = "memberUid"
            DN: Final[str] = "dn"
            USER_ID_ATTRIBUTES: ClassVar[t.StrSequence] = (
                "uid",
                "cn",
                "samaccountname",
            )
            MEMBERSHIP_ATTRIBUTES: ClassVar[t.StrSequence] = (
                "member",
                "uniqueMember",
                "memberUid",
            )

        class LdapSchemaMapping:
            """Project-specific LDAP schema class mappings."""

            USERS_CLASSES: ClassVar[t.StrSequence] = (
                "person",
                "user",
                "inetOrgPerson",
            )
            GROUPS_CLASSES: ClassVar[t.StrSequence] = (
                "group",
                "groupOfNames",
                "groupOfUniqueNames",
            )
            ORG_UNITS_CLASSES: ClassVar[t.StrSequence] = (
                "organizationalUnit",
                "organization",
            )

        class LdapEntityTypes:
            """Project-specific entity type identifiers."""

            USERS: Final[str] = "users"
            GROUPS: Final[str] = "groups"
            ORG_UNITS: Final[str] = "org_units"

        class Filters:
            """Project-specific LDAP search filters."""

            DEFAULT: Final[str] = "(objectClass=*)"
            USER: Final[str] = "(objectClass=person)"
            GROUP: Final[str] = "(objectClass=group)"
            MEMBERSHIP: Final[str] = "(|(objectClass=person)(objectClass=group))"

        class SearchAttributes:
            """Project-specific attribute sets for LDAP searches."""

            GROUP: ClassVar[t.StrSequence] = (
                "cn",
                "description",
                "member",
                "groupType",
            )
            MEMBERSHIP: ClassVar[t.StrSequence] = (
                "cn",
                "member",
                "memberOf",
                "uniqueMember",
            )

        class Ldaps:
            """Secure LDAP connection settings."""

            DEFAULT_PORT: Final[int] = 636

        class Dbt:
            """DBT-specific configuration constants."""

            DEFAULT_PROFILES_DIR = "./profiles"
            DEFAULT_TARGET = "dev"
            ALLOWED_TARGETS: ClassVar[t.StrSequence] = ("dev", "staging", "prod")

        class DbtModels:
            """DBT model names for LDAP transformations."""

            STG_USERS: Final[str] = "stg_users"
            DIM_USERS: Final[str] = "dim_users"
            STG_GROUPS: Final[str] = "stg_groups"
            DIM_GROUPS: Final[str] = "dim_groups"
            FACT_MEMBERSHIPS: Final[str] = "fact_memberships"

        class DataTypes:
            """LDAP attribute to SQL data type mappings."""

            TIMESTAMP_ATTRS: Final[t.StrSequence] = (
                "createtimestamp",
                "modifytimestamp",
            )
            ARRAY_ATTRS: Final[t.StrSequence] = ("memberof", "objectclass")
            INTEGER_ATTRS: Final[t.StrSequence] = ("uidnumber", "gidnumber")
            TIMESTAMP: Final[str] = "timestamp"
            TEXT_ARRAY: Final[str] = "text[]"
            INTEGER: Final[str] = "integer"
            TEXT: Final[str] = "text"

        class MembershipTypes:
            """Membership type identifiers."""

            DIRECT: Final[str] = "direct"

        class Statuses:
            """Common status string constants."""

            COMPLETED: Final[str] = "completed"
            OPERATIONAL: Final[str] = "operational"
            PENDING: Final[str] = "pending"

        class DbtProcessing:
            """DBT LDAP transformation configuration."""

            DEFAULT_BATCH_SIZE = FlextMeltanoConstants.DEFAULT_SIZE
            MAX_BATCH_SIZE = FlextMeltanoConstants.MAX_ITEMS

        class TransformationOptimization:
            """Transformation optimization performance thresholds."""

            PERFORMANCE_EXECUTION_TIME_THRESHOLD: Final[float] = 30.0
            PERFORMANCE_MEMORY_USAGE_THRESHOLD: Final[float] = 1024.0
            PERFORMANCE_ROWS_PROCESSED_THRESHOLD: Final[int] = 100000


c = FlextDbtLdapConstants

__all__ = ["FlextDbtLdapConstants", "c"]
