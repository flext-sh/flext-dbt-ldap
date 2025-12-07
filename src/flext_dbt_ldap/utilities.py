"""FLEXT DBT LDAP Utilities - Complete DBT LDAP Integration Utilities.

Copyright (c) 2025 FLEXT Contributors
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Callable, Iterable, Mapping
from enum import StrEnum
from functools import cache, wraps
from pathlib import Path
from typing import Annotated, TypeIs, TypeVar, get_type_hints

from flext_core import r, t, u as u_core
from flext_core.container import FlextContainer
from pydantic import BaseModel, BeforeValidator, ConfigDict, validate_call

from flext_dbt_ldap.typings import FlextDbtLdapTypes

T = TypeVar("T")


class FlextDbtLdapUtilities(u_core):
    """Unified DBT LDAP utilities service extending u.

    Provides complete DBT LDAP utilities for data transformation, LDAP integration,
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

    def execute(self) -> r[FlextDbtLdapTypes.DbtLdapCore.ResultDict]:
        """Execute the main DBT LDAP service operation.

        Returns:
        r[FlextDbtLdapTypes.DbtLdapCore.ResultDict]: Service status and capabilities.

        """
        return r[FlextDbtLdapTypes.DbtLdapCore.ResultDict].ok({
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

    class DbtProjectManagement:
        """DBT project management utilities."""

        @staticmethod
        def create_dbt_project_config(
            project_name: str,
            ldap_sources: list[FlextDbtLdapTypes.DbtSource.SourceTable],
            target_schema: str = "ldap_transformed",
        ) -> r[FlextDbtLdapTypes.DbtProject.ProjectConfiguration]:
            """Create DBT project configuration for LDAP data transformation.

            Args:
            project_name: Name of the DBT project
            ldap_sources: List of LDAP source configurations
            target_schema: Target schema for transformed data

            Returns:
            r containing DBT project configuration or error

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
                        },
                    },
                    "sources": {"ldap_sources": {"tables": ldap_sources}},
                }

                return r[FlextDbtLdapTypes.DbtProject.ProjectConfiguration].ok(
                    project_config
                )
            except Exception as e:
                return r[FlextDbtLdapTypes.DbtProject.ProjectConfiguration].fail(
                    f"DBT project config creation failed: {e}"
                )

        @staticmethod
        def generate_dbt_profiles(
            profile_name: str,
            connection_config: FlextDbtLdapTypes.DbtProject.ProfileConfiguration,
        ) -> r[FlextDbtLdapTypes.DbtProject.ProfileConfiguration]:
            """Generate DBT profiles configuration for LDAP data sources.

            Args:
            profile_name: Name of the DBT profile
            connection_config: Database connection configuration

            Returns:
            r containing DBT profiles configuration or error

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
                                    "prod_dbname",
                                    "ldap_prod",
                                ),
                                "schema": connection_config.get(
                                    "prod_schema",
                                    "public",
                                ),
                                "threads": connection_config.get("threads", 8),
                                "keepalives_idle": 0,
                            },
                        },
                    },
                }

                return r[FlextDbtLdapTypes.DbtProject.ProfileConfiguration].ok(
                    profiles_config
                )
            except Exception as e:
                return r[FlextDbtLdapTypes.DbtProject.ProfileConfiguration].fail(
                    f"DBT profiles generation failed: {e}"
                )

        @staticmethod
        def validate_dbt_project_structure(
            project_path: Path,
        ) -> r[FlextDbtLdapTypes.DbtLdapCore.BoolDict]:
            """Validate DBT project structure for LDAP transformation project.

            Args:
            project_path: Path to the DBT project

            Returns:
            r containing validation results or error

            """
            try:
                required_files = {
                    "dbt_project.yml": project_path / "dbt_project.yml",
                    "profiles.yml": project_path / "profiles.yml",
                    "models_dir": project_path / "models",
                    "macros_dir": project_path / "macros",
                    "tests_dir": project_path / "tests",
                }

                validation_results: FlextDbtLdapTypes.DbtLdapCore.BoolDict = {}
                for name, path in required_files.items():
                    validation_results[name] = path.exists()

                return r[FlextDbtLdapTypes.DbtLdapCore.BoolDict].ok(
                    validation_results,
                )
            except Exception as e:
                return r[FlextDbtLdapTypes.DbtLdapCore.BoolDict].fail(
                    f"DBT project structure validation failed: {e}",
                )

    class LdapDataTransformation:
        """LDAP data transformation utilities."""

        @staticmethod
        def generate_ldap_source_schema(
            ldap_attributes: list[str],
            source_name: str = "ldap_users",
        ) -> r[FlextDbtLdapTypes.DbtSource.SourceSchema]:
            """Generate DBT source schema for LDAP attributes.

            Args:
            ldap_attributes: List of LDAP attribute names
            source_name: Name for the LDAP source

            Returns:
            r containing DBT source schema or error

            """
            try:
                columns: list[FlextDbtLdapTypes.DbtLdapCore.DataDict] = []
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

                source_schema: FlextDbtLdapTypes.DbtSource.SourceSchema = {
                    "version": "2",
                    "sources": [
                        {
                            "name": "ldap",
                            "description": "LDAP directory data source",
                            "tables": [
                                {
                                    "name": source_name,
                                    "description": f"LDAP {source_name} data",
                                    "columns": columns,
                                },
                            ],
                        },
                    ],
                }

                return r[FlextDbtLdapTypes.DbtSource.SourceSchema].ok(
                    source_schema,
                )
            except Exception as e:
                return r[FlextDbtLdapTypes.DbtSource.SourceSchema].fail(
                    f"LDAP source schema generation failed: {e}",
                )

        @staticmethod
        def create_ldap_transformation_model(
            model_name: str,
            source_table: str,
            transformations: dict[str, str],
        ) -> r[str]:
            """Create DBT model SQL for LDAP data transformation.

            Args:
            model_name: Name of the DBT model
            source_table: Source table name
            transformations: Dictionary of column transformations

            Returns:
            r containing DBT model SQL or error

            """
            try:
                # Build SELECT clause with transformations
                select_clauses: list[str] = []
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
        description=f'Transformed LDAP data for {model_name}'
    )
}}}}

