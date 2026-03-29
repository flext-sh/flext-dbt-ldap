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
    """LDAP DBT transformation-specific constants following FLEXT unified pattern with nested domains.

    LDAP-generic constants are inherited from c.Ldap via MRO:
    - c.Ldap.ConnectionDefaults (PORT, TIMEOUT)
    - c.Ldap.LdapAttributeNames (UID, CN, MAIL, etc.)
    - c.Ldap.Filters (USER, GROUP, MEMBERSHIP, ALL_ENTRIES_FILTER)
    - c.Ldap.SearchAttributes (GROUP, MEMBERSHIP)
    - c.Ldap.SchemaMapping (USERS_CLASSES, GROUPS_CLASSES, ORG_UNITS_CLASSES)
    - c.Ldap.EntityTypes (USERS, GROUPS, ORG_UNITS)
    - c.Ldap.OperationType / c.Ldap.LdapOperationNames
    """

    class DbtLdap:
        """DBT-LDAP-specific constants (not available in parent c.Ldap)."""

        class Ldaps:
            """Secure LDAP connection settings."""

            DEFAULT_PORT: Final[int] = 636

        class Dbt:
            """DBT-specific configuration constants."""

            DEFAULT_PROFILES_DIR = "./profiles"
            DEFAULT_TARGET = "dev"
            ALLOWED_TARGETS: ClassVar[t.StrSequence] = ["dev", "staging", "prod"]

        class DbtModels:
            """DBT model names for LDAP transformations."""

            STG_USERS: Final[str] = "stg_users"
            DIM_USERS: Final[str] = "dim_users"
            STG_GROUPS: Final[str] = "stg_groups"
            DIM_GROUPS: Final[str] = "dim_groups"
            FACT_MEMBERSHIPS: Final[str] = "fact_memberships"

        class DataTypes:
            """LDAP attribute to SQL data type mappings."""

            TIMESTAMP_ATTRS: Final[t.StrSequence] = [
                "createtimestamp",
                "modifytimestamp",
            ]
            ARRAY_ATTRS: Final[t.StrSequence] = ["memberof", "objectclass"]
            INTEGER_ATTRS: Final[t.StrSequence] = ["uidnumber", "gidnumber"]
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
