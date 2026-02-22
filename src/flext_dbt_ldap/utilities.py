"""FLEXT DBT LDAP Utilities - Complete DBT LDAP Integration Utilities.

Copyright (c) 2025 FLEXT Contributors
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from enum import StrEnum
from pathlib import Path
from typing import Annotated

from flext_core import r
from flext_core.container import FlextContainer
from flext_core.utilities import u
from pydantic import BeforeValidator

from flext_dbt_ldap.constants import c
from flext_dbt_ldap.models import FlextDbtLdapModels as m


class FlextDbtLdapUtilities(u):
    """Unified DBT LDAP utilities service extending u."""

    def __init__(self) -> None:
        """Initialize FlextDbtLdapUtilities service."""
        super().__init__()
        self._container = FlextContainer.get_global()

    def execute(self) -> r[m.ServiceStatus]:
        """Execute the main DBT LDAP service operation."""
        return r[m.ServiceStatus].ok(
            m.ServiceStatus(
                status="operational",
                service="flext-dbt-ldap-utilities",
                capabilities=[
                    "dbt_project_management",
                    "ldap_data_transformation",
                    "schema_generation",
                    "macro_management",
                    "dbt_model_validation",
                    "ldap_source_configuration",
                    "transformation_optimization",
                ],
            ),
        )

    class DbtLdap:
        """DBT project management utilities."""

        @staticmethod
        def create_dbt_project_config(
            project_name: str,
            ldap_sources: list[m.DbtSourceTable],
            target_schema: str = "ldap_transformed",
        ) -> r[m.DbtProjectConfig]:
            """Create DBT project configuration for LDAP data transformation."""
            try:
                _ = ldap_sources
                project_config = m.DbtProjectConfig(
                    name=project_name,
                    profile=f"{project_name}_profile",
                    target_schema=target_schema,
                    tags=["ldap", "transformation"],
                )
                return r[m.DbtProjectConfig].ok(project_config)
            except Exception as e:
                return r[m.DbtProjectConfig].fail(
                    f"DBT project config creation failed: {e}",
                )

        @staticmethod
        def generate_dbt_profiles(
            profile_name: str,
            connection_config: m.DbtProfileConfig,
        ) -> r[m.DbtProfileConfig]:
            """Generate DBT profiles configuration for LDAP data sources."""
            try:
                _ = profile_name
                return r[m.DbtProfileConfig].ok(connection_config)
            except Exception as e:
                return r[m.DbtProfileConfig].fail(
                    f"DBT profiles generation failed: {e}",
                )

        @staticmethod
        def validate_dbt_project_structure(
            project_path: Path,
        ) -> r[m.ProjectStructureValidation]:
            """Validate DBT project structure for LDAP transformation project."""
            try:
                required_files = {
                    "dbt_project.yml": project_path / "dbt_project.yml",
                    "profiles.yml": project_path / "profiles.yml",
                    "models_dir": project_path / "models",
                    "macros_dir": project_path / "macros",
                    "tests_dir": project_path / "tests",
                }
                results: dict[str, bool] = {}
                for name, path in required_files.items():
                    results[name] = path.exists()

                return r[m.ProjectStructureValidation].ok(
                    m.ProjectStructureValidation(results=results),
                )
            except Exception as e:
                return r[m.ProjectStructureValidation].fail(
                    f"DBT project structure validation failed: {e}",
                )

        class Collection(u.Collection):
            """Collection utilities extending u.Collection via inheritance."""

        class Args(u.Args):
            """Args utilities extending u.Args via inheritance."""

        class Model(u.Model):
            """Model utilities extending u.Model via inheritance."""

        class Pydantic:
            """Annotated type factories."""

            @staticmethod
            def coerced_enum[E: StrEnum](enum_cls: type[E]) -> object:
                """Create coerced enum type (Annotated wrapper)."""
                return Annotated[
                    enum_cls,
                    BeforeValidator(u.Enum.coerce_validator(enum_cls)),
                ]

    class LdapDataTransformation:
        """LDAP data transformation utilities."""

        @staticmethod
        def generate_ldap_source_schema(
            ldap_attributes: list[str],
            source_name: str = "ldap_users",
        ) -> r[m.DbtSourceSchema]:
            """Generate DBT source schema for LDAP attributes."""
            try:
                columns: list[dict[str, str]] = []
                for attr in ldap_attributes:
                    if attr.lower() in {"createtimestamp", "modifytimestamp"}:
                        data_type = "timestamp"
                    elif attr.lower() in {"memberof", "objectclass"}:
                        data_type = "text[]"
                    elif attr.lower() in {"uidnumber", "gidnumber"}:
                        data_type = "integer"
                    else:
                        data_type = "text"
                    columns.append({
                        "name": attr.lower().replace("-", "_"),
                        "description": f"LDAP {attr} attribute",
                        "data_type": data_type,
                    })

                source_schema = m.DbtSourceSchema(
                    sources=[
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
                )
                return r[m.DbtSourceSchema].ok(source_schema)
            except Exception as e:
                return r[m.DbtSourceSchema].fail(
                    f"LDAP source schema generation failed: {e}",
                )

        @staticmethod
        def create_ldap_transformation_model(
            model_name: str,
            source_table: str,
            transformations: dict[str, str],
        ) -> r[str]:
            """Create DBT model SQL for LDAP data transformation."""
            try:
                select_clauses: list[str] = []
                for column, transformation in transformations.items():
                    if transformation == "identity":
                        select_clauses.append(f"    {column}")
                    else:
                        select_clauses.append(f"    {transformation} as {column}")

                model_sql = "".join([  # nosec B608
                    "{{\n",
                    "    config(\n",
                    "        materialized='table',\n",
                    "        tags=['ldap', 'transformation'],\n",
                    f"        description=f'Transformed LDAP data for {model_name}'\n",
                    "    )\n",
                    "}}\n\n",
                    "select\n",
                    ",".join(select_clauses),
                    "\n",
                    f"from {{{{ source('ldap', '{source_table}') }}}}\n",
                    "where 1=1\n",
                    "    -- Add any filtering conditions here\n",
                    "    and objectclass is not null\n",
                ])
                return r[str].ok(model_sql)
            except Exception as e:
                return r[str].fail(
                    f"LDAP transformation model creation failed: {e}",
                )

        @staticmethod
        def generate_ldap_data_tests(
            model_name: str,
            test_config: m.DbtTestConfig,
        ) -> r[m.DbtTestConfig]:
            """Generate DBT data tests for LDAP transformation models."""
            try:
                tests = m.DbtTestConfig(
                    models=[
                        {
                            "name": model_name,
                            "description": f"Data tests for {model_name} LDAP model",
                            "tests": ["unique", "not_null"],
                            "columns": [],
                        },
                    ],
                )
                # Add column-specific tests from input config
                if test_config.columns and tests.models:
                    model_dict = tests.models[0]
                    if isinstance(model_dict, dict):  # pyright: ignore[reportUnnecessaryIsInstance]
                        columns_list = model_dict.get("columns")
                        if isinstance(columns_list, list):
                            for col, col_tests in test_config.columns.items():
                                columns_list.append({
                                    "name": col,
                                    "description": f"Tests for {col} column",
                                    "tests": col_tests,
                                })
                return r[m.DbtTestConfig].ok(tests)
            except Exception as e:
                return r[m.DbtTestConfig].fail(
                    f"LDAP data tests generation failed: {e}",
                )

    class MacroManagement:
        """DBT macro management utilities for LDAP operations."""

        @staticmethod
        def create_ldap_parsing_macro(
            macro_name: str = "parse_ldap_dn",
        ) -> r[str]:
            """Create DBT macro for parsing LDAP distinguished names."""
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
            """Create DBT macro for extracting LDAP attributes from arrays."""
            try:
                macro_sql = "".join([  # nosec B608
                    "-- Macro to extract specific values from LDAP multi-valued attributes\n",
                    f"{{% macro {macro_name}(attribute_array, filter_pattern='') %}}\n",
                    " case\n",
                    " when {{{{attribute_array}}}} is null then null\n",
                    " when array_length({{{{attribute_array}}}}, 1) = 0 then null\n",
                    " {% if filter_pattern %}\n",
                    " else (\n",
                    " select array_agg(attr)\n",
                    " from unnest({{{{attribute_array}}}}) as attr\n",
                    " where attr ilike '%{{{{filter_pattern}}}}%'\n",
                    " )[1]\n",
                    " {% else %}\n",
                    " else {{{{attribute_array}}}}[1]\n",
                    " {% endif %}\n",
                    " end\n",
                    "{% endmacro %}",
                ])
                return r[str].ok(macro_sql)
            except Exception as e:
                return r[str].fail(
                    f"LDAP attribute macro creation failed: {e}",
                )

        @staticmethod
        def create_ldap_normalization_macro(
            macro_name: str = "normalize_ldap_timestamp",
        ) -> r[str]:
            """Create DBT macro for normalizing LDAP timestamps."""
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
        def generate_user_schema() -> r[m.DbtModelDefinition]:
            """Generate standard schema for LDAP user data."""
            try:
                user_schema = m.DbtModelDefinition(
                    models=[
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
                                {"name": "manager", "description": "User manager"},
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
                )
                return r[m.DbtModelDefinition].ok(user_schema)
            except Exception as e:
                return r[m.DbtModelDefinition].fail(
                    f"User schema generation failed: {e}",
                )

        @staticmethod
        def generate_group_schema() -> r[m.DbtModelDefinition]:
            """Generate standard schema for LDAP group data."""
            try:
                group_schema = m.DbtModelDefinition(
                    models=[
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
                                {"name": "group_type", "description": "Type of group"},
                                {"name": "members", "description": "Group member list"},
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
                )
                return r[m.DbtModelDefinition].ok(group_schema)
            except Exception as e:
                return r[m.DbtModelDefinition].fail(
                    f"Group schema generation failed: {e}",
                )

    class TransformationOptimization:
        """Transformation optimization utilities."""

        @staticmethod
        def optimize_ldap_query(
            base_query: str,
            optimization_hints: m.OptimizationHints,
        ) -> r[str]:
            """Optimize DBT SQL query for LDAP data processing."""
            try:
                optimized_query = base_query
                if optimization_hints.add_indexes:
                    for column in optimization_hints.index_columns:
                        optimized_query = (
                            f"-- Consider adding index on {column}\n{optimized_query}"
                        )
                if optimization_hints.partition_by:
                    optimized_query = f"{optimized_query}\n-- Consider partitioning by {optimization_hints.partition_by}"
                if optimization_hints.filter_early:
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
            model_stats: m.PerformanceAnalysis,
        ) -> r[m.PerformanceAnalysis]:
            """Analyze performance of LDAP transformation models."""
            try:
                recommendations: list[str] = []
                if (
                    model_stats.execution_time
                    > c.TransformationOptimization.PERFORMANCE_EXECUTION_TIME_THRESHOLD
                ):
                    recommendations.append(
                        "Consider adding indexes or partitioning for large datasets",
                    )
                if (
                    model_stats.memory_usage
                    > c.TransformationOptimization.PERFORMANCE_MEMORY_USAGE_THRESHOLD
                ):
                    recommendations.append(
                        "Consider processing data in smaller batches",
                    )
                if (
                    model_stats.rows_processed
                    > c.TransformationOptimization.PERFORMANCE_ROWS_PROCESSED_THRESHOLD
                ):
                    recommendations.append(
                        "Consider incremental processing for large datasets",
                    )
                analysis = m.PerformanceAnalysis(
                    execution_time=model_stats.execution_time,
                    rows_processed=model_stats.rows_processed,
                    memory_usage=model_stats.memory_usage,
                    recommendations=recommendations,
                )
                return r[m.PerformanceAnalysis].ok(analysis)
            except Exception as e:
                return r[m.PerformanceAnalysis].fail(
                    f"Performance analysis failed: {e}",
                )


__all__ = ["FlextDbtLdapUtilities"]