select
{",".join(select_clauses)}
from {{{{ source('ldap', '{source_table}') }}}}
where 1=1
    -- Add any filtering conditions here
    and objectclass is not null
"""

                return r[str].ok(model_sql)
            except Exception as e:
                return r[str].fail(
                    f"LDAP transformation model creation failed: {e}",
                )

        @staticmethod
        def generate_ldap_data_tests(
            model_name: str,
            test_config: FlextDbtLdapTypes.DbtProject.TestConfiguration,
        ) -> r[FlextDbtLdapTypes.DbtProject.TestConfiguration]:
            """Generate DBT data tests for LDAP transformation models.

            Args:
            model_name: Name of the model to test
            test_config: Test configuration parameters

            Returns:
            r containing DBT test configuration or error

            """
            try:
                tests: FlextDbtLdapTypes.DbtProject.TestConfiguration = {
                    "version": "2",
                    "models": [
                        {
                            "name": model_name,
                            "description": f"Data tests for {model_name} LDAP model",
                            "tests": [
                                "unique",
                                "not_null",
                            ],
                            "columns": [],
                        },
                    ],
                }

                # Add column-specific tests
                columns_config_value = test_config.get("columns")
                if not isinstance(columns_config_value, dict):
                    return r[FlextDbtLdapTypes.DbtProject.TestConfiguration].ok(tests)

                models_list_value = tests.get("models")
                if not isinstance(models_list_value, list) or not models_list_value:
                    return r[FlextDbtLdapTypes.DbtProject.TestConfiguration].ok(tests)

                model_dict = models_list_value[0]
                if not isinstance(model_dict, dict):
                    return r[FlextDbtLdapTypes.DbtProject.TestConfiguration].ok(tests)

                columns_list_value = model_dict.get("columns")
                if isinstance(columns_list_value, list):
                    for (
                        column,
                        column_tests,
                    ) in columns_config_value.items():
                        column_config: FlextDbtLdapTypes.DbtLdapCore.DataDict = {
                            "name": column,
                            "description": f"Tests for {column} column",
                            "tests": column_tests,
                        }
                        columns_list_value.append(column_config)

                return r[FlextDbtLdapTypes.DbtProject.TestConfiguration].ok(
                    tests,
                )
            except Exception as e:
                return r[FlextDbtLdapTypes.DbtProject.TestConfiguration].fail(
                    f"LDAP data tests generation failed: {e}",
                )

    class MacroManagement:
        """DBT macro management utilities for LDAP operations."""

        @staticmethod
        def create_ldap_parsing_macro(
            macro_name: str = "parse_ldap_dn",
        ) -> r[str]:
            """Create DBT macro for parsing LDAP distinguished names.

            Args:
            macro_name: Name of the macro

            Returns:
            r containing macro SQL or error

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

                return r[str].ok(macro_sql)
            except Exception as e:
                return r[str].fail(f"LDAP parsing macro creation failed: {e}")

        @staticmethod
        def create_ldap_attribute_macro(
            macro_name: str = "extract_ldap_attribute",
        ) -> r[str]:
            """Create DBT macro for extracting LDAP attributes from arrays.

            Args:
            macro_name: Name of the macro

            Returns:
            r containing macro SQL or error

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

                return r[str].ok(macro_sql)
            except Exception as e:
                return r[str].fail(
                    f"LDAP attribute macro creation failed: {e}",
                )

        @staticmethod
        def create_ldap_normalization_macro(
            macro_name: str = "normalize_ldap_timestamp",
        ) -> r[str]:
            """Create DBT macro for normalizing LDAP timestamps.

            Args:
            macro_name: Name of the macro

            Returns:
            r containing macro SQL or error

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

                return r[str].ok(macro_sql)
            except Exception as e:
                return r[str].fail(
                    f"LDAP normalization macro creation failed: {e}",
                )

    class SchemaGeneration:
        """Schema generation utilities for LDAP data structures."""

        @staticmethod
        def generate_user_schema() -> r[FlextDbtLdapTypes.DbtModel.ModelDefinition]:
            """Generate standard schema for LDAP user data.

            Returns:
            r containing user schema configuration or error

            """
            try:
                user_schema: FlextDbtLdapTypes.DbtModel.ModelDefinition = {
                    "version": "2",
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
                        },
                    ],
                }

                return r[FlextDbtLdapTypes.DbtModel.ModelDefinition].ok(
                    user_schema,
                )
            except Exception as e:
                return r[FlextDbtLdapTypes.DbtModel.ModelDefinition].fail(
                    f"User schema generation failed: {e}",
                )

        @staticmethod
        def generate_group_schema() -> r[FlextDbtLdapTypes.DbtModel.ModelDefinition]:
            """Generate standard schema for LDAP group data.

            Returns:
            r containing group schema configuration or error

            """
            try:
                group_schema: FlextDbtLdapTypes.DbtModel.ModelDefinition = {
                    "version": "2",
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
                        },
                    ],
                }

                return r[FlextDbtLdapTypes.DbtModel.ModelDefinition].ok(
                    group_schema,
                )
            except Exception as e:
                return r[FlextDbtLdapTypes.DbtModel.ModelDefinition].fail(
                    f"Group schema generation failed: {e}",
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
            optimization_hints: FlextDbtLdapTypes.DbtLdapCore.ConfigDict,
        ) -> r[str]:
            """Optimize DBT SQL query for LDAP data processing.

            Args:
            base_query: Base SQL query to optimize
            optimization_hints: Optimization configuration

            Returns:
            r containing optimized query or error

            """
            try:
                optimized_query = base_query

                # Add indexing hints if specified
                add_indexes_value = optimization_hints.get("add_indexes")
                if add_indexes_value:
                    index_columns_value = optimization_hints.get("index_columns")
                    if isinstance(index_columns_value, list):
                        for column in index_columns_value:
                            if isinstance(column, str):
                                optimized_query = f"-- Consider adding index on {column}\n{optimized_query}"

                # Add partitioning hints
                partition_by_value = optimization_hints.get("partition_by")
                if partition_by_value:
                    optimized_query = f"{optimized_query}\n-- Consider partitioning by {partition_by_value}"

                # Add filtering optimizations
                filter_early_value = optimization_hints.get("filter_early")
                if filter_early_value:
                    optimized_query = optimized_query.replace(
                        "where 1=1",
                        "where 1=1\n    -- Apply filters early for performance",
                    )

                return r[str].ok(optimized_query)
            except Exception as e:
                return r[str].fail(f"Query optimization failed: {e}")

        @classmethod
        def analyze_transformation_performance(
            cls,
            model_stats: FlextDbtLdapTypes.DbtLdapCore.MetricsDict,
        ) -> r[FlextDbtLdapTypes.DbtLdapCore.MetricsDict]:
            """Analyze performance of LDAP transformation models.

            Args:
            model_stats: Model execution statistics

            Returns:
            r containing performance analysis or error

            """
            try:
                execution_time_value = model_stats.get("execution_time", 0)
                rows_processed_value = model_stats.get("rows_processed", 0)
                memory_usage_value = model_stats.get("memory_usage", 0)

                execution_time = (
                    execution_time_value
                    if isinstance(execution_time_value, (int, float))
                    else 0.0
                )
                rows_processed = (
                    rows_processed_value if isinstance(rows_processed_value, int) else 0
                )
                memory_usage = (
                    memory_usage_value
                    if isinstance(memory_usage_value, (int, float))
                    else 0.0
                )
                recommendations: list[str] = []

                # Generate performance recommendations
                if execution_time > cls.PERFORMANCE_EXECUTION_TIME_THRESHOLD:
                    recommendations.append(
                        "Consider adding indexes or partitioning for large datasets",
                    )

                if memory_usage > cls.PERFORMANCE_MEMORY_USAGE_THRESHOLD:
                    recommendations.append(
                        "Consider processing data in smaller batches",
                    )

                if rows_processed > cls.PERFORMANCE_ROWS_PROCESSED_THRESHOLD:
                    recommendations.append(
                        "Consider incremental processing for large datasets",
                    )

                analysis: FlextDbtLdapTypes.DbtLdapCore.MetricsDict = {
                    "execution_time": execution_time,
                    "rows_processed": rows_processed,
                    "memory_usage": memory_usage,
                    "recommendations": recommendations,
                }

                return r[FlextDbtLdapTypes.DbtLdapCore.MetricsDict].ok(
                    analysis,
                )
            except Exception as e:
                return r[FlextDbtLdapTypes.DbtLdapCore.MetricsDict].fail(
                    f"Performance analysis failed: {e}",
                )

    # ═══════════════════════════════════════════════════════════════════
    # TypeIs (PEP 742), BeforeValidator, validate_call, collections.abc, ParamSpec.
    # ═══════════════════════════════════════════════════════════════════

    class Enum:
        """TypeIs genérico, parsing, coerção - ZERO TypeGuard manual."""

        @staticmethod
        def is_member[E: StrEnum](enum_cls: type[E], value: object) -> TypeIs[E]:
            """TypeIs narrowing em AMBAS branches if/else."""
            return isinstance(value, enum_cls) or (
                isinstance(value, str) and value in enum_cls._value2member_map_
            )

        @staticmethod
        def is_subset[E: StrEnum](
            enum_cls: type[E],
            valid: frozenset[E],
            value: object,
        ) -> TypeIs[E]:
            """Check if value is a valid subset member of the enum."""
            if isinstance(value, enum_cls):
                return value in valid
            if isinstance(value, str):
                try:
                    return enum_cls(value) in valid
                except ValueError:
                    return False
            return False

        @staticmethod
        def parse[E: StrEnum](enum_cls: type[E], value: str | E) -> r[E]:
            """Parse string or enum value to enum result."""
            if isinstance(value, enum_cls):
                return r.ok(value)
            try:
                return r.ok(enum_cls(value))
            except ValueError:
                return r.fail(f"Invalid {enum_cls.__name__}: '{value}'")

        @staticmethod
        def coerce_validator[E: StrEnum](enum_cls: type[E]) -> Callable[[str | E], E]:
            """BeforeValidator factory para Pydantic."""

            def _coerce(v: str | E) -> E:
                if isinstance(v, enum_cls):
                    return v
                if isinstance(v, str):
                    try:
                        return enum_cls(v)
                    except ValueError:
                        pass
                msg = f"Invalid {enum_cls.__name__}: {v!r}"
                raise ValueError(msg)

            return _coerce

        @staticmethod
        @cache
        def values[E: StrEnum](enum_cls: type[E]) -> frozenset[str]:
            """Get all enum values as frozenset."""
            return frozenset(m.value for m in enum_cls)

    class Collection:
        """Parsing de Sequence/Mapping com StrEnums."""

        @staticmethod
        def parse_sequence[E: StrEnum](
            enum_cls: type[E],
            values: Iterable[str | E],
        ) -> r[tuple[E, ...]]:
            """Parse sequence of strings/enums to enum tuple."""
            parsed, errors = [], []
            for i, v in enumerate(values):
                if isinstance(v, enum_cls):
                    parsed.append(v)
                else:
                    try:
                        parsed.append(enum_cls(v))
                    except ValueError:
                        errors.append(f"[{i}]: '{v}'")
            return r.fail(f"Invalid: {errors}") if errors else r.ok(tuple(parsed))

        @staticmethod
        def coerce_list_validator[E: StrEnum](
            enum_cls: type[E],
        ) -> Callable[[Iterable[str | E]], list[E]]:
            """Create validator for list of enums."""

            def _coerce(value: Iterable[str | E]) -> list[E]:
                if not isinstance(value, (list, tuple, set)):
                    msg = "Expected sequence"
                    raise TypeError(msg)
                result = []
                for i, item in enumerate(value):
                    if isinstance(item, enum_cls):
                        result.append(item)
                    elif isinstance(item, str):
                        try:
                            result.append(enum_cls(item))
                        except ValueError as err:
                            msg = f"Invalid at [{i}]: {item!r}"
                            raise ValueError(msg) from err
                    else:
                        msg = f"Expected str at [{i}]"
                        raise TypeError(msg)
                return result

            return _coerce

    class Args:
        """@validated, parse_kwargs - ZERO boilerplate de validação."""

        @staticmethod
        def validated[P, R](func: Callable[P, R]) -> Callable[P, R]:
            """Decorator com validate_call - aceita str OU enum, converte auto."""
            return validate_call(
                config=ConfigDict(arbitrary_types_allowed=True, use_enum_values=False),
                validate_return=False,
            )(func)

        @staticmethod
        def validated_with_result[P, R](
            func: Callable[P, r[R]],
        ) -> Callable[P, r[R]]:
            """ValidationError → r.fail()."""

            @wraps(func)
            def wrapper(*args: object, **kwargs: object) -> r[R]:
                try:
                    return validate_call(
                        config=ConfigDict(arbitrary_types_allowed=True),
                        validate_return=False,
                    )(func)(*args, **kwargs)
                except Exception as e:
                    return r.fail(str(e))

            return wrapper

        @staticmethod
        def parse_kwargs[E: StrEnum](
            kwargs: Mapping[str, t.JsonValue],
            enum_fields: Mapping[str, type[E]],
        ) -> r[dict[str, t.JsonValue]]:
            """Parse kwargs with enum fields."""
            parsed, errors = dict(kwargs), []
            for field, enum_cls in enum_fields.items():
                if field in parsed and isinstance(parsed[field], str):
                    try:
                        parsed[field] = enum_cls(parsed[field])
                    except ValueError:
                        errors.append(f"{field}: '{parsed[field]}'")
            return r.fail(f"Invalid: {errors}") if errors else r.ok(parsed)

        @staticmethod
        def get_enum_params(func: Callable[..., object]) -> dict[str, type[StrEnum]]:
            """Extrai parâmetros StrEnum da signature."""
            try:
                hints = get_type_hints(func)
            except Exception:
                return {}
            return {
                n: h
                for n, h in hints.items()
                if n != "return" and isinstance(h, type) and issubclass(h, StrEnum)
            }

    class Model:
        """from_dict, merge_defaults, update - ZERO try/except."""

        @staticmethod
        def from_dict[M: BaseModel](
            model_cls: type[M],
            data: Mapping[str, t.JsonValue],
            *,
            strict: bool = False,
        ) -> r[M]:
            """Create model from dict."""
            try:
                return r.ok(model_cls.model_validate(data, strict=strict))
            except Exception as e:
                return r.fail(f"Validation failed: {e}")

        @staticmethod
        def merge_defaults[M: BaseModel](
            model_cls: type[M],
            defaults: Mapping[str, t.JsonValue],
            overrides: Mapping[str, t.JsonValue],
        ) -> r[M]:
            """Merge defaults with overrides."""
            return FlextDbtLdapUtilities.Model.from_dict(
                model_cls,
                {**defaults, **overrides},
            )

        @staticmethod
        def update[M: BaseModel](instance: M, **updates: t.JsonValue) -> r[M]:
            """Update model instance."""
            try:
                current = instance.model_dump()
                current.update(updates)
                return r.ok(type(instance).model_validate(current))
            except Exception as e:
                return r.fail(f"Update failed: {e}")

    class Pydantic:
        """Fábricas de Annotated types."""

        @staticmethod
        def coerced_enum[E: StrEnum](enum_cls: type[E]) -> type:
            """Create coerced enum type."""
            return Annotated[
                enum_cls,
                BeforeValidator(FlextDbtLdapUtilities.Enum.coerce_validator(enum_cls)),
            ]


__all__ = ["FlextDbtLdapUtilities"]
