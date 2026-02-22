"""DBT LDAP protocols for FLEXT ecosystem.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Protocol, runtime_checkable

from flext_core.protocols import FlextProtocols as p_core
from flext_ldap.protocols import FlextLdapProtocols as p_ldap
from flext_meltano.protocols import FlextMeltanoProtocols as p_meltano

from flext_dbt_ldap.models import FlextDbtLdapModels as m


class FlextDbtLdapProtocols(p_meltano, p_ldap):
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
            class DbtProtocol(p_core.Service[m.DbtRunStatus], Protocol):
                """Protocol for DBT operations with LDAP data."""

                def run_dbt_models(
                    self,
                    models: Sequence[str] | None = None,
                    config: m.DbtConfig | None = None,
                ) -> p_meltano.Result[m.DbtRunStatus]:
                    """Run DBT models with LDAP data sources."""
                    ...

                def test_dbt_models(
                    self,
                    models: Sequence[str] | None = None,
                    config: m.DbtConfig | None = None,
                ) -> p_meltano.Result[m.DbtRunStatus]:
                    """Test DBT models with LDAP data validation."""
                    ...

                def compile_dbt_models(
                    self,
                    models: Sequence[str] | None = None,
                    config: m.DbtConfig | None = None,
                ) -> p_meltano.Result[m.DbtRunStatus]:
                    """Compile DBT models for LDAP data processing."""
                    ...

                def get_dbt_manifest(
                    self,
                ) -> p_meltano.Result[m.DbtProjectConfig]:
                    """Get DBT manifest with LDAP model definitions."""
                    ...

                def validate_dbt_project(
                    self,
                    project_path: str,
                ) -> p_meltano.Result[bool]:
                    """Validate DBT project configuration."""
                    ...

            @runtime_checkable
            class LdapIntegrationProtocol(
                p_core.Service[m.DbtLdapPipelineResult], Protocol
            ):
                """Protocol for LDAP data integration operations."""

                def extract_ldap_data(
                    self,
                    ldap_config: m.LdapQuery,
                    extraction_config: m.TransformationConfig,
                ) -> p_meltano.Result[Sequence[m.UserDimension]]:
                    """Extract data from LDAP directory for DBT processing."""
                    ...

                def transform_ldap_to_dbt_format(
                    self,
                    ldap_data: Sequence[m.UserDimension],
                    transformation_config: m.TransformationConfig,
                ) -> p_meltano.Result[Sequence[m.UserDimension]]:
                    """Transform LDAP data to DBT-compatible format."""
                    ...

                def validate_ldap_data_quality(
                    self,
                    data: Sequence[m.UserDimension],
                    quality_rules: m.DataValidationConfig,
                ) -> p_meltano.Result[m.ValidationMetrics]:
                    """Validate LDAP data quality for DBT processing."""
                    ...

                def sync_ldap_to_warehouse(
                    self,
                    ldap_data: Sequence[m.UserDimension],
                    warehouse_config: m.DbtConfig,
                ) -> p_meltano.Result[m.DbtRunStatus]:
                    """Sync LDAP data to data warehouse."""
                    ...

            @runtime_checkable
            class ModelingProtocol(p_core.Service[m.DbtModelDefinition], Protocol):
                """Protocol for LDAP data modeling operations."""

                def create_user_dimension(
                    self,
                    ldap_users: Sequence[m.UserDimension],
                    dimension_config: m.DbtModelDefinition,
                ) -> p_meltano.Result[m.DbtModelDefinition]:
                    """Create user dimension model from LDAP user data."""
                    ...

                def create_group_dimension(
                    self,
                    ldap_groups: Sequence[m.GroupDimension],
                    dimension_config: m.DbtModelDefinition,
                ) -> p_meltano.Result[m.DbtModelDefinition]:
                    """Create group dimension model from LDAP group data."""
                    ...

                def create_organizational_hierarchy(
                    self,
                    ldap_data: Sequence[m.UserDimension],
                    hierarchy_config: m.DbtModelDefinition,
                ) -> p_meltano.Result[m.DbtModelDefinition]:
                    """Create organizational hierarchy from LDAP OUs."""
                    ...

                def generate_fact_tables(
                    self,
                    dimensions: Sequence[m.DbtModelDefinition],
                    fact_config: m.DbtModelDefinition,
                ) -> p_meltano.Result[Sequence[m.DbtModelDefinition]]:
                    """Generate fact tables from LDAP dimensions."""
                    ...

            @runtime_checkable
            class TransformationProtocol(p_core.Service[m.UserDimension], Protocol):
                """Protocol for LDAP data transformation operations."""

                def normalize_ldap_attributes(
                    self,
                    ldap_entries: Sequence[m.UserDimension],
                    normalization_rules: m.TransformationRule,
                ) -> p_meltano.Result[Sequence[m.UserDimension]]:
                    """Normalize LDAP attributes for consistent processing."""
                    ...

                def enrich_ldap_data(
                    self,
                    ldap_data: Sequence[m.UserDimension],
                    enrichment_sources: Sequence[m.UserDimension],
                ) -> p_meltano.Result[Sequence[m.UserDimension]]:
                    """Enrich LDAP data with additional data sources."""
                    ...

                def apply_business_rules(
                    self,
                    data: Sequence[m.UserDimension],
                    business_rules: m.TransformationRule,
                ) -> p_meltano.Result[Sequence[m.UserDimension]]:
                    """Apply business rules to LDAP data transformations."""
                    ...

                def generate_derived_attributes(
                    self,
                    ldap_data: Sequence[m.UserDimension],
                    derivation_config: m.TransformationConfig,
                ) -> p_meltano.Result[Sequence[m.UserDimension]]:
                    """Generate derived attributes from LDAP base attributes."""
                    ...

            @runtime_checkable
            class MacroProtocol(p_core.Service[str], Protocol):
                """Protocol for DBT macro operations with LDAP data."""

                def generate_ldap_source_macro(
                    self,
                    source_config: m.DbtSourceDefinition,
                ) -> p_meltano.Result[str]:
                    """Generate DBT macro for LDAP data sources."""
                    ...

                def create_ldap_test_macro(
                    self,
                    test_config: m.DbtTestConfig,
                ) -> p_meltano.Result[str]:
                    """Create DBT test macro for LDAP data validation."""
                    ...

                def generate_ldap_transformation_macro(
                    self,
                    transformation_config: m.TransformationConfig,
                ) -> p_meltano.Result[str]:
                    """Generate DBT transformation macro for LDAP data."""
                    ...

                def create_ldap_snapshot_macro(
                    self,
                    snapshot_config: m.DbtConfig,
                ) -> p_meltano.Result[str]:
                    """Create DBT snapshot macro for LDAP data versioning."""
                    ...

            @runtime_checkable
            class QualityProtocol(p_core.Service[m.ValidationMetrics], Protocol):
                """Protocol for LDAP data quality operations."""

                def validate_ldap_schema_compliance(
                    self,
                    ldap_data: Sequence[m.UserDimension],
                    schema_rules: m.LdapSchema,
                ) -> p_meltano.Result[m.ValidationMetrics]:
                    """Validate LDAP data against schema compliance rules."""
                    ...

                def check_data_completeness(
                    self,
                    data: Sequence[m.UserDimension],
                    completeness_config: m.DataValidationConfig,
                ) -> p_meltano.Result[m.ValidationMetrics]:
                    """Check LDAP data completeness for DBT processing."""
                    ...

                def detect_data_anomalies(
                    self,
                    data: Sequence[m.UserDimension],
                    anomaly_config: m.DataValidationConfig,
                ) -> p_meltano.Result[Sequence[m.UserDimension]]:
                    """Detect anomalies in LDAP data."""
                    ...

                def generate_quality_report(
                    self,
                    quality_results: Sequence[m.ValidationMetrics],
                    report_config: m.DbtConfig,
                ) -> p_meltano.Result[m.DbtRunStatus]:
                    """Generate data quality report."""
                    ...

            @runtime_checkable
            class PerformanceProtocol(p_core.Service[m.PerformanceAnalysis], Protocol):
                """Protocol for DBT LDAP performance optimization."""

                def optimize_dbt_models(
                    self,
                    model_config: m.DbtProjectConfig,
                    performance_metrics: m.PerformanceAnalysis,
                ) -> p_meltano.Result[m.DbtProjectConfig]:
                    """Optimize DBT models for performance."""
                    ...

                def cache_ldap_extractions(
                    self,
                    extraction_config: m.TransformationConfig,
                    cache_config: m.DbtConfig,
                ) -> p_meltano.Result[bool]:
                    """Cache LDAP data extractions."""
                    ...

                def monitor_dbt_performance(
                    self,
                    run_results: m.DbtRunStatus,
                ) -> p_meltano.Result[m.PerformanceAnalysis]:
                    """Monitor DBT performance."""
                    ...

                def optimize_ldap_queries(
                    self,
                    query_config: m.LdapQuery,
                ) -> p_meltano.Result[m.LdapQuery]:
                    """Optimize LDAP queries for DBT data extraction."""
                    ...

            @runtime_checkable
            class MonitoringProtocol(p_core.Service[m.DbtRunStatus], Protocol):
                """Protocol for DBT LDAP monitoring operations."""

                def track_dbt_run_metrics(
                    self,
                    run_id: str,
                    metrics: m.PerformanceAnalysis,
                ) -> p_meltano.Result[bool]:
                    """Track DBT run metrics."""
                    ...

                def monitor_ldap_data_freshness(
                    self,
                    freshness_config: m.DbtSourceFreshness,
                ) -> p_meltano.Result[m.DbtSourceFreshness]:
                    """Monitor LDAP data freshness."""
                    ...

                def get_health_status(
                    self,
                ) -> p_meltano.Result[m.ServiceStatus]:
                    """Get DBT LDAP integration health status."""
                    ...

                def create_monitoring_dashboard(
                    self,
                    dashboard_config: m.DbtConfig,
                ) -> p_meltano.Result[m.DbtRunStatus]:
                    """Create monitoring dashboard."""
                    ...


# Runtime alias for simplified usage
p = FlextDbtLdapProtocols

__all__ = [
    "FlextDbtLdapProtocols",
    "p",
]
