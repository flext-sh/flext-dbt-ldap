"""FLEXT DBT LDAP Utilities - Comprehensive DBT LDAP Integration Utilities.

Copyright (c) 2025 FLEXT Contributors
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from flext_core import (
    FlextContainer,
    FlextLogger,
    FlextResult,
    FlextUtilities,
)


class FlextDbtLdapUtilities(FlextUtilities):
    """Unified DBT LDAP utilities service extending FlextUtilities.

    Provides comprehensive DBT LDAP utilities for data transformation, LDAP integration,
    and DBT project management without duplicating functionality.
    Uses FlextDbtLdapModels for all domain-specific data structures.
    """

    # Performance analysis constants
    PERFORMANCE_EXECUTION_TIME_THRESHOLD = 300  # 5 minutes in seconds
    PERFORMANCE_MEMORY_USAGE_THRESHOLD = 1000  # 1GB in MB
    PERFORMANCE_ROWS_PROCESSED_THRESHOLD = 1000000  # 1M rows

    def __init__(self) -> None:
        """Initialize FlextDbtLdapUtilities service."""
        super().__init__()
        self._container = FlextContainer.get_global()
        self._logger = FlextLogger(__name__)

    def execute(self) -> FlextResult[dict[str, Any]]:
        """Execute the main DBT LDAP service operation.

        Returns:
            FlextResult[dict[str, Any]]: Service status and capabilities.

        """
        return FlextResult[dict[str, Any]].ok({
            "status": "operational",
            "service": "flext-dbt-ldap-utilities",
            "capabilities": [
                "dbt_project_management",
                "ldap_data_transformation",
                "schema_generation",
                "macro_management",
                "dbt_model_validation",
                "ldap_source_configuration",
                "transformation_optimization",
            ],
        })

    @property
    def logger(self) -> FlextLogger:
        """Get logger instance."""
        return self._logger

    @property
    def container(self) -> FlextContainer:
        """Get container instance."""
        return self._container

    class DbtProjectManagement:
        """DBT project management utilities."""

        @staticmethod
        def create_dbt_project_config(
            project_name: str,
            ldap_sources: list[dict[str, Any]],
            target_schema: str = "ldap_transformed",
        ) -> FlextResult[dict[str, Any]]:
            """Create DBT project configuration for LDAP data transformation.

            Args:
                project_name: Name of the DBT project
                ldap_sources: List of LDAP source configurations
                target_schema: Target schema for transformed data

            Returns:
                FlextResult containing DBT project configuration or error

            """
            try:
                project_config = {
                    "name": project_name,
                    "version": "1.0.0",
                    "profile": f"{project_name}_profile",
                    "model-paths": ["models"],
                    "analysis-paths": ["analyses"],
                    "test-paths": ["tests"],
                    "seed-paths": ["seeds"],
                    "macro-paths": ["macros"],
                    "snapshot-paths": ["snapshots"],
                    "target-path": "target",
                    "clean-targets": ["target", "dbt_packages"],
                    "models": {
                        project_name: {
                            "materialized": "table",
                            "schema": target_schema,
                            "tags": ["ldap", "transformation"],
                        }
                    },
                    "sources": {"ldap_sources": {"tables": ldap_sources}},
                }

                return FlextResult[dict[str, Any]].ok(project_config)
            except Exception as e:
                return FlextResult[dict[str, Any]].fail(
                    f"DBT project config creation failed: {e}"
                )

        @staticmethod
        def generate_dbt_profiles(
            profile_name: str,
            connection_config: dict[str, Any],
        ) -> FlextResult[dict[str, Any]]:
            """Generate DBT profiles configuration for LDAP data sources.

            Args:
                profile_name: Name of the DBT profile
                connection_config: Database connection configuration

            Returns:
                FlextResult containing DBT profiles configuration or error

            """
            try:
                profiles_config = {
                    profile_name: {
                        "target": "dev",
                        "outputs": {
                            "dev": {
                                "type": connection_config.get("type", "postgres"),
                                "host": connection_config.get("host", "localhost"),
                                "user": connection_config.get("user", "dbt_user"),
                                "password": connection_config.get("password", ""),
                                "port": connection_config.get("port", 5432),
                                "dbname": connection_config.get("dbname", "ldap_db"),
                                "schema": connection_config.get("schema", "public"),
                                "threads": connection_config.get("threads", 4),
                                "keepalives_idle": 0,
                            },
                            "prod": {
                                "type": connection_config.get("type", "postgres"),
                                "host": connection_config.get("prod_host", "prod-db"),
                                "user": connection_config.get("prod_user", "dbt_user"),
                                "password": connection_config.get("prod_password", ""),
                                "port": connection_config.get("port", 5432),
                                "dbname": connection_config.get(
                                    "prod_dbname", "ldap_prod"
                                ),
                                "schema": connection_config.get(
                                    "prod_schema", "public"
                                ),
                                "threads": connection_config.get("threads", 8),
                                "keepalives_idle": 0,
                            },
                        },
                    }
                }

                return FlextResult[dict[str, Any]].ok(profiles_config)
            except Exception as e:
                return FlextResult[dict[str, Any]].fail(
                    f"DBT profiles generation failed: {e}"
                )

        @staticmethod
        def validate_dbt_project_structure(
            project_path: Path,
        ) -> FlextResult[dict[str, bool]]:
            """Validate DBT project structure for LDAP transformation project.

            Args:
                project_path: Path to the DBT project

            Returns:
                FlextResult containing validation results or error

            """
            try:
                required_files = {
                    "dbt_project.yml": project_path / "dbt_project.yml",
                    "profiles.yml": project_path / "profiles.yml",
                    "models_dir": project_path / "models",
                    "macros_dir": project_path / "macros",
                    "tests_dir": project_path / "tests",
                }

                validation_results = {}
                for name, path in required_files.items():
                    validation_results[name] = path.exists()

                return FlextResult[dict[str, bool]].ok(validation_results)
            except Exception as e:
                return FlextResult[dict[str, bool]].fail(
                    f"DBT project structure validation failed: {e}"
                )

    class LdapDataTransformation:
        """LDAP data transformation utilities."""

        @staticmethod
        def generate_ldap_source_schema(
            ldap_attributes: list[str],
            source_name: str = "ldap_users",
        ) -> FlextResult[dict[str, Any]]:
            """Generate DBT source schema for LDAP attributes.

            Args:
                ldap_attributes: List of LDAP attribute names
                source_name: Name for the LDAP source

            Returns:
                FlextResult containing DBT source schema or error

            """
            try:
                columns = []
                for attr in ldap_attributes:
                    # Map common LDAP attributes to appropriate data types
                    if attr.lower() in {"createtimestamp", "modifytimestamp"}:
                        data_type = "timestamp"
                    elif attr.lower() in {"memberof", "objectclass"}:
                        data_type = "text[]"  # Array for multi-valued attributes
                    elif attr.lower() in {"uidnumber", "gidnumber"}:
                        data_type = "integer"
                    else:
                        data_type = "text"  # Default for string attributes

                    columns.append({
                        "name": attr.lower().replace("-", "_"),
                        "description": f"LDAP {attr} attribute",
                        "data_type": data_type,
                    })

                source_schema = {
                    "version": 2,
                    "sources": [
                        {
                            "name": "ldap",
                            "description": "LDAP directory data source",
                            "tables": [
                                {
                                    "name": source_name,
                                    "description": f"LDAP {source_name} data",
                                    "columns": columns,
                                }
                            ],
                        }
                    ],
                }

                return FlextResult[dict[str, Any]].ok(source_schema)
            except Exception as e:
                return FlextResult[dict[str, Any]].fail(
                    f"LDAP source schema generation failed: {e}"
                )

        @staticmethod
        def create_ldap_transformation_model(
            model_name: str,
            source_table: str,
            transformations: dict[str, str],
        ) -> FlextResult[str]:
            """Create DBT model SQL for LDAP data transformation.

            Args:
                model_name: Name of the DBT model
                source_table: Source table name
                transformations: Dictionary of column transformations

            Returns:
                FlextResult containing DBT model SQL or error

            """
            try:
                # Build SELECT clause with transformations
                select_clauses = []
                for column, transformation in transformations.items():
                    if transformation == "identity":
                        select_clauses.append(f"    {column}")
                    else:
                        select_clauses.append(f"    {transformation} as {column}")

                # DBT template generation - safe string formatting
                model_sql = f"""{{{{
    config(
        materialized='table',
        tags=['ldap', 'transformation'],
        description='Transformed LDAP data for {model_name}'
    )
}}}}

