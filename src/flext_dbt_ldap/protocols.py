"""DBT LDAP protocols for FLEXT ecosystem.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, runtime_checkable

from flext_dbt_ldap import p
from flext_ldap import FlextLdapProtocols
from flext_meltano import p

if TYPE_CHECKING:
    from flext_dbt_ldap import t


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
            class Dbt(p.Service[p.DbtLdap.DbtRunStatus], Protocol):
                """Protocol for DBT operations with LDAP data."""

                def compile_dbt_models(
                    self,
                    models: t.StrSequence | None = None,
                    settings: p.DbtLdap.DbtConfig | None = None,
                ) -> p.Result[p.DbtLdap.DbtRunStatus]:
                    """Compile DBT models for LDAP data processing."""
                    ...

                def get_dbt_manifest(
                    self,
                ) -> p.Result[p.DbtLdap.DbtProjectConfig]:
                    """Get DBT manifest with LDAP model definitions."""
                    ...

                def run_dbt_models(
                    self,
                    models: t.ScalarList | None = None,
                    settings: p.DbtLdap.DbtConfig | None = None,
                ) -> p.Result[p.DbtLdap.DbtRunStatus]:
                    """Run DBT models with LDAP data sources."""
                    ...

                def test_dbt_models(
                    self,
                    models: t.ScalarList | None = None,
                    settings: p.DbtLdap.DbtConfig | None = None,
                ) -> p.Result[p.DbtLdap.DbtRunStatus]:
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
                p.Service[p.DbtLdap.DbtLdapPipelineResult],
                Protocol,
            ):
                """LDAP integration protocol for dbt LDAP operations."""

                def extract_ldap_data(
                    self,
                    ldap_config: p.DbtLdap.LdapQuery,
                    extraction_config: p.DbtLdap.TransformationConfig,
                ) -> p.Result[t.SequenceOf[p.DbtLdap.UserDimension]]:
                    """Extract data from LDAP directory for DBT processing."""
                    ...

                def sync_ldap_to_warehouse(
                    self,
                    ldap_data: t.SequenceOf[p.DbtLdap.UserDimension],
                    warehouse_config: p.DbtLdap.DbtConfig,
                ) -> p.Result[p.DbtLdap.DbtRunStatus]:
                    """Sync LDAP data to data warehouse."""
                    ...

                def transform_ldap_to_dbt_format(
                    self,
                    ldap_data: t.SequenceOf[p.DbtLdap.UserDimension],
                    transformation_config: p.DbtLdap.TransformationConfig,
                ) -> p.Result[t.SequenceOf[p.DbtLdap.UserDimension]]:
                    """Transform LDAP data to DBT-compatible format."""
                    ...

                def validate_ldap_data_quality(
                    self,
                    data: t.SequenceOf[p.DbtLdap.UserDimension],
                    quality_rules: p.DbtLdap.DataValidationConfig,
                ) -> p.Result[p.DbtLdap.ValidationMetrics]:
                    """Validate LDAP data quality for DBT processing."""
                    ...

            @runtime_checkable
            class Modeling(
                p.Service[p.DbtLdap.DbtModelDefinition],
                Protocol,
            ):
                """Protocol for LDAP data modeling operations."""

                def create_group_dimension(
                    self,
                    ldap_groups: t.SequenceOf[p.DbtLdap.GroupDimension],
                    dimension_config: p.DbtLdap.DbtModelDefinition,
                ) -> p.Result[p.DbtLdap.DbtModelDefinition]:
                    """Create group dimension model from LDAP group data."""
                    ...

                def create_organizational_hierarchy(
                    self,
                    ldap_data: t.SequenceOf[p.DbtLdap.UserDimension],
                    hierarchy_config: p.DbtLdap.DbtModelDefinition,
                ) -> p.Result[p.DbtLdap.DbtModelDefinition]:
                    """Create organizational hierarchy from LDAP OUs."""
                    ...

                def create_user_dimension(
                    self,
                    ldap_users: t.SequenceOf[p.DbtLdap.UserDimension],
                    dimension_config: p.DbtLdap.DbtModelDefinition,
                ) -> p.Result[p.DbtLdap.DbtModelDefinition]:
                    """Create user dimension model from LDAP user data."""
                    ...

                def generate_fact_tables(
                    self,
                    dimensions: t.SequenceOf[p.DbtLdap.DbtModelDefinition],
                    fact_config: p.DbtLdap.DbtModelDefinition,
                ) -> p.Result[t.SequenceOf[p.DbtLdap.DbtModelDefinition]]:
                    """Generate fact tables from LDAP dimensions."""
                    ...

            @runtime_checkable
            class Transformation(
                p.Service[p.DbtLdap.UserDimension],
                Protocol,
            ):
                """Protocol for LDAP data transformation operations."""

                def apply_business_rules(
                    self,
                    data: t.SequenceOf[p.DbtLdap.UserDimension],
                    business_rules: p.DbtLdap.TransformationRule,
                ) -> p.Result[t.SequenceOf[p.DbtLdap.UserDimension]]:
                    """Apply business rules to LDAP data transformations."""
                    ...

                def enrich_ldap_data(
                    self,
                    ldap_data: t.SequenceOf[p.DbtLdap.UserDimension],
                    enrichment_sources: t.SequenceOf[p.DbtLdap.UserDimension],
                ) -> p.Result[t.SequenceOf[p.DbtLdap.UserDimension]]:
                    """Enrich LDAP data with additional data sources."""
                    ...

                def generate_derived_attributes(
                    self,
                    ldap_data: t.SequenceOf[p.DbtLdap.UserDimension],
                    derivation_config: p.DbtLdap.TransformationConfig,
                ) -> p.Result[t.SequenceOf[p.DbtLdap.UserDimension]]:
                    """Generate derived attributes from LDAP base attributes."""
                    ...

                def normalize_ldap_attributes(
                    self,
                    ldap_entries: t.SequenceOf[p.DbtLdap.UserDimension],
                    normalization_rules: p.DbtLdap.TransformationRule,
                ) -> p.Result[t.SequenceOf[p.DbtLdap.UserDimension]]:
                    """Normalize LDAP attributes for consistent processing."""
                    ...

            @runtime_checkable
            class Macro(p.Service[str], Protocol):
                """Protocol for DBT macro operations with LDAP data."""

                def create_ldap_snapshot_macro(
                    self,
                    snapshot_config: p.DbtLdap.DbtConfig,
                ) -> p.Result[str]:
                    """Create DBT snapshot macro for LDAP data versioning."""
                    ...

                def create_ldap_test_macro(
                    self,
                    test_config: p.DbtLdap.DbtTestConfig,
                ) -> p.Result[str]:
                    """Create DBT test macro for LDAP data validation."""
                    ...

                def generate_ldap_source_macro(
                    self,
                    source_config: p.DbtLdap.DbtSourceDefinition,
                ) -> p.Result[str]:
                    """Generate DBT macro for LDAP data sources."""
                    ...

                def generate_ldap_transformation_macro(
                    self,
                    transformation_config: p.DbtLdap.TransformationConfig,
                ) -> p.Result[str]:
                    """Generate DBT transformation macro for LDAP data."""
                    ...

            @runtime_checkable
            class Quality(p.Service[p.DbtLdap.ValidationMetrics], Protocol):
                """Protocol for LDAP data quality operations."""

                def check_data_completeness(
                    self,
                    data: t.SequenceOf[p.DbtLdap.UserDimension],
                    completeness_config: p.DbtLdap.DataValidationConfig,
                ) -> p.Result[p.DbtLdap.ValidationMetrics]:
                    """Check LDAP data completeness for DBT processing."""
                    ...

                def detect_data_anomalies(
                    self,
                    data: t.SequenceOf[p.DbtLdap.UserDimension],
                    anomaly_config: p.DbtLdap.DataValidationConfig,
                ) -> p.Result[t.SequenceOf[p.DbtLdap.UserDimension]]:
                    """Detect anomalies in LDAP data."""
                    ...

                def generate_quality_report(
                    self,
                    quality_results: t.SequenceOf[p.DbtLdap.ValidationMetrics],
                    report_config: p.DbtLdap.DbtConfig,
                ) -> p.Result[p.DbtLdap.DbtRunStatus]:
                    """Generate data quality report."""
                    ...

                def validate_ldap_schema_compliance(
                    self,
                    ldap_data: t.SequenceOf[p.DbtLdap.UserDimension],
                    schema_rules: p.DbtLdap.LdapSchema,
                ) -> p.Result[p.DbtLdap.ValidationMetrics]:
                    """Validate LDAP data against schema compliance rules."""
                    ...

            @runtime_checkable
            class Performance(
                p.Service[p.DbtLdap.PerformanceAnalysis],
                Protocol,
            ):
                """Protocol for DBT LDAP performance optimization."""

                def cache_ldap_extractions(
                    self,
                    extraction_config: p.DbtLdap.TransformationConfig,
                    cache_config: p.DbtLdap.DbtConfig,
                ) -> p.Result[bool]:
                    """Cache LDAP data extractions."""
                    ...

                def monitor_dbt_performance(
                    self,
                    run_results: p.DbtLdap.DbtRunStatus,
                ) -> p.Result[p.DbtLdap.PerformanceAnalysis]:
                    """Monitor DBT performance."""
                    ...

                def optimize_dbt_models(
                    self,
                    model_config: p.DbtLdap.DbtProjectConfig,
                    performance_metrics: p.DbtLdap.PerformanceAnalysis,
                ) -> p.Result[p.DbtLdap.DbtProjectConfig]:
                    """Optimize DBT models for performance."""
                    ...

                def optimize_ldap_queries(
                    self,
                    query_config: p.DbtLdap.LdapQuery,
                ) -> p.Result[p.DbtLdap.LdapQuery]:
                    """Optimize LDAP queries for DBT data extraction."""
                    ...

            @runtime_checkable
            class Monitoring(p.Service[p.DbtLdap.DbtRunStatus], Protocol):
                """Protocol for DBT LDAP monitoring operations."""

                def create_monitoring_dashboard(
                    self,
                    dashboard_config: p.DbtLdap.DbtConfig,
                ) -> p.Result[p.DbtLdap.DbtRunStatus]:
                    """Create monitoring dashboard."""
                    ...

                def get_health_status(
                    self,
                ) -> p.Result[p.DbtLdap.ServiceStatus]:
                    """Get DBT LDAP integration health status."""
                    ...

                def monitor_ldap_data_freshness(
                    self,
                    freshness_config: p.DbtLdap.DbtSourceFreshness,
                ) -> p.Result[p.DbtLdap.DbtSourceFreshness]:
                    """Monitor LDAP data freshness."""
                    ...

                def track_dbt_run_metrics(
                    self,
                    run_id: str,
                    metrics: p.DbtLdap.PerformanceAnalysis,
                ) -> p.Result[bool]:
                    """Track DBT run metrics."""
                    ...


__all__: list[str] = ["FlextDbtLdapProtocols", "p"]

p = FlextDbtLdapProtocols
