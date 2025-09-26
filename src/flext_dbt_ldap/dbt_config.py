"""FLEXT DBT LDAP Configuration.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import threading
from pathlib import Path
from typing import ClassVar, Final

from flext_meltano.config import FlextMeltanoConfig
from pydantic import Field, SecretStr, field_validator, model_validator

from flext_core import FlextConfig, FlextConstants, FlextLogger, FlextTypes
from flext_dbt_ldap.typings import FlextDbtLdapTypes
from flext_ldap import FlextLdapModels

logger = FlextLogger(__name__)


class FlextDbtLdapLoggingConstants(FlextConstants):
    """DBT LDAP-specific logging constants for FLEXT DBT LDAP module.

    Provides domain-specific logging defaults, levels, and configuration
    options tailored for DBT LDAP operations, data transformation, and
    LDAP integration processes.
    """

    # Default Logging Levels for DBT LDAP
    DEFAULT_LEVEL: Final[str] = FlextConstants.Logging.DEFAULT_LEVEL
    AUDIT_LOG_LEVEL: Final[str] = FlextConstants.Logging.INFO

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

    # Environment-specific overrides for DBT LDAP logging
    class EnvironmentOverrides:
        """Environment-specific DBT LDAP logging configuration."""

        DEVELOPMENT: ClassVar[FlextTypes.Core.Dict] = {
            "log_dbt_sql": "True",  # Log SQL in dev
            "log_ldap_queries": "True",  # Log LDAP queries in dev
            "log_transformation_sql": "True",  # Log transformation SQL in dev
            "audit_log_level": FlextConstants.Config.LogLevel.DEBUG,
        }

        STAGING: ClassVar[FlextTypes.Core.Dict] = {
            "log_dbt_sql": "False",
            "log_ldap_queries": "False",
            "log_transformation_sql": "False",
            "audit_log_level": FlextConstants.Config.LogLevel.INFO,
        }

        PRODUCTION: ClassVar[FlextTypes.Core.Dict] = {
            "log_dbt_sql": "False",
            "log_ldap_queries": "False",
            "log_transformation_sql": "False",
            "audit_log_level": FlextConstants.Config.LogLevel.WARNING,
        }

        TESTING: ClassVar[FlextTypes.Core.Dict] = {
            "log_dbt_sql": "True",  # Log SQL in testing
            "log_ldap_queries": "True",  # Log LDAP queries in testing
            "log_transformation_sql": "True",  # Log transformation SQL in testing
            "audit_log_level": FlextConstants.Config.LogLevel.DEBUG,
        }


class FlextDbtLdapConfig(FlextConfig):
    """Single Pydantic 2 Settings class for flext-dbt-ldap extending FlextConfig.

    Follows standardized pattern:
    - Extends FlextConfig from flext-core
    - No nested classes within Config
    - All defaults from FlextDbtLdapConstants
    - Dependency injection integration with flext-core container
    - Uses Pydantic 2.11+ features (SecretStr for secrets)
    """

    # Singleton pattern attributes
    _global_instance: ClassVar[FlextDbtLdapConfig | None] = None
    _lock: ClassVar[threading.Lock] = threading.Lock()

    # LDAP Connection Settings (from flext-ldap) using Field and proper defaults
    ldap_host: str = Field(default="localhost", description="LDAP server hostname")
    ldap_port: int = Field(default=389, ge=1, le=65535, description="LDAP server port")
    ldap_use_tls: bool = Field(
        default=False, description="Use TLS for LDAP connections"
    )
    ldap_bind_dn: SecretStr | None = Field(
        default=None,
        description="LDAP bind distinguished name for authentication (sensitive)",
    )
    ldap_bind_password: SecretStr | None = Field(
        default=None, description="LDAP bind password for authentication (sensitive)"
    )
    ldap_base_dn: str = Field(
        default="", description="LDAP base distinguished name for searches"
    )

    # DBT Execution Settings (from flext-meltano) using Field
    dbt_project_dir: str = Field(default=".", description="DBT project directory path")
    dbt_profiles_dir: str = Field(
        default=".", description="DBT profiles directory path"
    )
    dbt_target: str = Field(default="dev", description="DBT target environment")
    dbt_threads: int = Field(
        default=1, ge=1, le=16, description="Number of DBT threads"
    )
    dbt_log_level: str = Field(default="info", description="DBT log level")

    # LDAP-specific DBT Settings - using constants
    ldap_schema_mapping: ClassVar[FlextTypes.Core.Headers] = {
        "users": "stg_users",
        "groups": "stg_groups",
        "org_units": "stg_org_units",
    }

    ldap_attribute_mapping: ClassVar[FlextTypes.Core.Headers] = {
        "cn": "common_name",
        "uid": "user_id",
        "mail": "email",
        "memberOf": "member_of",
    }

    # Data Quality Settings
    min_quality_threshold: float = Field(
        default=0.8, ge=0.0, le=1.0, description="Minimum data quality threshold"
    )
    required_attributes: ClassVar[FlextDbtLdapTypes.Core.StringList] = [
        "cn",
        "objectClass",
    ]
    validate_dns: bool = Field(
        default=True, description="Validate LDAP distinguished names"
    )

    # DBT LDAP-specific logging configuration using FlextDbtLdapLoggingConstants
    log_dbt_operations: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_DBT_OPERATIONS,
        description="Log DBT operations",
    )

    log_dbt_models: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_DBT_MODELS,
        description="Log DBT model execution",
    )

    log_dbt_tests: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_DBT_TESTS,
        description="Log DBT test execution",
    )

    log_dbt_snapshots: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_DBT_SNAPSHOTS,
        description="Log DBT snapshot operations",
    )

    log_dbt_seeds: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_DBT_SEEDS,
        description="Log DBT seed operations",
    )

    log_dbt_macros: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_DBT_MACROS,
        description="Log DBT macro execution",
    )

    log_dbt_hooks: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_DBT_HOOKS,
        description="Log DBT hook execution",
    )

    log_dbt_sources: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_DBT_SOURCES,
        description="Log DBT source operations",
    )

    log_dbt_exposures: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_DBT_EXPOSURES,
        description="Log DBT exposure operations",
    )

    log_dbt_metrics: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_DBT_METRICS,
        description="Log DBT metric operations",
    )

    # DBT Execution Logging
    log_dbt_execution: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_DBT_EXECUTION,
        description="Log DBT execution details",
    )

    log_dbt_sql: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_DBT_SQL,
        description="Log DBT SQL queries",
    )

    log_dbt_results: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_DBT_RESULTS,
        description="Log DBT execution results",
    )

    log_dbt_errors: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_DBT_ERRORS,
        description="Log DBT errors",
    )

    log_dbt_warnings: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_DBT_WARNINGS,
        description="Log DBT warnings",
    )

    log_dbt_performance: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_DBT_PERFORMANCE,
        description="Log DBT performance metrics",
    )

    log_dbt_timing: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_DBT_TIMING,
        description="Log DBT timing information",
    )

    log_dbt_memory: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_DBT_MEMORY,
        description="Log DBT memory usage",
    )

    log_dbt_throughput: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_DBT_THROUGHPUT,
        description="Log DBT throughput metrics",
    )

    # LDAP Integration Logging
    log_ldap_integration: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_LDAP_INTEGRATION,
        description="Log LDAP integration operations",
    )

    log_ldap_connections: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_LDAP_CONNECTIONS,
        description="Log LDAP connection events",
    )

    log_ldap_queries: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_LDAP_QUERIES,
        description="Log LDAP queries",
    )

    log_ldap_results: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_LDAP_RESULTS,
        description="Log LDAP query results",
    )

    log_ldap_errors: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_LDAP_ERRORS,
        description="Log LDAP errors",
    )

    log_ldap_performance: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_LDAP_PERFORMANCE,
        description="Log LDAP performance metrics",
    )

    log_ldap_timing: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_LDAP_TIMING,
        description="Log LDAP timing information",
    )

    log_ldap_memory: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_LDAP_MEMORY,
        description="Log LDAP memory usage",
    )

    log_ldap_throughput: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_LDAP_THROUGHPUT,
        description="Log LDAP throughput metrics",
    )

    # Data Transformation Logging
    log_transformation_operations: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_TRANSFORMATION_OPERATIONS,
        description="Log data transformation operations",
    )

    log_transformation_sql: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_TRANSFORMATION_SQL,
        description="Log transformation SQL queries",
    )

    log_transformation_results: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_TRANSFORMATION_RESULTS,
        description="Log transformation results",
    )

    log_transformation_errors: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_TRANSFORMATION_ERRORS,
        description="Log transformation errors",
    )

    log_transformation_warnings: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_TRANSFORMATION_WARNINGS,
        description="Log transformation warnings",
    )

    log_transformation_performance: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_TRANSFORMATION_PERFORMANCE,
        description="Log transformation performance metrics",
    )

    log_transformation_timing: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_TRANSFORMATION_TIMING,
        description="Log transformation timing information",
    )

    log_transformation_memory: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_TRANSFORMATION_MEMORY,
        description="Log transformation memory usage",
    )

    log_transformation_throughput: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_TRANSFORMATION_THROUGHPUT,
        description="Log transformation throughput metrics",
    )

    # Data Quality Logging
    log_data_quality: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_DATA_QUALITY,
        description="Log data quality checks",
    )

    log_data_quality_checks: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_DATA_QUALITY_CHECKS,
        description="Log data quality check results",
    )

    log_data_quality_errors: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_DATA_QUALITY_ERRORS,
        description="Log data quality errors",
    )

    log_data_quality_warnings: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_DATA_QUALITY_WARNINGS,
        description="Log data quality warnings",
    )

    log_data_quality_metrics: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_DATA_QUALITY_METRICS,
        description="Log data quality metrics",
    )

    log_data_quality_timing: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_DATA_QUALITY_TIMING,
        description="Log data quality timing information",
    )

    log_data_quality_memory: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_DATA_QUALITY_MEMORY,
        description="Log data quality memory usage",
    )

    log_data_quality_throughput: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_DATA_QUALITY_THROUGHPUT,
        description="Log data quality throughput metrics",
    )

    # Schema and Mapping Logging
    log_schema_mapping: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_SCHEMA_MAPPING,
        description="Log schema mapping operations",
    )

    log_attribute_mapping: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_ATTRIBUTE_MAPPING,
        description="Log attribute mapping operations",
    )

    log_schema_validation: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_SCHEMA_VALIDATION,
        description="Log schema validation operations",
    )

    log_schema_errors: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_SCHEMA_ERRORS,
        description="Log schema errors",
    )

    log_schema_warnings: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_SCHEMA_WARNINGS,
        description="Log schema warnings",
    )

    log_schema_performance: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_SCHEMA_PERFORMANCE,
        description="Log schema performance metrics",
    )

    log_schema_timing: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_SCHEMA_TIMING,
        description="Log schema timing information",
    )

    log_schema_memory: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_SCHEMA_MEMORY,
        description="Log schema memory usage",
    )

    log_schema_throughput: bool = Field(
        default=FlextDbtLdapLoggingConstants.LOG_SCHEMA_THROUGHPUT,
        description="Log schema throughput metrics",
    )

    # Performance Tracking for DBT LDAP Operations
    track_dbt_ldap_performance: bool = Field(
        default=FlextDbtLdapLoggingConstants.TRACK_DBT_LDAP_PERFORMANCE,
        description="Track DBT LDAP performance metrics",
    )

    dbt_ldap_performance_threshold_warning: float = Field(
        default=FlextDbtLdapLoggingConstants.DBT_LDAP_PERFORMANCE_THRESHOLD_WARNING,
        ge=0.0,
        description="DBT LDAP performance warning threshold in milliseconds",
    )

    dbt_ldap_performance_threshold_critical: float = Field(
        default=FlextDbtLdapLoggingConstants.DBT_LDAP_PERFORMANCE_THRESHOLD_CRITICAL,
        ge=0.0,
        description="DBT LDAP performance critical threshold in milliseconds",
    )

    # Context Information to Include in Logs
    include_dbt_info_in_logs: bool = Field(
        default=FlextDbtLdapLoggingConstants.INCLUDE_DBT_INFO_IN_LOGS,
        description="Include DBT information in log messages",
    )

    include_ldap_info_in_logs: bool = Field(
        default=FlextDbtLdapLoggingConstants.INCLUDE_LDAP_INFO_IN_LOGS,
        description="Include LDAP information in log messages",
    )

    include_transformation_info_in_logs: bool = Field(
        default=FlextDbtLdapLoggingConstants.INCLUDE_TRANSFORMATION_INFO_IN_LOGS,
        description="Include transformation information in log messages",
    )

    include_data_quality_info_in_logs: bool = Field(
        default=FlextDbtLdapLoggingConstants.INCLUDE_DATA_QUALITY_INFO_IN_LOGS,
        description="Include data quality information in log messages",
    )

    include_schema_info_in_logs: bool = Field(
        default=FlextDbtLdapLoggingConstants.INCLUDE_SCHEMA_INFO_IN_LOGS,
        description="Include schema information in log messages",
    )

    include_timing_in_logs: bool = Field(
        default=FlextDbtLdapLoggingConstants.INCLUDE_TIMING_IN_LOGS,
        description="Include timing information in log messages",
    )

    include_memory_in_logs: bool = Field(
        default=FlextDbtLdapLoggingConstants.INCLUDE_MEMORY_IN_LOGS,
        description="Include memory information in log messages",
    )

    include_throughput_in_logs: bool = Field(
        default=FlextDbtLdapLoggingConstants.INCLUDE_THROUGHPUT_IN_LOGS,
        description="Include throughput information in log messages",
    )

    # Security and Privacy Settings
    mask_sensitive_data: bool = Field(
        default=FlextDbtLdapLoggingConstants.MASK_SENSITIVE_DATA,
        description="Mask sensitive data in logs",
    )

    mask_credentials: bool = Field(
        default=FlextDbtLdapLoggingConstants.MASK_CREDENTIALS,
        description="Mask credentials in logs",
    )

    mask_connection_strings: bool = Field(
        default=FlextDbtLdapLoggingConstants.MASK_CONNECTION_STRINGS,
        description="Mask connection strings in logs",
    )

    mask_api_keys: bool = Field(
        default=FlextDbtLdapLoggingConstants.MASK_API_KEYS,
        description="Mask API keys in logs",
    )

    mask_ldap_passwords: bool = Field(
        default=FlextDbtLdapLoggingConstants.MASK_LDAP_PASSWORDS,
        description="Mask LDAP passwords in logs",
    )

    mask_ldap_dns: bool = Field(
        default=FlextDbtLdapLoggingConstants.MASK_LDAP_DNS,
        description="Mask LDAP DNs in logs",
    )

    # Log Message Templates
    use_standard_templates: bool = Field(
        default=FlextDbtLdapLoggingConstants.USE_STANDARD_TEMPLATES,
        description="Use standard log message templates",
    )

    custom_log_format: str | None = Field(
        default=FlextDbtLdapLoggingConstants.CUSTOM_LOG_FORMAT,
        description="Custom log message format",
    )

    # Audit Logging
    enable_audit_logging: bool = Field(
        default=FlextDbtLdapLoggingConstants.ENABLE_AUDIT_LOGGING,
        description="Enable audit logging",
    )

    audit_log_file: str = Field(
        default=FlextDbtLdapLoggingConstants.AUDIT_LOG_FILE,
        description="Audit log file path",
    )

    # Pydantic 2.11 field validators
    @field_validator("dbt_target")
    @classmethod
    def validate_dbt_target(cls, v: str) -> str:
        """Validate DBT target environment."""
        valid_targets = {
            "dev",
            "development",
            "staging",
            "prod",
            "production",
            "test",
            "local",
        }
        if v not in valid_targets:
            valid_targets_str = ", ".join(sorted(valid_targets))
            msg = f"Invalid DBT target: {v}. Must be one of: {valid_targets_str}"
            raise ValueError(msg)
        return v

    @field_validator("dbt_log_level")
    @classmethod
    def validate_dbt_log_level(cls, v: str) -> str:
        """Validate DBT log level."""
        valid_levels = {"debug", "info", "warn", "error", "none"}
        if v.lower() not in valid_levels:
            valid_levels_str = ", ".join(sorted(valid_levels))
            msg = f"Invalid DBT log level: {v}. Must be one of: {valid_levels_str}"
            raise ValueError(msg)
        return v.lower()

    @field_validator("ldap_bind_dn")
    @classmethod
    def validate_ldap_bind_dn(cls, v: SecretStr | None) -> SecretStr | None:
        """Validate LDAP bind DN format."""
        if v is None:
            return v

        dn_value = v.get_secret_value()
        if not dn_value or not dn_value.strip():
            return None

        if "=" not in dn_value:
            msg = "Invalid LDAP bind DN format: must contain attribute=value pairs"
            raise ValueError(msg)

        return v

    @model_validator(mode="after")
    def validate_ldap_configuration_consistency(self) -> FlextDbtLdapConfig:
        """Validate LDAP configuration consistency."""
        # Validate authentication configuration
        if self.ldap_bind_dn is not None and self.ldap_bind_password is None:
            msg = "Bind password is required when bind DN is specified"
            raise ValueError(msg)

        # Validate performance thresholds
        if (
            self.dbt_ldap_performance_threshold_warning
            > self.dbt_ldap_performance_threshold_critical
        ):
            msg = "Warning threshold cannot be greater than critical threshold"
            raise ValueError(msg)

        return self

    def get_ldap_config(self) -> FlextLdapModels.ConnectionConfig:
        """Get LDAP configuration for flext-ldap integration."""
        bind_dn = self.ldap_bind_dn.get_secret_value() if self.ldap_bind_dn else ""
        bind_password = (
            self.ldap_bind_password.get_secret_value()
            if self.ldap_bind_password
            else ""
        )

        return FlextLdapModels.ConnectionConfig(
            server=self.ldap_host,
            port=self.ldap_port,
            bind_dn=bind_dn,
            bind_password=bind_password,
        )

    def get_meltano_config(self) -> FlextMeltanoConfig:
        """Get Meltano configuration for flext-meltano integration."""
        # Convert string to proper Environment string value
        environment_mapping: dict[str, FlextTypes.Config.Environment] = {
            "dev": "development",
            "development": "development",
            "staging": "staging",
            "prod": "production",
            "production": "production",
            "test": "test",
            "local": "local",
        }

        environment_value = environment_mapping.get(
            self.dbt_target.lower(),
            "development",
        )

        return FlextMeltanoConfig(
            project_root=Path(self.dbt_project_dir),
            environment=environment_value,
        )

    def get_ldap_quality_config(self) -> FlextTypes.Core.Dict:
        """Get data quality configuration for LDAP validation."""
        return {
            "min_quality_threshold": self.min_quality_threshold,
            "required_attributes": self.required_attributes,
            "validate_dns": self.validate_dns,
        }

    def get_dbt_ldap_logging_config(self) -> FlextTypes.Core.Dict:
        """Get DBT LDAP-specific logging configuration dictionary."""
        return {
            "log_dbt_operations": self.log_dbt_operations,
            "log_dbt_models": self.log_dbt_models,
            "log_dbt_tests": self.log_dbt_tests,
            "log_dbt_snapshots": self.log_dbt_snapshots,
            "log_dbt_seeds": self.log_dbt_seeds,
            "log_dbt_macros": self.log_dbt_macros,
            "log_dbt_hooks": self.log_dbt_hooks,
            "log_dbt_sources": self.log_dbt_sources,
            "log_dbt_exposures": self.log_dbt_exposures,
            "log_dbt_metrics": self.log_dbt_metrics,
            "log_dbt_execution": self.log_dbt_execution,
            "log_dbt_sql": self.log_dbt_sql,
            "log_dbt_results": self.log_dbt_results,
            "log_dbt_errors": self.log_dbt_errors,
            "log_dbt_warnings": self.log_dbt_warnings,
            "log_dbt_performance": self.log_dbt_performance,
            "log_dbt_timing": self.log_dbt_timing,
            "log_dbt_memory": self.log_dbt_memory,
            "log_dbt_throughput": self.log_dbt_throughput,
            "log_ldap_integration": self.log_ldap_integration,
            "log_ldap_connections": self.log_ldap_connections,
            "log_ldap_queries": self.log_ldap_queries,
            "log_ldap_results": self.log_ldap_results,
            "log_ldap_errors": self.log_ldap_errors,
            "log_ldap_performance": self.log_ldap_performance,
            "log_ldap_timing": self.log_ldap_timing,
            "log_ldap_memory": self.log_ldap_memory,
            "log_ldap_throughput": self.log_ldap_throughput,
            "log_transformation_operations": self.log_transformation_operations,
            "log_transformation_sql": self.log_transformation_sql,
            "log_transformation_results": self.log_transformation_results,
            "log_transformation_errors": self.log_transformation_errors,
            "log_transformation_warnings": self.log_transformation_warnings,
            "log_transformation_performance": self.log_transformation_performance,
            "log_transformation_timing": self.log_transformation_timing,
            "log_transformation_memory": self.log_transformation_memory,
            "log_transformation_throughput": self.log_transformation_throughput,
            "log_data_quality": self.log_data_quality,
            "log_data_quality_checks": self.log_data_quality_checks,
            "log_data_quality_errors": self.log_data_quality_errors,
            "log_data_quality_warnings": self.log_data_quality_warnings,
            "log_data_quality_metrics": self.log_data_quality_metrics,
            "log_data_quality_timing": self.log_data_quality_timing,
            "log_data_quality_memory": self.log_data_quality_memory,
            "log_data_quality_throughput": self.log_data_quality_throughput,
            "log_schema_mapping": self.log_schema_mapping,
            "log_attribute_mapping": self.log_attribute_mapping,
            "log_schema_validation": self.log_schema_validation,
            "log_schema_errors": self.log_schema_errors,
            "log_schema_warnings": self.log_schema_warnings,
            "log_schema_performance": self.log_schema_performance,
            "log_schema_timing": self.log_schema_timing,
            "log_schema_memory": self.log_schema_memory,
            "log_schema_throughput": self.log_schema_throughput,
            "track_dbt_ldap_performance": self.track_dbt_ldap_performance,
            "dbt_ldap_performance_threshold_warning": self.dbt_ldap_performance_threshold_warning,
            "dbt_ldap_performance_threshold_critical": self.dbt_ldap_performance_threshold_critical,
            "include_dbt_info_in_logs": self.include_dbt_info_in_logs,
            "include_ldap_info_in_logs": self.include_ldap_info_in_logs,
            "include_transformation_info_in_logs": self.include_transformation_info_in_logs,
            "include_data_quality_info_in_logs": self.include_data_quality_info_in_logs,
            "include_schema_info_in_logs": self.include_schema_info_in_logs,
            "include_timing_in_logs": self.include_timing_in_logs,
            "include_memory_in_logs": self.include_memory_in_logs,
            "include_throughput_in_logs": self.include_throughput_in_logs,
            "mask_sensitive_data": self.mask_sensitive_data,
            "mask_credentials": self.mask_credentials,
            "mask_connection_strings": self.mask_connection_strings,
            "mask_api_keys": self.mask_api_keys,
            "mask_ldap_passwords": self.mask_ldap_passwords,
            "mask_ldap_dns": self.mask_ldap_dns,
            "use_standard_templates": self.use_standard_templates,
            "custom_log_format": self.custom_log_format,
            "enable_audit_logging": self.enable_audit_logging,
            "audit_log_file": self.audit_log_file,
        }

    @classmethod
    def create_for_environment(
        cls, environment: str, **overrides: object
    ) -> FlextDbtLdapConfig:
        """Create configuration for specific environment."""
        return cls(environment=environment, **overrides)

    @classmethod
    def create_default(cls) -> FlextDbtLdapConfig:
        """Create default configuration instance."""
        return cls()

    # Singleton pattern override for proper typing
    @classmethod
    def get_global_instance(cls) -> FlextDbtLdapConfig:
        """Get the global singleton instance of FlextDbtLdapConfig."""
        if cls._global_instance is None:
            with cls._lock:
                if cls._global_instance is None:
                    cls._global_instance = cls()
        return cls._global_instance

    @classmethod
    def reset_global_instance(cls) -> None:
        """Reset the global FlextDbtLdapConfig instance (mainly for testing)."""
        cls._global_instance = None


__all__: FlextDbtLdapTypes.Core.StringList = [
    "FlextDbtLdapConfig",
]
