"""DBT LDAP protocols for FLEXT ecosystem.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Protocol, runtime_checkable

from flext_dbt_ldap import m, t
from flext_ldap import FlextLdapProtocols
from flext_meltano import FlextMeltanoProtocols


class FlextDbtLdapProtocols(FlextMeltanoProtocols, FlextLdapProtocols):
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
            class Dbt(FlextMeltanoProtocols.Service[m.DbtLdap.DbtRunStatus], Protocol):
                """Protocol for DBT operations with LDAP data."""

                def compile_dbt_models(
                    self,
                    models: t.StrSequence | None = None,
                    config: m.DbtLdap.DbtConfig | None = None,
                ) -> FlextMeltanoProtocols.Result[m.DbtLdap.DbtRunStatus]:
                    """Compile DBT models for LDAP data processing."""
                    ...

                def get_dbt_manifest(
                    self,
                ) -> FlextMeltanoProtocols.Result[m.DbtLdap.DbtProjectConfig]:
                    """Get DBT manifest with LDAP model definitions."""
                    ...

                def run_dbt_models(
                    self,
                    models: t.ScalarList | None = None,
                    config: m.DbtLdap.DbtConfig | None = None,
                ) -> FlextMeltanoProtocols.Result[m.DbtLdap.DbtRunStatus]:
                    """Run DBT models with LDAP data sources."""
                    ...

                def test_dbt_models(
                    self,
                    models: t.ScalarList | None = None,
                    config: m.DbtLdap.DbtConfig | None = None,
                ) -> FlextMeltanoProtocols.Result[m.DbtLdap.DbtRunStatus]:
                    """Test DBT models with LDAP data validation."""
                    ...

                def validate_dbt_project(
                    self,
                    project_path: str,
                ) -> FlextMeltanoProtocols.Result[bool]:
                    """Validate DBT project configuration."""
                    ...

            @runtime_checkable
            class LdapIntegration(
                FlextMeltanoProtocols.Service[m.DbtLdap.DbtLdapPipelineResult],
                Protocol,
            ):
                """LDAP integration protocol for dbt LDAP operations."""

                def extract_ldap_data(
                    self,
                    ldap_config: m.DbtLdap.LdapQuery,
                    extraction_config: m.DbtLdap.TransformationConfig,
                ) -> FlextMeltanoProtocols.Result[Sequence[m.DbtLdap.UserDimension]]:
                    """Extract data from LDAP directory for DBT processing."""
                    ...

                def sync_ldap_to_warehouse(
                    self,
                    ldap_data: Sequence[m.DbtLdap.UserDimension],
                    warehouse_config: m.DbtLdap.DbtConfig,
                ) -> FlextMeltanoProtocols.Result[m.DbtLdap.DbtRunStatus]:
                    """Sync LDAP data to data warehouse."""
                    ...

                def transform_ldap_to_dbt_format(
                    self,
                    ldap_data: Sequence[m.DbtLdap.UserDimension],
                    transformation_config: m.DbtLdap.TransformationConfig,
                ) -> FlextMeltanoProtocols.Result[Sequence[m.DbtLdap.UserDimension]]:
                    """Transform LDAP data to DBT-compatible format."""
                    ...

                def validate_ldap_data_quality(
                    self,
                    data: Sequence[m.DbtLdap.UserDimension],
                    quality_rules: m.DbtLdap.DataValidationConfig,
                ) -> FlextMeltanoProtocols.Result[m.DbtLdap.ValidationMetrics]:
                    """Validate LDAP data quality for DBT processing."""
                    ...

            @runtime_checkable
            class Modeling(
                FlextMeltanoProtocols.Service[m.DbtLdap.DbtModelDefinition],
                Protocol,
            ):
                """Protocol for LDAP data modeling operations."""

                def create_group_dimension(
                    self,
                    ldap_groups: Sequence[m.DbtLdap.GroupDimension],
                    dimension_config: m.DbtLdap.DbtModelDefinition,
                ) -> FlextMeltanoProtocols.Result[m.DbtLdap.DbtModelDefinition]:
                    """Create group dimension model from LDAP group data."""
                    ...

                def create_organizational_hierarchy(
                    self,
                    ldap_data: Sequence[m.DbtLdap.UserDimension],
                    hierarchy_config: m.DbtLdap.DbtModelDefinition,
                ) -> FlextMeltanoProtocols.Result[m.DbtLdap.DbtModelDefinition]:
                    """Create organizational hierarchy from LDAP OUs."""
                    ...

                def create_user_dimension(
                    self,
                    ldap_users: Sequence[m.DbtLdap.UserDimension],
                    dimension_config: m.DbtLdap.DbtModelDefinition,
                ) -> FlextMeltanoProtocols.Result[m.DbtLdap.DbtModelDefinition]:
                    """Create user dimension model from LDAP user data."""
                    ...

                def generate_fact_tables(
                    self,
                    dimensions: Sequence[m.DbtLdap.DbtModelDefinition],
                    fact_config: m.DbtLdap.DbtModelDefinition,
                ) -> FlextMeltanoProtocols.Result[
                    Sequence[m.DbtLdap.DbtModelDefinition]
                ]:
                    """Generate fact tables from LDAP dimensions."""
                    ...

            @runtime_checkable
            class Transformation(
                FlextMeltanoProtocols.Service[m.DbtLdap.UserDimension],
                Protocol,
            ):
                """Protocol for LDAP data transformation operations."""

                def apply_business_rules(
                    self,
                    data: Sequence[m.DbtLdap.UserDimension],
                    business_rules: m.DbtLdap.TransformationRule,
                ) -> FlextMeltanoProtocols.Result[Sequence[m.DbtLdap.UserDimension]]:
                    """Apply business rules to LDAP data transformations."""
                    ...

                def enrich_ldap_data(
                    self,
                    ldap_data: Sequence[m.DbtLdap.UserDimension],
                    enrichment_sources: Sequence[m.DbtLdap.UserDimension],
                ) -> FlextMeltanoProtocols.Result[Sequence[m.DbtLdap.UserDimension]]:
                    """Enrich LDAP data with additional data sources."""
                    ...

                def generate_derived_attributes(
                    self,
                    ldap_data: Sequence[m.DbtLdap.UserDimension],
                    derivation_config: m.DbtLdap.TransformationConfig,
                ) -> FlextMeltanoProtocols.Result[Sequence[m.DbtLdap.UserDimension]]:
                    """Generate derived attributes from LDAP base attributes."""
                    ...

                def normalize_ldap_attributes(
                    self,
                    ldap_entries: Sequence[m.DbtLdap.UserDimension],
                    normalization_rules: m.DbtLdap.TransformationRule,
                ) -> FlextMeltanoProtocols.Result[Sequence[m.DbtLdap.UserDimension]]:
                    """Normalize LDAP attributes for consistent processing."""
                    ...

            @runtime_checkable
            class Macro(FlextMeltanoProtocols.Service[str], Protocol):
                """Protocol for DBT macro operations with LDAP data."""

                def create_ldap_snapshot_macro(
                    self,
                    snapshot_config: m.DbtLdap.DbtConfig,
                ) -> FlextMeltanoProtocols.Result[str]:
                    """Create DBT snapshot macro for LDAP data versioning."""
                    ...

                def create_ldap_test_macro(
                    self,
                    test_config: m.DbtLdap.DbtTestConfig,
                ) -> FlextMeltanoProtocols.Result[str]:
                    """Create DBT test macro for LDAP data validation."""
                    ...

                def generate_ldap_source_macro(
                    self,
                    source_config: m.DbtLdap.DbtSourceDefinition,
                ) -> FlextMeltanoProtocols.Result[str]:
                    """Generate DBT macro for LDAP data sources."""
                    ...

                def generate_ldap_transformation_macro(
                    self,
                    transformation_config: m.DbtLdap.TransformationConfig,
                ) -> FlextMeltanoProtocols.Result[str]:
                    """Generate DBT transformation macro for LDAP data."""
                    ...

            @runtime_checkable
            class Quality(
                FlextMeltanoProtocols.Service[m.DbtLdap.ValidationMetrics], Protocol
            ):
                """Protocol for LDAP data quality operations."""

                def check_data_completeness(
                    self,
                    data: Sequence[m.DbtLdap.UserDimension],
                    completeness_config: m.DbtLdap.DataValidationConfig,
                ) -> FlextMeltanoProtocols.Result[m.DbtLdap.ValidationMetrics]:
                    """Check LDAP data completeness for DBT processing."""
                    ...

                def detect_data_anomalies(
                    self,
                    data: Sequence[m.DbtLdap.UserDimension],
                    anomaly_config: m.DbtLdap.DataValidationConfig,
                ) -> FlextMeltanoProtocols.Result[Sequence[m.DbtLdap.UserDimension]]:
                    """Detect anomalies in LDAP data."""
                    ...

                def generate_quality_report(
                    self,
                    quality_results: Sequence[m.DbtLdap.ValidationMetrics],
                    report_config: m.DbtLdap.DbtConfig,
                ) -> FlextMeltanoProtocols.Result[m.DbtLdap.DbtRunStatus]:
                    """Generate data quality report."""
                    ...

                def validate_ldap_schema_compliance(
                    self,
                    ldap_data: Sequence[m.DbtLdap.UserDimension],
                    schema_rules: m.DbtLdap.LdapSchema,
                ) -> FlextMeltanoProtocols.Result[m.DbtLdap.ValidationMetrics]:
                    """Validate LDAP data against schema compliance rules."""
                    ...

            @runtime_checkable
            class Performance(
                FlextMeltanoProtocols.Service[m.DbtLdap.PerformanceAnalysis],
                Protocol,
            ):
                """Protocol for DBT LDAP performance optimization."""

                def cache_ldap_extractions(
                    self,
                    extraction_config: m.DbtLdap.TransformationConfig,
                    cache_config: m.DbtLdap.DbtConfig,
                ) -> FlextMeltanoProtocols.Result[bool]:
                    """Cache LDAP data extractions."""
                    ...

                def monitor_dbt_performance(
                    self,
                    run_results: m.DbtLdap.DbtRunStatus,
                ) -> FlextMeltanoProtocols.Result[m.DbtLdap.PerformanceAnalysis]:
                    """Monitor DBT performance."""
                    ...

                def optimize_dbt_models(
                    self,
                    model_config: m.DbtLdap.DbtProjectConfig,
                    performance_metrics: m.DbtLdap.PerformanceAnalysis,
                ) -> FlextMeltanoProtocols.Result[m.DbtLdap.DbtProjectConfig]:
                    """Optimize DBT models for performance."""
                    ...

                def optimize_ldap_queries(
                    self,
                    query_config: m.DbtLdap.LdapQuery,
                ) -> FlextMeltanoProtocols.Result[m.DbtLdap.LdapQuery]:
                    """Optimize LDAP queries for DBT data extraction."""
                    ...

            @runtime_checkable
            class Monitoring(
                FlextMeltanoProtocols.Service[m.DbtLdap.DbtRunStatus], Protocol
            ):
                """Protocol for DBT LDAP monitoring operations."""

                def create_monitoring_dashboard(
                    self,
                    dashboard_config: m.DbtLdap.DbtConfig,
                ) -> FlextMeltanoProtocols.Result[m.DbtLdap.DbtRunStatus]:
                    """Create monitoring dashboard."""
                    ...

                def get_health_status(
                    self,
                ) -> FlextMeltanoProtocols.Result[m.DbtLdap.ServiceStatus]:
                    """Get DBT LDAP integration health status."""
                    ...

                def monitor_ldap_data_freshness(
                    self,
                    freshness_config: m.DbtLdap.DbtSourceFreshness,
                ) -> FlextMeltanoProtocols.Result[m.DbtLdap.DbtSourceFreshness]:
                    """Monitor LDAP data freshness."""
                    ...

                def track_dbt_run_metrics(
                    self,
                    run_id: str,
                    metrics: m.DbtLdap.PerformanceAnalysis,
                ) -> FlextMeltanoProtocols.Result[bool]:
                    """Track DBT run metrics."""
                    ...


__all__ = ["FlextDbtLdapProtocols", "p"]

p = FlextDbtLdapProtocols
