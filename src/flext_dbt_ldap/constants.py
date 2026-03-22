"""FLEXT DBT LDAP Constants - LDAP DBT transformation constants.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from enum import StrEnum, unique
from typing import ClassVar, Final, Literal

from flext_core import FlextConstants
from flext_ldap import FlextLdapConstants
from flext_meltano import FlextMeltanoConstants


class FlextDbtLdapConstants(FlextMeltanoConstants, FlextLdapConstants):
    """LDAP DBT transformation-specific constants following FLEXT unified pattern with nested domains."""

    class DbtLdap:
        """LDAP connection configuration constants."""

        class Ldap:
            """Standard LDAP connection settings."""

            DEFAULT_HOST: Final[str] = FlextConstants.DEFAULT_HOST
            DEFAULT_PORT: Final[int] = 389
            DEFAULT_TIMEOUT: Final[int] = FlextConstants.DEFAULT_TIMEOUT_SECONDS

        class Ldaps:
            """Secure LDAP connection settings."""

            DEFAULT_PORT: Final[int] = 636

    class Dbt:
        """DBT-specific configuration constants."""

        DEFAULT_PROFILES_DIR = "./profiles"
        DEFAULT_TARGET = "dev"
        ALLOWED_TARGETS: ClassVar[list[str]] = ["dev", "staging", "prod"]

    class LdapSchemaMapping:
        """LDAP t.NormalizedValue class to schema type mappings."""

        USERS_CLASSES: Final[list[str]] = ["person", "user", "inetOrgPerson"]
        GROUPS_CLASSES: Final[list[str]] = [
            "group",
            "groupOfNames",
            "groupOfUniqueNames",
        ]
        ORG_UNITS_CLASSES: Final[list[str]] = ["organizationalUnit", "organization"]

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
        USER_ID_ATTRIBUTES: Final[list[str]] = ["uid", "cn", "samaccountname"]

    class DbtModels:
        """DBT model names for LDAP transformations."""

        STG_USERS: Final[str] = "stg_users"
        DIM_USERS: Final[str] = "dim_users"
        STG_GROUPS: Final[str] = "stg_groups"
        DIM_GROUPS: Final[str] = "dim_groups"
        FACT_MEMBERSHIPS: Final[str] = "fact_memberships"

    class DbtProcessing:
        """DBT LDAP transformation configuration."""

        DEFAULT_BATCH_SIZE = FlextConstants.DEFAULT_SIZE
        MAX_BATCH_SIZE = FlextConstants.MAX_ITEMS

    class TransformationOptimization:
        """Transformation optimization performance thresholds."""

        PERFORMANCE_EXECUTION_TIME_THRESHOLD: Final[float] = 30.0
        PERFORMANCE_MEMORY_USAGE_THRESHOLD: Final[float] = 1024.0
        PERFORMANCE_ROWS_PROCESSED_THRESHOLD: Final[int] = 100000

    class DbtLogging:
        """DBT LDAP-specific logging constants."""

        DEFAULT_LEVEL: Final[str] = FlextConstants.DEFAULT_LEVEL
        AUDIT_LOG_LEVEL: Final[str] = FlextConstants.LogLevel.INFO
        LOG_DBT_OPERATIONS: Final[bool] = True
        LOG_DBT_MODELS: Final[bool] = True
        LOG_DBT_TESTS: Final[bool] = True
        LOG_DBT_SNAPSHOTS: Final[bool] = True
        LOG_DBT_SEEDS: Final[bool] = True
        LOG_DBT_MACROS: Final[bool] = True
        LOG_DBT_HOOKS: Final[bool] = True
        LOG_DBT_SOURCES: Final[bool] = True
        LOG_DBT_EXPOSURES: Final[bool] = True
        LOG_DBT_METRICS: Final[bool] = True
        LOG_DBT_EXECUTION: Final[bool] = True
        LOG_DBT_SQL: Final[bool] = False
        LOG_DBT_RESULTS: Final[bool] = True
        LOG_DBT_ERRORS: Final[bool] = True
        LOG_DBT_WARNINGS: Final[bool] = True
        LOG_DBT_PERFORMANCE: Final[bool] = True
        LOG_DBT_TIMING: Final[bool] = True
        LOG_DBT_MEMORY: Final[bool] = False
        LOG_DBT_THROUGHPUT: Final[bool] = True
        LOG_LDAP_INTEGRATION: Final[bool] = True
        LOG_LDAP_CONNECTIONS: Final[bool] = True
        LOG_LDAP_QUERIES: Final[bool] = False
        LOG_LDAP_RESULTS: Final[bool] = True
        LOG_LDAP_ERRORS: Final[bool] = True
        LOG_LDAP_PERFORMANCE: Final[bool] = True
        LOG_LDAP_TIMING: Final[bool] = True
        LOG_LDAP_MEMORY: Final[bool] = False
        LOG_LDAP_THROUGHPUT: Final[bool] = True
        LOG_TRANSFORMATION_OPERATIONS: Final[bool] = True
        LOG_TRANSFORMATION_SQL: Final[bool] = False
        LOG_TRANSFORMATION_RESULTS: Final[bool] = True
        LOG_TRANSFORMATION_ERRORS: Final[bool] = True
        LOG_TRANSFORMATION_WARNINGS: Final[bool] = True
        LOG_TRANSFORMATION_PERFORMANCE: Final[bool] = True
        LOG_TRANSFORMATION_TIMING: Final[bool] = True
        LOG_TRANSFORMATION_MEMORY: Final[bool] = False
        LOG_TRANSFORMATION_THROUGHPUT: Final[bool] = True
        LOG_DATA_QUALITY: Final[bool] = True
        LOG_DATA_QUALITY_CHECKS: Final[bool] = True
        LOG_DATA_QUALITY_ERRORS: Final[bool] = True
        LOG_DATA_QUALITY_WARNINGS: Final[bool] = True
        LOG_DATA_QUALITY_METRICS: Final[bool] = True
        LOG_DATA_QUALITY_TIMING: Final[bool] = True
        LOG_DATA_QUALITY_MEMORY: Final[bool] = False
        LOG_DATA_QUALITY_THROUGHPUT: Final[bool] = True
        LOG_SCHEMA_MAPPING: Final[bool] = True
        LOG_ATTRIBUTE_MAPPING: Final[bool] = True
        LOG_SCHEMA_VALIDATION: Final[bool] = True
        LOG_SCHEMA_ERRORS: Final[bool] = True
        LOG_SCHEMA_WARNINGS: Final[bool] = True
        LOG_SCHEMA_PERFORMANCE: Final[bool] = True
        LOG_SCHEMA_TIMING: Final[bool] = True
        LOG_SCHEMA_MEMORY: Final[bool] = False
        LOG_SCHEMA_THROUGHPUT: Final[bool] = True
        TRACK_DBT_LDAP_PERFORMANCE: Final[bool] = True
        DBT_LDAP_PERFORMANCE_THRESHOLD_WARNING: Final[float] = 1000.0
        DBT_LDAP_PERFORMANCE_THRESHOLD_CRITICAL: Final[float] = 5000.0
        INCLUDE_DBT_INFO_IN_LOGS: Final[bool] = True
        INCLUDE_LDAP_INFO_IN_LOGS: Final[bool] = True
        INCLUDE_TRANSFORMATION_INFO_IN_LOGS: Final[bool] = True
        INCLUDE_DATA_QUALITY_INFO_IN_LOGS: Final[bool] = True
        INCLUDE_SCHEMA_INFO_IN_LOGS: Final[bool] = True
        INCLUDE_TIMING_IN_LOGS: Final[bool] = True
        INCLUDE_MEMORY_IN_LOGS: Final[bool] = False
        INCLUDE_THROUGHPUT_IN_LOGS: Final[bool] = True
        MASK_SENSITIVE_DATA: Final[bool] = True
        MASK_CREDENTIALS: Final[bool] = True
        MASK_CONNECTION_STRINGS: Final[bool] = True
        MASK_API_KEYS: Final[bool] = True
        MASK_LDAP_PASSWORDS: Final[bool] = True
        MASK_LDAP_DNS: Final[bool] = False
        USE_STANDARD_TEMPLATES: Final[bool] = True
        CUSTOM_LOG_FORMAT: Final[str | None] = None
        ENABLE_AUDIT_LOGGING: Final[bool] = True
        AUDIT_LOG_FILE: Final[str] = "flext_dbt_ldap_audit.log"

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

    type LdapOperationLiteral = Literal[
        "search", "bind", "unbind", "add", "modify", "delete"
    ]
    "LDAP operation literal - matches LdapOperations StrEnum values."
    type DbtCommandLiteral = Literal["run", "test", "build", "seed", "snapshot", "docs"]
    "DBT command literal - matches DbtCommands StrEnum values."
    type DbtLogLevelLiteral = Literal["debug", "info", "warn", "error", "none"]
    "DBT log level literal - no corresponding StrEnum."
    type DbtTargetLiteral = Literal["dev", "staging", "prod"]
    "DBT target literal - no corresponding StrEnum."

    @unique
    class DbtLdapProjectType(StrEnum):
        """Project-type identifiers for dbt LDAP packages."""

        LIBRARY = "library"
        APPLICATION = "application"
        SERVICE = "service"
        DBT_LDAP = "dbt-ldap"
        LDAP_TRANSFORM = "ldap-transform"
        DIRECTORY_ANALYTICS = "directory-analytics"
        LDAP_DBT_MODELS = "ldap-dbt-models"
        DBT_LDAP_PROJECT = "dbt-ldap-project"
        LDAP_DIMENSIONAL = "ldap-dimensional"
        DIRECTORY_WAREHOUSE = "directory-warehouse"
        LDAP_ETL = "ldap-etl"
        DBT_LDAP_PIPELINE = "dbt-ldap-pipeline"
        LDAP_ANALYTICS = "ldap-analytics"
        DIRECTORY_DBT = "directory-dbt"
        LDAP_DATA_WAREHOUSE = "ldap-data-warehouse"


c = FlextDbtLdapConstants

__all__ = ["FlextDbtLdapConstants", "c"]
