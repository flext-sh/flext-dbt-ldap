"""DBT LDAP protocols for FLEXT ecosystem.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import (
    Sequence,
)
from typing import Protocol, runtime_checkable

from flext_dbt_ldap import m, t
from flext_ldap import FlextLdapProtocols
from flext_meltano import p


class FlextDbtLdapProtocols(p, FlextLdapProtocols):
    """DBT LDAP protocols extending LDAP and Meltano protocols."""

    class DbtLdap:
        """DBT domain protocols."""

        @runtime_checkable
        class DataFrameLike(Protocol):
            """Protocol for DataFrame-like objects used in DBT Python models."""

            def __len__(self) -> int:
                """Return the number of rows in the DataFrame."""
                ...

        class Ldap:
            """DBT LDAP domain protocols."""

            @runtime_checkable
            class Dbt(p.Service[m.DbtLdap.DbtRunStatus], Protocol):
                """Protocol for DBT operations with LDAP data."""

                def compile_dbt_models(
                    self,
                    models: t.StrSequence | None = None,
                    settings: m.DbtLdap.DbtConfig | None = None,
                ) -> p.Result[m.DbtLdap.DbtRunStatus]:
                    """Compile DBT models for LDAP data processing."""
                    ...

                def get_dbt_manifest(
                    self,
                ) -> p.Result[m.DbtLdap.DbtProjectConfig]:
                    """Get DBT manifest with LDAP model definitions."""
                    ...

                def run_dbt_models(
                    self,
                    models: t.ScalarList | None = None,
                    settings: m.DbtLdap.DbtConfig | None = None,
                ) -> p.Result[m.DbtLdap.DbtRunStatus]:
                    """Run DBT models with LDAP data sources."""
                    ...

                def test_dbt_models(
                    self,
                    models: t.ScalarList | None = None,
                    settings: m.DbtLdap.DbtConfig | None = None,
                ) -> p.Result[m.DbtLdap.DbtRunStatus]:
                    """Test DBT models with LDAP data validation."""
                    ...

                def validate_dbt_project(
                    self,
                    project_path: str,
                ) -> p.Result[bool]:
                    """Validate DBT project configuration."""
                    ...

            @runtime_checkable
            class LdapIntegration(
                p.Service[m.DbtLdap.DbtLdapPipelineResult],
                Protocol,
            ):
                """LDAP integration protocol for dbt LDAP operations."""

                def extract_ldap_data(
                    self,
                    ldap_config: m.DbtLdap.LdapQuery,
                    extraction_config: m.DbtLdap.TransformationConfig,
                ) -> p.Result[Sequence[m.DbtLdap.UserDimension]]:
                    """Extract data from LDAP directory for DBT processing."""
                    ...

                def sync_ldap_to_warehouse(
                    self,
                    ldap_data: Sequence[m.DbtLdap.UserDimension],
                    warehouse_config: m.DbtLdap.DbtConfig,
                ) -> p.Result[m.DbtLdap.DbtRunStatus]:
                    """Sync LDAP data to data warehouse."""
                    ...

                def transform_ldap_to_dbt_format(
                    self,
                    ldap_data: Sequence[m.DbtLdap.UserDimension],
                    transformation_config: m.DbtLdap.TransformationConfig,
                ) -> p.Result[Sequence[m.DbtLdap.UserDimension]]:
                    """Transform LDAP data to DBT-compatible format."""
                    ...

                def validate_ldap_data_quality(
                    self,
                    data: Sequence[m.DbtLdap.UserDimension],
                    quality_rules: m.DbtLdap.DataValidationConfig,
                ) -> p.Result[m.DbtLdap.ValidationMetrics]:
                    """Validate LDAP data quality for DBT processing."""
                    ...

            @runtime_checkable
            class Modeling(
                p.Service[m.DbtLdap.DbtModelDefinition],
                Protocol,
            ):
                """Protocol for LDAP data modeling operations."""

                def create_group_dimension(
                    self,
                    ldap_groups: Sequence[m.DbtLdap.GroupDimension],
                    dimension_config: m.DbtLdap.DbtModelDefinition,
                ) -> p.Result[m.DbtLdap.DbtModelDefinition]:
                    """Create group dimension model from LDAP group data."""
                    ...

                def create_organizational_hierarchy(
                    self,
                    ldap_data: Sequence[m.DbtLdap.UserDimension],
                    hierarchy_config: m.DbtLdap.DbtModelDefinition,
                ) -> p.Result[m.DbtLdap.DbtModelDefinition]:
                    """Create organizational hierarchy from LDAP OUs."""
                    ...

                def create_user_dimension(
                    self,
                    ldap_users: Sequence[m.DbtLdap.UserDimension],
                    dimension_config: m.DbtLdap.DbtModelDefinition,
                ) -> p.Result[m.DbtLdap.DbtModelDefinition]:
                    """Create user dimension model from LDAP user data."""
                    ...

                def generate_fact_tables(
                    self,
                    dimensions: Sequence[m.DbtLdap.DbtModelDefinition],
                    fact_config: m.DbtLdap.DbtModelDefinition,
                ) -> p.Result[Sequence[m.DbtLdap.DbtModelDefinition]]:
                    """Generate fact tables from LDAP dimensions."""
                    ...

            @runtime_checkable
            class Transformation(
                p.Service[m.DbtLdap.UserDimension],
                Protocol,
            ):
                """Protocol for LDAP data transformation operations."""

                def apply_business_rules(
                    self,
                    data: Sequence[m.DbtLdap.UserDimension],
                    business_rules: m.DbtLdap.TransformationRule,
                ) -> p.Result[Sequence[m.DbtLdap.UserDimension]]:
                    """Apply business rules to LDAP data transformations."""
                    ...

                def enrich_ldap_data(
                    self,
                    ldap_data: Sequence[m.DbtLdap.UserDimension],
                    enrichment_sources: Sequence[m.DbtLdap.UserDimension],
                ) -> p.Result[Sequence[m.DbtLdap.UserDimension]]:
                    """Enrich LDAP data with additional data sources."""
                    ...

                def generate_derived_attributes(
                    self,
                    ldap_data: Sequence[m.DbtLdap.UserDimension],
                    derivation_config: m.DbtLdap.TransformationConfig,
                ) -> p.Result[Sequence[m.DbtLdap.UserDimension]]:
                    """Generate derived attributes from LDAP base attributes."""
                    ...

                def normalize_ldap_attributes(
                    self,
                    ldap_entries: Sequence[m.DbtLdap.UserDimension],
                    normalization_rules: m.DbtLdap.TransformationRule,
                ) -> p.Result[Sequence[m.DbtLdap.UserDimension]]:
                    """Normalize LDAP attributes for consistent processing."""
                    ...

            @runtime_checkable
            class Macro(p.Service[str], Protocol):
                """Protocol for DBT macro operations with LDAP data."""

                def create_ldap_snapshot_macro(
                    self,
                    snapshot_config: m.DbtLdap.DbtConfig,
                ) -> p.Result[str]:
                    """Create DBT snapshot macro for LDAP data versioning."""
                    ...

                def create_ldap_test_macro(
                    self,
                    test_config: m.DbtLdap.DbtTestConfig,
                ) -> p.Result[str]:
                    """Create DBT test macro for LDAP data validation."""
                    ...

                def generate_ldap_source_macro(
                    self,
                    source_config: m.DbtLdap.DbtSourceDefinition,
                ) -> p.Result[str]:
                    """Generate DBT macro for LDAP data sources."""
                    ...

                def generate_ldap_transformation_macro(
                    self,
                    transformation_config: m.DbtLdap.TransformationConfig,
                ) -> p.Result[str]:
                    """Generate DBT transformation macro for LDAP data."""
                    ...

            @runtime_checkable
            class Quality(p.Service[m.DbtLdap.ValidationMetrics], Protocol):
                """Protocol for LDAP data quality operations."""

                def check_data_completeness(
                    self,
                    data: Sequence[m.DbtLdap.UserDimension],
                    completeness_config: m.DbtLdap.DataValidationConfig,
                ) -> p.Result[m.DbtLdap.ValidationMetrics]:
                    """Check LDAP data completeness for DBT processing."""
                    ...

                def detect_data_anomalies(
                    self,
                    data: Sequence[m.DbtLdap.UserDimension],
                    anomaly_config: m.DbtLdap.DataValidationConfig,
                ) -> p.Result[Sequence[m.DbtLdap.UserDimension]]:
                    """Detect anomalies in LDAP data."""
                    ...

                def generate_quality_report(
                    self,
                    quality_results: Sequence[m.DbtLdap.ValidationMetrics],
                    report_config: m.DbtLdap.DbtConfig,
                ) -> p.Result[m.DbtLdap.DbtRunStatus]:
                    """Generate data quality report."""
                    ...

                def validate_ldap_schema_compliance(
                    self,
                    ldap_data: Sequence[m.DbtLdap.UserDimension],
                    schema_rules: m.DbtLdap.LdapSchema,
                ) -> p.Result[m.DbtLdap.ValidationMetrics]:
                    """Validate LDAP data against schema compliance rules."""
                    ...

            @runtime_checkable
            class Performance(
                p.Service[m.DbtLdap.PerformanceAnalysis],
                Protocol,
            ):
                """Protocol for DBT LDAP performance optimization."""

                def cache_ldap_extractions(
                    self,
                    extraction_config: m.DbtLdap.TransformationConfig,
                    cache_config: m.DbtLdap.DbtConfig,
                ) -> p.Result[bool]:
                    """Cache LDAP data extractions."""
                    ...

                def monitor_dbt_performance(
                    self,
                    run_results: m.DbtLdap.DbtRunStatus,
                ) -> p.Result[m.DbtLdap.PerformanceAnalysis]:
                    """Monitor DBT performance."""
                    ...

                def optimize_dbt_models(
                    self,
                    model_config: m.DbtLdap.DbtProjectConfig,
                    performance_metrics: m.DbtLdap.PerformanceAnalysis,
                ) -> p.Result[m.DbtLdap.DbtProjectConfig]:
                    """Optimize DBT models for performance."""
                    ...

                def optimize_ldap_queries(
                    self,
                    query_config: m.DbtLdap.LdapQuery,
                ) -> p.Result[m.DbtLdap.LdapQuery]:
                    """Optimize LDAP queries for DBT data extraction."""
                    ...

            @runtime_checkable
            class Monitoring(p.Service[m.DbtLdap.DbtRunStatus], Protocol):
                """Protocol for DBT LDAP monitoring operations."""

                def create_monitoring_dashboard(
                    self,
                    dashboard_config: m.DbtLdap.DbtConfig,
                ) -> p.Result[m.DbtLdap.DbtRunStatus]:
                    """Create monitoring dashboard."""
                    ...

                def get_health_status(
                    self,
                ) -> p.Result[m.DbtLdap.ServiceStatus]:
                    """Get DBT LDAP integration health status."""
                    ...

                def monitor_ldap_data_freshness(
                    self,
                    freshness_config: m.DbtLdap.DbtSourceFreshness,
                ) -> p.Result[m.DbtLdap.DbtSourceFreshness]:
                    """Monitor LDAP data freshness."""
                    ...

                def track_dbt_run_metrics(
                    self,
                    run_id: str,
                    metrics: m.DbtLdap.PerformanceAnalysis,
                ) -> p.Result[bool]:
                    """Track DBT run metrics."""
                    ...


__all__: list[str] = ["FlextDbtLdapProtocols", "p"]

p = FlextDbtLdapProtocols
