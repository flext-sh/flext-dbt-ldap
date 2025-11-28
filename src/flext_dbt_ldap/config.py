"""FLEXT DBT LDAP Configuration.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from pathlib import Path
from typing import ClassVar, Self, cast

from flext_core import FlextConfig, FlextLogger, FlextResult
from flext_ldap import FlextLdapModels
from flext_meltano import FlextMeltanoConfig
from pydantic import Field, SecretStr, field_validator, model_validator
from pydantic_settings import SettingsConfigDict

from flext_dbt_ldap.constants import FlextDbtLdapConstants
from flext_dbt_ldap.typings import FlextDbtLdapTypes

logger = FlextLogger(__name__)


class FlextDbtLdapConfig(FlextConfig):
    """Single Pydantic 2 Settings class for flext-dbt-ldap extending FlextConfig.

    Follows standardized pattern:
    - Extends FlextConfig from flext-core
    - No nested classes within Config
    - All defaults from FlextDbtLdapConstants
    - Uses enhanced singleton pattern with inverse dependency injection
    - Uses Pydantic 2.11+ features (field_validator, model_validator)
    """

    model_config = SettingsConfigDict(
        env_prefix="FLEXT_DBT_LDAP_",
        case_sensitive=False,
        extra="allow",
        validate_assignment=True,
        str_strip_whitespace=True,
        json_schema_extra={
            "title": "FLEXT DBT LDAP Configuration",
            "description": "DBT LDAP configuration extending FlextConfig",
        },
    )

    # LDAP Connection Settings (from flext-ldap) using Field and proper defaults
    ldap_host: str = Field(
        default=FlextDbtLdapConstants.Connection.Ldap.DEFAULT_HOST,
        description="LDAP server hostname",
    )
    ldap_port: int = Field(
        default=FlextDbtLdapConstants.Connection.Ldap.DEFAULT_PORT,
        ge=1,
        le=65535,
        description="LDAP server port",
    )
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
        default=FlextDbtLdapConstants.DbtProcessing.DEFAULT_BATCH_SIZE // 1000,
        ge=1,
        le=16,
        description="Number of DBT threads",
    )
    dbt_log_level: FlextDbtLdapConstants.Literals.DbtLogLevelLiteral = Field(
        default="info", description="DBT log level"
    )

    # LDAP-specific DBT Settings - using constants
    ldap_schema_mapping: ClassVar[dict[str, str]] = {
        "users": "stg_users",
        "groups": "stg_groups",
        "org_units": "stg_org_units",
    }

    ldap_attribute_mapping: ClassVar[dict[str, str]] = {
        "cn": "common_name",
        "uid": "user_id",
        "mail": "email",
        "memberOf": "member_of",
    }

    # Data Quality Settings
    min_quality_threshold: float = Field(
        default=0.8, ge=0.0, le=1.0, description="Minimum data quality threshold"
    )
    required_attributes: ClassVar[FlextDbtLdapTypes.DbtLdapCore.StringList] = [
        "cn",
        "objectClass",
    ]
    validate_dns: bool = Field(
        default=True, description="Validate LDAP distinguished names"
    )

    # DBT LDAP-specific logging configuration using FlextDbtLdapLoggingConstants
    log_dbt_operations: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_DBT_OPERATIONS,
        description="Log DBT operations",
    )

    log_dbt_models: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_DBT_MODELS,
        description="Log DBT model execution",
    )

    log_dbt_tests: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_DBT_TESTS,
        description="Log DBT test execution",
    )

    log_dbt_snapshots: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_DBT_SNAPSHOTS,
        description="Log DBT snapshot operations",
    )

    log_dbt_seeds: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_DBT_SEEDS,
        description="Log DBT seed operations",
    )

    log_dbt_macros: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_DBT_MACROS,
        description="Log DBT macro execution",
    )

    log_dbt_hooks: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_DBT_HOOKS,
        description="Log DBT hook execution",
    )

    log_dbt_sources: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_DBT_SOURCES,
        description="Log DBT source operations",
    )

    log_dbt_exposures: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_DBT_EXPOSURES,
        description="Log DBT exposure operations",
    )

    log_dbt_metrics: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_DBT_METRICS,
        description="Log DBT metric operations",
    )

    # DBT Execution Logging
    log_dbt_execution: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_DBT_EXECUTION,
        description="Log DBT execution details",
    )

    log_dbt_sql: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_DBT_SQL,
        description="Log DBT SQL queries",
    )

    log_dbt_results: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_DBT_RESULTS,
        description="Log DBT execution results",
    )

    log_dbt_errors: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_DBT_ERRORS,
        description="Log DBT errors",
    )

    log_dbt_warnings: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_DBT_WARNINGS,
        description="Log DBT warnings",
    )

    log_dbt_performance: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_DBT_PERFORMANCE,
        description="Log DBT performance metrics",
    )

    log_dbt_timing: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_DBT_TIMING,
        description="Log DBT timing information",
    )

    log_dbt_memory: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_DBT_MEMORY,
        description="Log DBT memory usage",
    )

    log_dbt_throughput: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_DBT_THROUGHPUT,
        description="Log DBT throughput metrics",
    )

    # LDAP Integration Logging
    log_ldap_integration: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_LDAP_INTEGRATION,
        description="Log LDAP integration operations",
    )

    log_ldap_connections: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_LDAP_CONNECTIONS,
        description="Log LDAP connection events",
    )

    log_ldap_queries: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_LDAP_QUERIES,
        description="Log LDAP queries",
    )

    log_ldap_results: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_LDAP_RESULTS,
        description="Log LDAP query results",
    )

    log_ldap_errors: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_LDAP_ERRORS,
        description="Log LDAP errors",
    )

    log_ldap_performance: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_LDAP_PERFORMANCE,
        description="Log LDAP performance metrics",
    )

    log_ldap_timing: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_LDAP_TIMING,
        description="Log LDAP timing information",
    )

    log_ldap_memory: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_LDAP_MEMORY,
        description="Log LDAP memory usage",
    )

    log_ldap_throughput: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_LDAP_THROUGHPUT,
        description="Log LDAP throughput metrics",
    )

    # Data Transformation Logging
    log_transformation_operations: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_TRANSFORMATION_OPERATIONS,
        description="Log data transformation operations",
    )

    log_transformation_sql: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_TRANSFORMATION_SQL,
        description="Log transformation SQL queries",
    )

    log_transformation_results: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_TRANSFORMATION_RESULTS,
        description="Log transformation results",
    )

    log_transformation_errors: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_TRANSFORMATION_ERRORS,
        description="Log transformation errors",
    )

    log_transformation_warnings: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_TRANSFORMATION_WARNINGS,
        description="Log transformation warnings",
    )

    log_transformation_performance: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_TRANSFORMATION_PERFORMANCE,
        description="Log transformation performance metrics",
    )

    log_transformation_timing: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_TRANSFORMATION_TIMING,
        description="Log transformation timing information",
    )

    log_transformation_memory: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_TRANSFORMATION_MEMORY,
        description="Log transformation memory usage",
    )

    log_transformation_throughput: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_TRANSFORMATION_THROUGHPUT,
        description="Log transformation throughput metrics",
    )

    # Data Quality Logging
    log_data_quality: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_DATA_QUALITY,
        description="Log data quality checks",
    )

    log_data_quality_checks: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_DATA_QUALITY_CHECKS,
        description="Log data quality check results",
    )

    log_data_quality_errors: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_DATA_QUALITY_ERRORS,
        description="Log data quality errors",
    )

    log_data_quality_warnings: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_DATA_QUALITY_WARNINGS,
        description="Log data quality warnings",
    )

    log_data_quality_metrics: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_DATA_QUALITY_METRICS,
        description="Log data quality metrics",
    )

    log_data_quality_timing: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_DATA_QUALITY_TIMING,
        description="Log data quality timing information",
    )

    log_data_quality_memory: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_DATA_QUALITY_MEMORY,
        description="Log data quality memory usage",
    )

    log_data_quality_throughput: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_DATA_QUALITY_THROUGHPUT,
        description="Log data quality throughput metrics",
    )

    # Schema and Mapping Logging
    log_schema_mapping: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_SCHEMA_MAPPING,
        description="Log schema mapping operations",
    )

    log_attribute_mapping: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_ATTRIBUTE_MAPPING,
        description="Log attribute mapping operations",
    )

    log_schema_validation: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_SCHEMA_VALIDATION,
        description="Log schema validation operations",
    )

    log_schema_errors: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_SCHEMA_ERRORS,
        description="Log schema errors",
    )

    log_schema_warnings: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_SCHEMA_WARNINGS,
        description="Log schema warnings",
    )

    log_schema_performance: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_SCHEMA_PERFORMANCE,
        description="Log schema performance metrics",
    )

    log_schema_timing: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_SCHEMA_TIMING,
        description="Log schema timing information",
    )

    log_schema_memory: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_SCHEMA_MEMORY,
        description="Log schema memory usage",
    )

    log_schema_throughput: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.LOG_SCHEMA_THROUGHPUT,
        description="Log schema throughput metrics",
    )

    # Performance Tracking for DBT LDAP Operations
    track_dbt_ldap_performance: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.TRACK_DBT_LDAP_PERFORMANCE,
        description="Track DBT LDAP performance metrics",
    )

    dbt_ldap_performance_threshold_warning: float = Field(
        default=FlextDbtLdapConstants.DbtLogging.DBT_LDAP_PERFORMANCE_THRESHOLD_WARNING,
        ge=0.0,
        description="DBT LDAP performance warning threshold in milliseconds",
    )

    dbt_ldap_performance_threshold_critical: float = Field(
        default=FlextDbtLdapConstants.DbtLogging.DBT_LDAP_PERFORMANCE_THRESHOLD_CRITICAL,
        ge=0.0,
        description="DBT LDAP performance critical threshold in milliseconds",
    )

    # Context Information to Include in Logs
    include_dbt_info_in_logs: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.INCLUDE_DBT_INFO_IN_LOGS,
        description="Include DBT information in log messages",
    )

    include_ldap_info_in_logs: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.INCLUDE_LDAP_INFO_IN_LOGS,
        description="Include LDAP information in log messages",
    )

    include_transformation_info_in_logs: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.INCLUDE_TRANSFORMATION_INFO_IN_LOGS,
        description="Include transformation information in log messages",
    )

    include_data_quality_info_in_logs: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.INCLUDE_DATA_QUALITY_INFO_IN_LOGS,
        description="Include data quality information in log messages",
    )

    include_schema_info_in_logs: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.INCLUDE_SCHEMA_INFO_IN_LOGS,
        description="Include schema information in log messages",
    )

    include_timing_in_logs: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.INCLUDE_TIMING_IN_LOGS,
        description="Include timing information in log messages",
    )

    include_memory_in_logs: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.INCLUDE_MEMORY_IN_LOGS,
        description="Include memory information in log messages",
    )

    include_throughput_in_logs: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.INCLUDE_THROUGHPUT_IN_LOGS,
        description="Include throughput information in log messages",
    )

    # Security and Privacy Settings
    mask_sensitive_data: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.MASK_SENSITIVE_DATA,
        description="Mask sensitive data in logs",
    )

    mask_credentials: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.MASK_CREDENTIALS,
        description="Mask credentials in logs",
    )

    mask_connection_strings: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.MASK_CONNECTION_STRINGS,
        description="Mask connection strings in logs",
    )

    mask_api_keys: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.MASK_API_KEYS,
        description="Mask API keys in logs",
    )

    mask_ldap_passwords: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.MASK_LDAP_PASSWORDS,
        description="Mask LDAP passwords in logs",
    )

    mask_ldap_dns: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.MASK_LDAP_DNS,
        description="Mask LDAP DNs in logs",
    )

    # Log Message Templates
    use_standard_templates: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.USE_STANDARD_TEMPLATES,
        description="Use standard log message templates",
    )

    custom_log_format: str | None = Field(
        default=FlextDbtLdapConstants.DbtLogging.CUSTOM_LOG_FORMAT,
        description="Custom log message format",
    )

    # Audit Logging
    enable_audit_logging: bool = Field(
        default=FlextDbtLdapConstants.DbtLogging.ENABLE_AUDIT_LOGGING,
        description="Enable audit logging",
    )

    audit_log_file: str = Field(
        default=FlextDbtLdapConstants.DbtLogging.AUDIT_LOG_FILE,
        description="Audit log file path",
    )

    # Project Identification
    project_name: str = Field(
        default="flext-dbt-ldap",
        description="Project name",
    )

    project_version: str = Field(
        default="0.9.0",
        description="Project version",
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
    def validate_ldap_configuration_consistency(self) -> Self:
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

    def validate_business_rules(self) -> FlextResult[None]:
        """Validate DBT LDAP specific business rules."""
        try:
            # Validate LDAP configuration
            if not self.ldap_host:
                return FlextResult[None].fail("LDAP host is required")

            # Validate DBT configuration
            if not self.dbt_project_dir:
                return FlextResult[None].fail("DBT project directory is required")

            # Validate performance thresholds
            if self.dbt_ldap_performance_threshold_warning < 0:
                return FlextResult[None].fail(
                    "Performance warning threshold must be non-negative"
                )

            if self.dbt_ldap_performance_threshold_critical < 0:
                return FlextResult[None].fail(
                    "Performance critical threshold must be non-negative"
                )

            return FlextResult[None].ok(None)
        except Exception as e:
            return FlextResult[None].fail(f"Business rules validation failed: {e}")

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
        environment_mapping: dict[str, str] = {
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

    def get_ldap_quality_config(self) -> dict[str, object]:
        """Get data quality configuration for LDAP validation."""
        return {
            "min_quality_threshold": self.min_quality_threshold,
            "required_attributes": self.required_attributes,
            "validate_dns": self.validate_dns,
        }

    def get_dbt_ldap_logging_config(self) -> dict[str, object]:
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
        """Create configuration for specific environment using enhanced singleton pattern."""
        return cls.get_or_create_shared_instance(
            project_name="flext-dbt-ldap", environment=environment, **overrides
        )

    @classmethod
    def create_default(cls) -> FlextDbtLdapConfig:
        """Create default configuration instance using enhanced singleton pattern."""
        return cls.get_or_create_shared_instance(project_name="flext-dbt-ldap")

    @classmethod
    def create_for_development(cls) -> FlextDbtLdapConfig:
        """Create configuration optimized for development using enhanced singleton pattern."""
        return cls.get_or_create_shared_instance(
            project_name="flext-dbt-ldap",
            ldap_use_tls=False,
            dbt_target="dev",
            dbt_threads=1,
            dbt_log_level="debug",
            enable_audit_logging=False,
        )

    @classmethod
    def create_for_production(cls) -> FlextDbtLdapConfig:
        """Create configuration optimized for production using enhanced singleton pattern."""
        return cls.get_or_create_shared_instance(
            project_name="flext-dbt-ldap",
            ldap_use_tls=True,
            dbt_target="production",
            dbt_threads=8,
            dbt_log_level="info",
            enable_audit_logging=True,
            track_dbt_ldap_performance=True,
        )

    @classmethod
    def create_for_testing(cls) -> FlextDbtLdapConfig:
        """Create configuration optimized for testing using enhanced singleton pattern."""
        return cls.get_or_create_shared_instance(
            project_name="flext-dbt-ldap",
            ldap_host="test.example.com",
            ldap_port=389,
            ldap_use_tls=False,
            dbt_target="test",
            dbt_threads=1,
            dbt_log_level="debug",
            enable_audit_logging=False,
            min_quality_threshold=0.5,
        )

    @classmethod
    def get_global_instance(cls) -> FlextDbtLdapConfig:
        """Get the global singleton instance using enhanced FlextConfig pattern."""
        return cls.get_or_create_shared_instance(project_name="flext-dbt-ldap")

    @classmethod
    def get_or_create_shared_instance(
        cls,
        _project_name: str | None = None,
        **kwargs: object,
    ) -> Self:
        """Get or create shared singleton instance with optional configuration."""
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    # Create instance with provided kwargs
                    instance = cls(**kwargs)
                    cls._instances[cls] = instance
        return cast("Self", cls._instances[cls])

    @classmethod
    def reset_shared_instance(cls) -> None:
        """Reset the shared singleton instance."""
        with cls._lock:
            cls._instances.pop(cls, None)

    @classmethod
    def reset_global_instance(cls) -> None:
        """Reset the global FlextDbtLdapConfig instance (mainly for testing)."""
        # Use the enhanced FlextConfig reset mechanism
        cls.reset_shared_instance()


__all__: FlextDbtLdapTypes.DbtLdapCore.StringList = [
    "FlextDbtLdapConfig",
]