select
{",".join(select_clauses)}
from {{{{ source('ldap', '{source_table}') }}}}
where 1=1
    -- Add any filtering conditions here
    and objectclass is not null
"""

                return FlextResult[str].ok(model_sql)
            except Exception as e:
                return FlextResult[str].fail(
                    f"LDAP transformation model creation failed: {e}"
                )

        @staticmethod
        def generate_ldap_data_tests(
            model_name: str,
            test_config: dict[str, Any],
        ) -> FlextResult[dict[str, Any]]:
            """Generate DBT data tests for LDAP transformation models.

            Args:
                model_name: Name of the model to test
                test_config: Test configuration parameters

            Returns:
                FlextResult containing DBT test configuration or error

            """
            try:
                tests = {
                    "version": 2,
                    "models": [
                        {
                            "name": model_name,
                            "description": f"Data tests for {model_name} LDAP model",
                            "tests": [
                                "unique",
                                "not_null",
                            ],
                            "columns": [],
                        }
                    ],
                }

                # Add column-specific tests
                for column, column_tests in test_config.get("columns", {}).items():
                    column_config = {
                        "name": column,
                        "description": f"Tests for {column} column",
                        "tests": column_tests,
                    }
                    tests["models"][0]["columns"].append(column_config)

                return FlextResult[dict[str, Any]].ok(tests)
            except Exception as e:
                return FlextResult[dict[str, Any]].fail(
                    f"LDAP data tests generation failed: {e}"
                )

    class MacroManagement:
        """DBT macro management utilities for LDAP operations."""

        @staticmethod
        def create_ldap_parsing_macro(
            macro_name: str = "parse_ldap_dn",
        ) -> FlextResult[str]:
            """Create DBT macro for parsing LDAP distinguished names.

            Args:
                macro_name: Name of the macro

            Returns:
                FlextResult containing macro SQL or error

            """
            try:
                macro_sql = f"""-- Macro to parse LDAP Distinguished Name (DN) components
{{% macro {macro_name}(dn_column, component='cn') %}}
    case
        when {{{{{{dn_column}}}}}} is null then null
        when position('{{{{{{component}}}}}}=' in lower({{{{{{dn_column}}}}}}) = 0 then null
        else trim(both '"' from
            split_part(
                split_part(
                    lower({{{{{{dn_column}}}}}}),
                    '{{{{{{component}}}}}}=',
                    2
                ),
                ',',
                1
            )
        )
    end
{{% endmacro %}}"""

                return FlextResult[str].ok(macro_sql)
            except Exception as e:
                return FlextResult[str].fail(f"LDAP parsing macro creation failed: {e}")

        @staticmethod
        def create_ldap_attribute_macro(
            macro_name: str = "extract_ldap_attribute",
        ) -> FlextResult[str]:
            """Create DBT macro for extracting LDAP attributes from arrays.

            Args:
                macro_name: Name of the macro

            Returns:
                FlextResult containing macro SQL or error

            """
            try:
                # DBT macro template generation - safe string formatting
                macro_sql = f"""-- Macro to extract specific values from LDAP multi-valued attributes
{{% macro {macro_name}(attribute_array, filter_pattern='') %}}
    case
        when {{{{{{attribute_array}}}}}} is null then null
        when array_length({{{{{{attribute_array}}}}}}, 1) = 0 then null
        {{% if filter_pattern %}}
        else (
            select array_agg(attr)
            from unnest({{{{{{attribute_array}}}}}}) as attr
            where attr ilike '%{{{{{{filter_pattern}}}}}}%'
        )[1]
        {{% else %}}
        else {{{{{{attribute_array}}}}}}[1]
        {{% endif %}}
    end
{{% endmacro %}}"""

                return FlextResult[str].ok(macro_sql)
            except Exception as e:
                return FlextResult[str].fail(
                    f"LDAP attribute macro creation failed: {e}"
                )

        @staticmethod
        def create_ldap_normalization_macro(
            macro_name: str = "normalize_ldap_timestamp",
        ) -> FlextResult[str]:
            """Create DBT macro for normalizing LDAP timestamps.

            Args:
                macro_name: Name of the macro

            Returns:
                FlextResult containing macro SQL or error

            """
            try:
                macro_sql = f"""-- Macro to normalize LDAP timestamps to standard format
{{% macro {macro_name}(timestamp_column) %}}
    case
        when {{{{{{timestamp_column}}}}}} is null then null
        when length({{{{{{timestamp_column}}}}}}) = 14 then
            -- LDAP GeneralizedTime format: YYYYMMDDHHMMSSZ
            to_timestamp(
                substring({{{{{{timestamp_column}}}}}} from 1 for 14),
                'YYYYMMDDHH24MISS'
            )
        else
            -- Try to parse as standard timestamp
            try_cast({{{{{{timestamp_column}}}}}} as timestamp)
    end
{{% endmacro %}}"""

                return FlextResult[str].ok(macro_sql)
            except Exception as e:
                return FlextResult[str].fail(
                    f"LDAP normalization macro creation failed: {e}"
                )

    class SchemaGeneration:
        """Schema generation utilities for LDAP data structures."""

        @staticmethod
        def generate_user_schema() -> FlextResult[dict[str, Any]]:
            """Generate standard schema for LDAP user data.

            Returns:
                FlextResult containing user schema configuration or error

            """
            try:
                user_schema = {
                    "version": 2,
                    "models": [
                        {
                            "name": "ldap_users",
                            "description": "Normalized LDAP user data",
                            "columns": [
                                {
                                    "name": "user_id",
                                    "description": "Unique user identifier",
                                    "tests": ["unique", "not_null"],
                                },
                                {
                                    "name": "username",
                                    "description": "User login name",
                                    "tests": ["unique", "not_null"],
                                },
                                {
                                    "name": "email",
                                    "description": "User email address",
                                    "tests": ["not_null"],
                                },
                                {
                                    "name": "full_name",
                                    "description": "User display name",
                                },
                                {
                                    "name": "department",
                                    "description": "User department",
                                },
                                {
                                    "name": "manager",
                                    "description": "User manager",
                                },
                                {
                                    "name": "groups",
                                    "description": "User group memberships",
                                },
                                {
                                    "name": "created_at",
                                    "description": "Account creation timestamp",
                                },
                                {
                                    "name": "modified_at",
                                    "description": "Last modification timestamp",
                                },
                                {
                                    "name": "is_active",
                                    "description": "User active status",
                                    "tests": ["not_null"],
                                },
                            ],
                        }
                    ],
                }

                return FlextResult[dict[str, Any]].ok(user_schema)
            except Exception as e:
                return FlextResult[dict[str, Any]].fail(
                    f"User schema generation failed: {e}"
                )

        @staticmethod
        def generate_group_schema() -> FlextResult[dict[str, Any]]:
            """Generate standard schema for LDAP group data.

            Returns:
                FlextResult containing group schema configuration or error

            """
            try:
                group_schema = {
                    "version": 2,
                    "models": [
                        {
                            "name": "ldap_groups",
                            "description": "Normalized LDAP group data",
                            "columns": [
                                {
                                    "name": "group_id",
                                    "description": "Unique group identifier",
                                    "tests": ["unique", "not_null"],
                                },
                                {
                                    "name": "group_name",
                                    "description": "Group name",
                                    "tests": ["unique", "not_null"],
                                },
                                {
                                    "name": "description",
                                    "description": "Group description",
                                },
                                {
                                    "name": "group_type",
                                    "description": "Type of group (security, distribution, etc.)",
                                },
                                {
                                    "name": "members",
                                    "description": "Group member list",
                                },
                                {
                                    "name": "created_at",
                                    "description": "Group creation timestamp",
                                },
                                {
                                    "name": "modified_at",
                                    "description": "Last modification timestamp",
                                },
                            ],
                        }
                    ],
                }

                return FlextResult[dict[str, Any]].ok(group_schema)
            except Exception as e:
                return FlextResult[dict[str, Any]].fail(
                    f"Group schema generation failed: {e}"
                )

    class TransformationOptimization:
        """Transformation optimization utilities."""

        # Performance threshold constants
        PERFORMANCE_EXECUTION_TIME_THRESHOLD: float = 30.0  # seconds
        PERFORMANCE_MEMORY_USAGE_THRESHOLD: float = 1024.0  # MB
        PERFORMANCE_ROWS_PROCESSED_THRESHOLD: int = 100000  # rows

        @staticmethod
        def optimize_ldap_query(
            base_query: str,
            optimization_hints: dict[str, Any],
        ) -> FlextResult[str]:
            """Optimize DBT SQL query for LDAP data processing.

            Args:
                base_query: Base SQL query to optimize
                optimization_hints: Optimization configuration

            Returns:
                FlextResult containing optimized query or error

            """
            try:
                optimized_query = base_query

                # Add indexing hints if specified
                if optimization_hints.get("add_indexes"):
                    index_columns = optimization_hints.get("index_columns", [])
                    for column in index_columns:
                        optimized_query = (
                            f"-- Consider adding index on {column}\n{optimized_query}"
                        )

                # Add partitioning hints
                if optimization_hints.get("partition_by"):
                    partition_column = optimization_hints["partition_by"]
                    optimized_query = f"{optimized_query}\n-- Consider partitioning by {partition_column}"

                # Add filtering optimizations
                if optimization_hints.get("filter_early"):
                    optimized_query = optimized_query.replace(
                        "where 1=1",
                        "where 1=1\n    -- Apply filters early for performance",
                    )

                return FlextResult[str].ok(optimized_query)
            except Exception as e:
                return FlextResult[str].fail(f"Query optimization failed: {e}")

        @classmethod
        def analyze_transformation_performance(
            cls,
            model_stats: dict[str, Any],
        ) -> FlextResult[dict[str, Any]]:
            """Analyze performance of LDAP transformation models.

            Args:
                model_stats: Model execution statistics

            Returns:
                FlextResult containing performance analysis or error

            """
            try:
                analysis = {
                    "execution_time": model_stats.get("execution_time", 0),
                    "rows_processed": model_stats.get("rows_processed", 0),
                    "memory_usage": model_stats.get("memory_usage", 0),
                    "recommendations": [],
                }

                # Generate performance recommendations
                if (
                    analysis["execution_time"]
                    > cls.PERFORMANCE_EXECUTION_TIME_THRESHOLD
                ):
                    analysis["recommendations"].append(
                        "Consider adding indexes or partitioning for large datasets"
                    )

                if analysis["memory_usage"] > cls.PERFORMANCE_MEMORY_USAGE_THRESHOLD:
                    analysis["recommendations"].append(
                        "Consider processing data in smaller batches"
                    )

                if (
                    analysis["rows_processed"]
                    > cls.PERFORMANCE_ROWS_PROCESSED_THRESHOLD
                ):
                    analysis["recommendations"].append(
                        "Consider incremental processing for large datasets"
                    )

                return FlextResult[dict[str, Any]].ok(analysis)
            except Exception as e:
                return FlextResult[dict[str, Any]].fail(
                    f"Performance analysis failed: {e}"
                )

    def execute(self) -> FlextResult[dict[str, Any]]:
        """Execute DBT LDAP utilities service operation hronously."""
        return FlextResult[dict[str, Any]].ok({
            "status": "operational",
            "service": "flext-dbt-ldap-utilities",
            "timestamp": "now",
            "version": "1.0.0",
        })


__all__ = ["FlextDbtLdapUtilities"]
