"""FLEXT DBT LDAP Constants - LDAP DBT transformation constants.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from enum import StrEnum, unique
from typing import TYPE_CHECKING, ClassVar, Final

from flext_ldap import FlextLdapConstants
from flext_meltano import FlextMeltanoConstants

if TYPE_CHECKING:
    from flext_dbt_ldap import t


class FlextDbtLdapConstants(FlextMeltanoConstants, FlextLdapConstants):
    """LDAP DBT transformation-specific constants following FLEXT unified pattern with nested domains."""

    class DbtLdap:
        """LDAP connection configuration constants."""

        class Ldap:
            """Standard LDAP connection settings."""

            DEFAULT_HOST: Final[str] = FlextMeltanoConstants.DEFAULT_HOST
            DEFAULT_PORT: Final[int] = 389
            DEFAULT_TIMEOUT: Final[int] = FlextMeltanoConstants.DEFAULT_TIMEOUT_SECONDS

        class Ldaps:
            """Secure LDAP connection settings."""

            DEFAULT_PORT: Final[int] = 636

        class Dbt:
            """DBT-specific configuration constants."""

            DEFAULT_PROFILES_DIR = "./profiles"
            DEFAULT_TARGET = "dev"
            ALLOWED_TARGETS: ClassVar[t.StrSequence] = ["dev", "staging", "prod"]

        class LdapSchemaMapping:
            """LDAP t.NormalizedValue class to schema type mappings."""

            USERS_CLASSES: Final[t.StrSequence] = ["person", "user", "inetOrgPerson"]
            GROUPS_CLASSES: Final[t.StrSequence] = [
                "group",
                "groupOfNames",
                "groupOfUniqueNames",
            ]
            ORG_UNITS_CLASSES: Final[t.StrSequence] = [
                "organizationalUnit",
                "organization",
            ]

        class LdapEntityTypes:
            """LDAP entity type identifiers."""

            USERS: Final[str] = "users"
            GROUPS: Final[str] = "groups"
            ORG_UNITS: Final[str] = "org_units"

        class LdapAttributes:
            """Common LDAP attribute names."""

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
            USER_ID_ATTRIBUTES: Final[t.StrSequence] = ["uid", "cn", "samaccountname"]

        class DbtModels:
            """DBT model names for LDAP transformations."""

            STG_USERS: Final[str] = "stg_users"
            DIM_USERS: Final[str] = "dim_users"
            STG_GROUPS: Final[str] = "stg_groups"
            DIM_GROUPS: Final[str] = "dim_groups"
            FACT_MEMBERSHIPS: Final[str] = "fact_memberships"

        class DbtProcessing:
            """DBT LDAP transformation configuration."""

            DEFAULT_BATCH_SIZE = FlextMeltanoConstants.DEFAULT_SIZE
            MAX_BATCH_SIZE = FlextMeltanoConstants.MAX_ITEMS

        class TransformationOptimization:
            """Transformation optimization performance thresholds."""

            PERFORMANCE_EXECUTION_TIME_THRESHOLD: Final[float] = 30.0
            PERFORMANCE_MEMORY_USAGE_THRESHOLD: Final[float] = 1024.0
            PERFORMANCE_ROWS_PROCESSED_THRESHOLD: Final[int] = 100000

        @unique
        class LdapOperations(StrEnum):
            """LDAP operation types.

            DRY Pattern:
                StrEnum is the single source of truth. Use LdapOperations.SEARCH.value
                or LdapOperations.SEARCH directly - no base strings needed.
            """

            SEARCH = "search"
            BIND = "bind"
            UNBIND = "unbind"
            ADD = "add"
            MODIFY = "modify"
            DELETE = "delete"

        @unique
        class DbtCommands(StrEnum):
            """DBT command types.

            DRY Pattern:
                StrEnum is the single source of truth. Use DbtCommands.RUN.value
                or DbtCommands.RUN directly - no base strings needed.
            """

            RUN = "run"
            TEST = "test"
            BUILD = "build"
            SEED = "seed"
            SNAPSHOT = "snapshot"
            DOCS = "docs"


c = FlextDbtLdapConstants

__all__ = ["FlextDbtLdapConstants", "c"]
