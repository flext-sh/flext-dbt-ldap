"""FLEXT DBT LDAP Utilities - Complete DBT LDAP Integration Utilities.

Copyright (c) 2025 FLEXT Contributors
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Mapping, MutableMapping, MutableSequence, Sequence
from pathlib import Path

from flext_core import r
from flext_dbt_ldap import c, m, t
from flext_ldap import FlextLdapUtilities
from flext_meltano import FlextMeltanoUtilities


class FlextDbtLdapUtilities(FlextMeltanoUtilities, FlextLdapUtilities):
    """Unified DBT LDAP utilities service extending u."""

    class DbtLdap:
        """DBT project management utilities."""

        @staticmethod
        def create_dbt_project_config(
            project_name: str,
            ldap_sources: Sequence[m.DbtLdap.DbtSourceTable],
            target_schema: str = "ldap_transformed",
        ) -> r[m.DbtLdap.DbtProjectConfig]:
            """Create DBT project configuration for LDAP data transformation."""
            try:
                _ = ldap_sources
                project_config = m.DbtLdap.DbtProjectConfig(
                    name=project_name,
                    model_paths=["models"],
                    analysis_paths=["analyses"],
                    test_paths=["tests"],
                    seed_paths=["seeds"],
                    macro_paths=["macros"],
                    snapshot_paths=["snapshots"],
                    clean_targets=["target", "dbt_packages"],
                    profile=f"{project_name}_profile",
                    target_schema=target_schema,
                    tags=["ldap", "transformation"],
                )
                return r[m.DbtLdap.DbtProjectConfig].ok(project_config)
            except c.Meltano.Singer.SAFE_EXCEPTIONS as e:
                return r[m.DbtLdap.DbtProjectConfig].fail(
                    f"DBT project config creation failed: {e}",
                )

        @staticmethod
        def generate_dbt_profiles(
            profile_name: str,
            connection_config: m.DbtLdap.DbtProfileConfig,
        ) -> r[m.DbtLdap.DbtProfileConfig]:
            """Generate DBT profiles configuration for LDAP data sources."""
            try:
                _ = profile_name
                return r[m.DbtLdap.DbtProfileConfig].ok(connection_config)
            except c.Meltano.Singer.SAFE_EXCEPTIONS as e:
                return r[m.DbtLdap.DbtProfileConfig].fail(
                    f"DBT profiles generation failed: {e}",
                )

        @staticmethod
        def validate_dbt_project_structure(
            project_path: Path,
        ) -> r[m.DbtLdap.ProjectStructureValidation]:
            """Validate DBT project structure for LDAP transformation project."""
            try:
                required_files = {
                    "dbt_project.yml": project_path / "dbt_project.yml",
                    "profiles.yml": project_path / "profiles.yml",
                    "models_dir": project_path / "models",
                    "macros_dir": project_path / "macros",
                    "tests_dir": project_path / "tests",
                }
                results: MutableMapping[str, bool] = {}
                for name, path in required_files.items():
                    results[name] = path.exists()
                return r[m.DbtLdap.ProjectStructureValidation].ok(
                    m.DbtLdap.ProjectStructureValidation(results=results),
                )
            except c.Meltano.Singer.SAFE_EXCEPTIONS as e:
                return r[m.DbtLdap.ProjectStructureValidation].fail(
                    f"DBT project structure validation failed: {e}",
                )

        class LdapDataTransformation:
            """LDAP data transformation utilities."""

            @staticmethod
            def create_ldap_transformation_model(
                model_name: str,
                source_table: str,
                transformations: t.StrMapping,
            ) -> r[str]:
                """Create DBT model SQL for LDAP data transformation."""
                try:
                    select_clauses: Sequence[str] = [
                        f"    {column}"
                        if transformation == "identity"
                        else f"    {transformation} as {column}"
                        for column, transformation in transformations.items()
                    ]
                    model_sql = "".join([
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
                except c.Meltano.Singer.SAFE_EXCEPTIONS as e:
                    return r[str].fail(
                        f"LDAP transformation model creation failed: {e}"
                    )

            @staticmethod
            def generate_ldap_data_tests(
                model_name: str,
                test_config: m.DbtLdap.DbtTestConfig,
            ) -> r[m.DbtLdap.DbtTestConfig]:
                """Generate DBT data tests for LDAP transformation models."""
                try:
                    column_tests: Sequence[Mapping[str, t.Serializable]] = [
                        {
                            "name": col,
                            "description": f"Tests for {col} column",
                            "tests": col_tests,
                        }
                        for col, col_tests in test_config.columns.items()
                    ]
                    serializable_columns: Sequence[t.Serializable] = list(column_tests)
                    model_entry: Mapping[str, t.Serializable] = {
                        "name": model_name,
                        "description": f"Data tests for {model_name} LDAP model",
                        "tests": ["unique", "not_null"],
                        "columns": serializable_columns,
                    }
                    tests = m.DbtLdap.DbtTestConfig(
                        columns={},
                        models=[model_entry],
                    )
                    return r[m.DbtLdap.DbtTestConfig].ok(tests)
                except c.Meltano.Singer.SAFE_EXCEPTIONS as e:
                    return r[m.DbtLdap.DbtTestConfig].fail(
                        f"LDAP data tests generation failed: {e}",
                    )

            @staticmethod
            def generate_ldap_source_schema(
                ldap_attributes: t.StrSequence,
                source_name: str = "ldap_users",
            ) -> r[m.DbtLdap.DbtSourceSchema]:
                """Generate DBT source schema for LDAP attributes."""
                try:
                    columns: Sequence[t.StrMapping] = [
                        {
                            "name": attr.lower().replace("-", "_"),
                            "description": f"LDAP {attr} attribute",
                            "data_type": (
                                c.DbtLdap.DataTypes.TIMESTAMP
                                if attr.lower()
                                in set(c.DbtLdap.DataTypes.TIMESTAMP_ATTRS)
                                else c.DbtLdap.DataTypes.TEXT_ARRAY
                                if attr.lower() in set(c.DbtLdap.DataTypes.ARRAY_ATTRS)
                                else c.DbtLdap.DataTypes.INTEGER
                                if attr.lower()
                                in set(c.DbtLdap.DataTypes.INTEGER_ATTRS)
                                else c.DbtLdap.DataTypes.TEXT
                            ),
                        }
                        for attr in ldap_attributes
                    ]
                    serializable_cols: Sequence[t.Serializable] = list(columns)
                    table_entry: Mapping[str, t.Serializable] = {
                        "name": source_name,
                        "description": f"LDAP {source_name} data",
                        "columns": serializable_cols,
                    }
                    source_entry: Mapping[str, t.Serializable] = {
                        "name": "ldap",
                        "description": "LDAP directory data source",
                        "tables": [table_entry],
                    }
                    source_schema = m.DbtLdap.DbtSourceSchema(sources=[source_entry])
                    return r[m.DbtLdap.DbtSourceSchema].ok(source_schema)
                except c.Meltano.Singer.SAFE_EXCEPTIONS as e:
                    return r[m.DbtLdap.DbtSourceSchema].fail(
                        f"LDAP source schema generation failed: {e}",
                    )

        class MacroManagement:
            """DBT macro management utilities for LDAP operations."""

            @staticmethod
            def create_ldap_attribute_macro(
                macro_name: str = "extract_ldap_attribute",
            ) -> r[str]:
                """Create DBT macro for extracting LDAP attributes from arrays."""
                try:
                    macro_sql = "".join([
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
                except c.Meltano.Singer.SAFE_EXCEPTIONS as e:
                    return r[str].fail(f"LDAP attribute macro creation failed: {e}")

            @staticmethod
            def create_ldap_normalization_macro(
                macro_name: str = "normalize_ldap_timestamp",
            ) -> r[str]:
                """Create DBT macro for normalizing LDAP timestamps."""
                try:
                    macro_sql = f"-- Macro to normalize LDAP timestamps to standard format\n{{% macro {macro_name}(timestamp_column) %}}\n case\n when {{{{{{timestamp_column}}}}}} is null then null\n when length({{{{{{timestamp_column}}}}}}) = 14 then\n -- LDAP GeneralizedTime format: YYYYMMDDHHMMSSZ\n to_timestamp(\n substring({{{{{{timestamp_column}}}}}} from 1 for 14),\n 'YYYYMMDDHH24MISS'\n )\n else\n -- Try to parse as standard timestamp\n try_cast({{{{{{timestamp_column}}}}}} as timestamp)\n end\n{{% endmacro %}}"
                    return r[str].ok(macro_sql)
                except c.Meltano.Singer.SAFE_EXCEPTIONS as e:
                    return r[str].fail(f"LDAP normalization macro creation failed: {e}")

            @staticmethod
            def create_ldap_parsing_macro(macro_name: str = "parse_ldap_dn") -> r[str]:
                """Create DBT macro for parsing LDAP distinguished names."""
                try:
                    macro_sql = f"""-- Macro to parse LDAP Distinguished Name (DN) components\n{{% macro {macro_name}(dn_column, component='cn') %}}\n    case\n        when {{{{{{dn_column}}}}}} is null then null\n        when position('{{{{{{component}}}}}}=' in lower({{{{{{dn_column}}}}}}) = 0 then null\n        else trim(both '"' from\n            split_part(\n                split_part(\n                    lower({{{{{{dn_column}}}}}}),\n                    '{{{{{{component}}}}}}=',\n                    2\n                ),\n                ',',\n                1\n            )\n        )\n    end\n{{% endmacro %}}"""
                    return r[str].ok(macro_sql)
                except c.Meltano.Singer.SAFE_EXCEPTIONS as e:
                    return r[str].fail(f"LDAP parsing macro creation failed: {e}")

        class SchemaGeneration:
            """Schema generation utilities for LDAP data structures."""

            @staticmethod
            def generate_group_schema() -> r[m.DbtLdap.DbtModelDefinition]:
                """Generate standard schema for LDAP group data."""
                try:
                    group_schema = m.DbtLdap.DbtModelDefinition(
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
                                    {
                                        "name": "group_type",
                                        "description": "Type of group",
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
                    )
                    return r[m.DbtLdap.DbtModelDefinition].ok(group_schema)
                except c.Meltano.Singer.SAFE_EXCEPTIONS as e:
                    return r[m.DbtLdap.DbtModelDefinition].fail(
                        f"Group schema generation failed: {e}",
                    )

            @staticmethod
            def generate_user_schema() -> r[m.DbtLdap.DbtModelDefinition]:
                """Generate standard schema for LDAP user data."""
                try:
                    user_schema = m.DbtLdap.DbtModelDefinition(
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
                    return r[m.DbtLdap.DbtModelDefinition].ok(user_schema)
                except c.Meltano.Singer.SAFE_EXCEPTIONS as e:
                    return r[m.DbtLdap.DbtModelDefinition].fail(
                        f"User schema generation failed: {e}",
                    )

        class TransformationOptimization:
            """Transformation optimization utilities."""

            @classmethod
            def analyze_transformation_performance(
                cls,
                model_stats: m.DbtLdap.PerformanceAnalysis,
            ) -> r[m.DbtLdap.PerformanceAnalysis]:
                """Analyze performance of LDAP transformation models."""
                try:
                    recommendations: MutableSequence[str] = []
                    if (
                        model_stats.execution_time
                        > c.DbtLdap.TransformationOptimization.PERFORMANCE_EXECUTION_TIME_THRESHOLD
                    ):
                        recommendations.append(
                            "Consider adding indexes or partitioning for large datasets",
                        )
                    if (
                        model_stats.memory_usage
                        > c.DbtLdap.TransformationOptimization.PERFORMANCE_MEMORY_USAGE_THRESHOLD
                    ):
                        recommendations.append(
                            "Consider processing data in smaller batches",
                        )
                    if (
                        model_stats.rows_processed
                        > c.DbtLdap.TransformationOptimization.PERFORMANCE_ROWS_PROCESSED_THRESHOLD
                    ):
                        recommendations.append(
                            "Consider incremental processing for large datasets",
                        )
                    analysis = m.DbtLdap.PerformanceAnalysis(
                        execution_time=model_stats.execution_time,
                        rows_processed=model_stats.rows_processed,
                        memory_usage=model_stats.memory_usage,
                        recommendations=recommendations,
                    )
                    return r[m.DbtLdap.PerformanceAnalysis].ok(analysis)
                except c.Meltano.Singer.SAFE_EXCEPTIONS as e:
                    return r[m.DbtLdap.PerformanceAnalysis].fail(
                        f"Performance analysis failed: {e}",
                    )

            @staticmethod
            def optimize_ldap_query(
                base_query: str,
                optimization_hints: m.DbtLdap.OptimizationHints,
            ) -> r[str]:
                """Optimize DBT SQL query for LDAP data processing."""
                try:
                    optimized_query = base_query
                    if optimization_hints.add_indexes:
                        for column in optimization_hints.index_columns:
                            optimized_query = f"-- Consider adding index on {column}\n{optimized_query}"
                    if optimization_hints.partition_by:
                        optimized_query = f"{optimized_query}\n-- Consider partitioning by {optimization_hints.partition_by}"
                    if optimization_hints.filter_early:
                        optimized_query = optimized_query.replace(
                            "where 1=1",
                            "where 1=1\n    -- Apply filters early for performance",
                        )
                    return r[str].ok(optimized_query)
                except c.Meltano.Singer.SAFE_EXCEPTIONS as e:
                    return r[str].fail(f"Query optimization failed: {e}")


__all__ = ["FlextDbtLdapUtilities", "u"]

u = FlextDbtLdapUtilities
