"""FLEXT DBT LDAP Constants - LDAP DBT transformation constants.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from enum import StrEnum
from typing import ClassVar, Final, Literal

from flext_core import c as c_core


class FlextDbtLdapConstants(c_core):
    """LDAP DBT transformation-specific constants following FLEXT unified pattern with nested domains."""

    class DbtLdap:
        """LDAP connection configuration constants."""

        class Ldap:
            """Standard LDAP connection settings."""

            DEFAULT_HOST: Final[str] = c_core.Platform.DEFAULT_HOST
            DEFAULT_PORT: Final[int] = 389  # Standard LDAP port
            DEFAULT_TIMEOUT: Final[int] = c_core.Network.DEFAULT_TIMEOUT

        class Ldaps:
            """Secure LDAP connection settings."""

            DEFAULT_PORT: Final[int] = 636  # Standard LDAPS port

    class Dbt:
        """DBT-specific configuration constants."""

        DEFAULT_PROFILES_DIR = "./profiles"
        DEFAULT_TARGET = "dev"
        ALLOWED_TARGETS: ClassVar[list[str]] = [
            "dev",
            "staging",
            "prod",
        ]

    class DbtProcessing:
        """DBT LDAP transformation configuration."""

        DEFAULT_BATCH_SIZE = c_core.Performance.BatchProcessing.DEFAULT_SIZE
        MAX_BATCH_SIZE = c_core.Performance.BatchProcessing.MAX_ITEMS

    class TransformationOptimization:
        """Transformation optimization performance thresholds."""

        # Thresholds for performance analysis
        PERFORMANCE_EXECUTION_TIME_THRESHOLD: Final[float] = 30.0  # seconds
        PERFORMANCE_MEMORY_USAGE_THRESHOLD: Final[float] = 1024.0  # MB
        PERFORMANCE_ROWS_PROCESSED_THRESHOLD: Final[int] = 100000  # rows

    class DbtLogging:
        """DBT LDAP-specific logging constants."""

        # Default Logging Levels for DBT LDAP - use Settings.LogLevel StrEnum
        DEFAULT_LEVEL: Final[str] = c_core.Logging.DEFAULT_LEVEL
        AUDIT_LOG_LEVEL: Final[str] = c_core.Settings.LogLevel.INFO

        # DBT Operation Logging
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

        # DBT Execution Logging
        LOG_DBT_EXECUTION: Final[bool] = True
        LOG_DBT_SQL: Final[bool] = False
        LOG_DBT_RESULTS: Final[bool] = True
        LOG_DBT_ERRORS: Final[bool] = True
        LOG_DBT_WARNINGS: Final[bool] = True
        LOG_DBT_PERFORMANCE: Final[bool] = True
        LOG_DBT_TIMING: Final[bool] = True
        LOG_DBT_MEMORY: Final[bool] = False
        LOG_DBT_THROUGHPUT: Final[bool] = True

        # LDAP Integration Logging
        LOG_LDAP_INTEGRATION: Final[bool] = True
        LOG_LDAP_CONNECTIONS: Final[bool] = True
        LOG_LDAP_QUERIES: Final[bool] = False
        LOG_LDAP_RESULTS: Final[bool] = True
        LOG_LDAP_ERRORS: Final[bool] = True
        LOG_LDAP_PERFORMANCE: Final[bool] = True
        LOG_LDAP_TIMING: Final[bool] = True
        LOG_LDAP_MEMORY: Final[bool] = False
        LOG_LDAP_THROUGHPUT: Final[bool] = True

        # Data Transformation Logging
        LOG_TRANSFORMATION_OPERATIONS: Final[bool] = True
        LOG_TRANSFORMATION_SQL: Final[bool] = False
        LOG_TRANSFORMATION_RESULTS: Final[bool] = True
        LOG_TRANSFORMATION_ERRORS: Final[bool] = True
        LOG_TRANSFORMATION_WARNINGS: Final[bool] = True
        LOG_TRANSFORMATION_PERFORMANCE: Final[bool] = True
        LOG_TRANSFORMATION_TIMING: Final[bool] = True
        LOG_TRANSFORMATION_MEMORY: Final[bool] = False
        LOG_TRANSFORMATION_THROUGHPUT: Final[bool] = True

        # Data Quality Logging
        LOG_DATA_QUALITY: Final[bool] = True
        LOG_DATA_QUALITY_CHECKS: Final[bool] = True
        LOG_DATA_QUALITY_ERRORS: Final[bool] = True
        LOG_DATA_QUALITY_WARNINGS: Final[bool] = True
        LOG_DATA_QUALITY_METRICS: Final[bool] = True
        LOG_DATA_QUALITY_TIMING: Final[bool] = True
        LOG_DATA_QUALITY_MEMORY: Final[bool] = False
        LOG_DATA_QUALITY_THROUGHPUT: Final[bool] = True

        # Schema and Mapping Logging
        LOG_SCHEMA_MAPPING: Final[bool] = True
        LOG_ATTRIBUTE_MAPPING: Final[bool] = True
        LOG_SCHEMA_VALIDATION: Final[bool] = True
        LOG_SCHEMA_ERRORS: Final[bool] = True
        LOG_SCHEMA_WARNINGS: Final[bool] = True
        LOG_SCHEMA_PERFORMANCE: Final[bool] = True
        LOG_SCHEMA_TIMING: Final[bool] = True
        LOG_SCHEMA_MEMORY: Final[bool] = False
        LOG_SCHEMA_THROUGHPUT: Final[bool] = True

        # Performance Tracking for DBT LDAP Operations
        TRACK_DBT_LDAP_PERFORMANCE: Final[bool] = True
        DBT_LDAP_PERFORMANCE_THRESHOLD_WARNING: Final[float] = 1000.0  # milliseconds
        DBT_LDAP_PERFORMANCE_THRESHOLD_CRITICAL: Final[float] = 5000.0  # milliseconds

        # Context Information to Include in Logs
        INCLUDE_DBT_INFO_IN_LOGS: Final[bool] = True
        INCLUDE_LDAP_INFO_IN_LOGS: Final[bool] = True
        INCLUDE_TRANSFORMATION_INFO_IN_LOGS: Final[bool] = True
        INCLUDE_DATA_QUALITY_INFO_IN_LOGS: Final[bool] = True
        INCLUDE_SCHEMA_INFO_IN_LOGS: Final[bool] = True
        INCLUDE_TIMING_IN_LOGS: Final[bool] = True
        INCLUDE_MEMORY_IN_LOGS: Final[bool] = False
        INCLUDE_THROUGHPUT_IN_LOGS: Final[bool] = True

        # Security and Privacy Settings
        MASK_SENSITIVE_DATA: Final[bool] = True
        MASK_CREDENTIALS: Final[bool] = True
        MASK_CONNECTION_STRINGS: Final[bool] = True
        MASK_API_KEYS: Final[bool] = True
        MASK_LDAP_PASSWORDS: Final[bool] = True
        MASK_LDAP_DNS: Final[bool] = False

        # Log Message Templates
        USE_STANDARD_TEMPLATES: Final[bool] = True
        CUSTOM_LOG_FORMAT: Final[str | None] = None

        # Audit Logging
        ENABLE_AUDIT_LOGGING: Final[bool] = True
        AUDIT_LOG_FILE: Final[str] = "flext_dbt_ldap_audit.log"

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

    # ═══════════════════════════════════════════════════════════════════
    # LITERAL TYPES: PEP 695 strict type aliases (Python 3.13+)
    # ═══════════════════════════════════════════════════════════════════
    # Literal types use string values matching corresponding StrEnum values

    type LdapOperationLiteral = Literal[
        "search",
        "bind",
        "unbind",
        "add",
        "modify",
        "delete",
    ]
    """LDAP operation literal - matches LdapOperations StrEnum values."""

    type DbtCommandLiteral = Literal[
        "run",
        "test",
        "build",
        "seed",
        "snapshot",
        "docs",
    ]
    """DBT command literal - matches DbtCommands StrEnum values."""

    # DBT log level literal - matches DBT log levels (no corresponding StrEnum)
    type DbtLogLevelLiteral = Literal["debug", "info", "warn", "error", "none"]
    """DBT log level literal - no corresponding StrEnum."""

    # DBT target literal - matches Dbt.ALLOWED_TARGETS (no corresponding StrEnum)
    type DbtTargetLiteral = Literal["dev", "staging", "prod"]
    """DBT target literal - no corresponding StrEnum."""


c = FlextDbtLdapConstants

__all__ = ["FlextDbtLdapConstants", "c"]
