"""DBT LDAP protocols for FLEXT ecosystem."""

from collections.abc import Sequence
from typing import Protocol, runtime_checkable

from flext_ldap.protocols import FlextLdapProtocols as p_ldap
from flext_meltano.protocols import FlextMeltanoProtocols as p_meltano

from flext_dbt_ldap.typings import t


class FlextDbtLdapProtocols(p_meltano, p_ldap):
    """DBT LDAP protocols extending LDAP and Meltano protocols.

    Extends both FlextLdapProtocols and FlextMeltanoProtocols via multiple inheritance
    to inherit all LDAP protocols, Meltano protocols, and foundation protocols.

    Architecture:
    - EXTENDS: FlextLdapProtocols (inherits .Ldap.* and .Ldif.* protocols)
    - EXTENDS: FlextMeltanoProtocols (inherits .Meltano.* protocols)
    - ADDS: DBT LDAP-specific protocols in Dbt.Ldap namespace
    - PROVIDES: Root-level alias `p` for convenient access

    Usage:
    from flext_dbt_ldap.protocols import p

    # Foundation protocols (inherited)
    result: p.Result[str]
    service: p.Service[str]

    # LDAP protocols (inherited)
    entry: p.Ldap.EntryProtocol

    # Meltano protocols (inherited)
    dbt: p.Meltano.DbtProtocol

    # DBT LDAP-specific protocols
    dbt_protocol: p.Dbt.Ldap.DbtProtocol
    """

    class Dbt:
        """DBT domain protocols."""

        class Ldap:
            """DBT LDAP domain protocols for LDAP data transformation and analytics."""

            @runtime_checkable
            class DbtProtocol(p_ldap.Service[object], Protocol):
                """Protocol for DBT operations with LDAP data."""

                def run_dbt_models(
                    self,
                    models: Sequence[str] | None = None,
                    config: t.DbtLdapCore.DbtConfigDict | None = None,
                ) -> p_meltano.Result[t.DbtLdapCore.ResultDict]:
                    """Run DBT models with LDAP data sources.

                    Args:
                    models: Specific models to run, or None for all models
                    config: DBT configuration parameters

                    Returns:
                    r[t.DbtLdapCore.ResultDict]: DBT run results or error

                    """
                    ...

                def test_dbt_models(
                    self,
                    models: Sequence[str] | None = None,
                    config: t.DbtLdapCore.DbtConfigDict | None = None,
                ) -> p_meltano.Result[t.DbtLdapCore.ResultDict]:
                    """Test DBT models with LDAP data validation.

                    Args:
                    models: Specific models to test, or None for all models
                    config: DBT test configuration

                    Returns:
                    r[t.DbtLdapCore.ResultDict]: DBT test results or error

                    """
                    ...

                def compile_dbt_models(
                    self,
                    models: Sequence[str] | None = None,
                    config: t.DbtLdapCore.DbtConfigDict | None = None,
                ) -> p_meltano.Result[t.DbtLdapCore.ResultDict]:
                    """Compile DBT models for LDAP data processing.

                    Args:
                    models: Specific models to compile, or None for all models
                    config: DBT compilation configuration

                    Returns:
                    r[t.DbtLdapCore.ResultDict]: DBT compilation results or error

                    """
                    ...

                def get_dbt_manifest(
                    self,
                ) -> p_meltano.Result[t.DbtProject.ProjectConfiguration]:
                    """Get DBT manifest with LDAP model definitions.

                    Returns:
                    p_meltano.Result[t.DbtLdapCore.ResultDict]: DBT manifest or error

                    """
                    ...

                def validate_dbt_project(
                    self, project_path: str,
                ) -> p_meltano.Result[bool]:
                    """Validate DBT project configuration for LDAP integration.

                    Args:
                    project_path: Path to DBT project directory

                    Returns:
                    r[bool]: Validation status or error

                    """
                    ...

            @runtime_checkable
            class LdapIntegrationProtocol(p_ldap.Service[object], Protocol):
                """Protocol for LDAP data integration operations."""

                def extract_ldap_data(
                    self,
                    ldap_config: t.LdapConnection.ConnectionConfig,
                    extraction_config: t.DbtTransformation.TransformationConfig,
                ) -> "p_meltano.Result[Sequence[t.DbtLdapCore.DataDict]]":
                    """Extract data from LDAP directory for DBT processing.

                    Args:
                    ldap_config: LDAP connection configuration
                    extraction_config: Data extraction parameters

                    Returns:
                    p_meltano.Result[Sequence[t.DbtLdapCore.DataDict]]: Extracted LDAP data or error

                    """
                    ...

                def transform_ldap_to_dbt_format(
                    self,
                    ldap_data: Sequence[t.DbtLdapCore.DataDict],
                    transformation_config: t.DbtTransformation.TransformationConfig,
                ) -> "p_meltano.Result[Sequence[t.DbtLdapCore.DataDict]]":
                    """Transform LDAP data to DBT-compatible format.

                    Args:
                    ldap_data: Raw LDAP data
                    transformation_config: Transformation parameters

                    Returns:
                    p_meltano.Result[Sequence[t.DbtLdapCore.DataDict]]: Transformed data or error

                    """
                    ...

                def validate_ldap_data_quality(
                    self,
                    data: Sequence[t.DbtLdapCore.DataDict],
                    quality_rules: t.DbtTransformation.DataValidation,
                ) -> "p_meltano.Result[t.DbtLdapCore.ValidationDict]":
                    """Validate LDAP data quality for DBT processing.

                    Args:
                    data: LDAP data to validate
                    quality_rules: Data quality validation rules

                    Returns:
                    p_meltano.Result[t.DbtLdapCore.ValidationDict]: Quality validation results or error

                    """
                    ...

                def sync_ldap_to_warehouse(
                    self,
                    ldap_data: Sequence[t.DbtLdapCore.DataDict],
                    warehouse_config: t.DbtLdapCore.ConfigDict,
                ) -> "p_meltano.Result[t.DbtLdapCore.ResultDict]":
                    """Sync LDAP data to data warehouse for DBT processing.

                    Args:
                    ldap_data: LDAP data to sync
                    warehouse_config: Data warehouse configuration

                    Returns:
                    r[ResultDict]: Sync operation results or error

                    """
                    ...

            @runtime_checkable
            class ModelingProtocol(p_ldap.Service[object], Protocol):
                """Protocol for LDAP data modeling operations."""

                def create_user_dimension(
                    self,
                    ldap_users: Sequence[t.DbtLdapCore.DataDict],
                    dimension_config: t.DbtModel.ModelDefinition,
                ) -> "p_meltano.Result[t.DbtModel.ModelDefinition]":
                    """Create user dimension model from LDAP user data.

                    Args:
                    ldap_users: LDAP user data
                    dimension_config: Dimension modeling configuration

                    Returns:
                    p_meltano.Result[t.DbtModel.ModelDefinition]: User dimension model or error

                    """
                    ...

                def create_group_dimension(
                    self,
                    ldap_groups: Sequence[t.DbtLdapCore.DataDict],
                    dimension_config: t.DbtModel.ModelDefinition,
                ) -> "p_meltano.Result[t.DbtModel.ModelDefinition]":
                    """Create group dimension model from LDAP group data.

                    Args:
                    ldap_groups: LDAP group data
                    dimension_config: Dimension modeling configuration

                    Returns:
                    p_meltano.Result[t.DbtModel.ModelDefinition]: Group dimension model or error

                    """
                    ...

                def create_organizational_hierarchy(
                    self,
                    ldap_data: Sequence[t.DbtLdapCore.DataDict],
                    hierarchy_config: t.DbtModel.ModelDefinition,
                ) -> "p_meltano.Result[t.DbtModel.ModelDefinition]":
                    """Create organizational hierarchy from LDAP organizational units.

                    Args:
                    ldap_data: LDAP organizational data
                    hierarchy_config: Hierarchy modeling configuration

                    Returns:
                    p_meltano.Result[t.DbtModel.ModelDefinition]: Organizational hierarchy or error

                    """
                    ...

                def generate_fact_tables(
                    self,
                    dimensions: Sequence[t.DbtModel.ModelDefinition],
                    fact_config: t.DbtModel.ModelDefinition,
                ) -> "p_meltano.Result[Sequence[t.DbtModel.ModelDefinition]]":
                    """Generate fact tables from LDAP dimensions.

                    Args:
                    dimensions: LDAP dimension models
                    fact_config: Fact table configuration

                    Returns:
                    p_meltano.Result[Sequence[t.DbtModel.ModelDefinition]]: Generated fact tables or error

                    """
                    ...

            @runtime_checkable
            class TransformationProtocol(p_ldap.Service[object], Protocol):
                """Protocol for LDAP data transformation operations."""

                def normalize_ldap_attributes(
                    self,
                    ldap_entries: Sequence[t.DbtLdapCore.DataDict],
                    normalization_rules: t.DbtTransformation.TransformationRule,
                ) -> "p_meltano.Result[Sequence[t.DbtLdapCore.DataDict]]":
                    """Normalize LDAP attributes for consistent data processing.

                    Args:
                    ldap_entries: Raw LDAP entries
                    normalization_rules: Attribute normalization rules

                    Returns:
                    p_meltano.Result[Sequence[t.DbtLdapCore.DataDict]]: Normalized LDAP data or error

                    """
                    ...

                def enrich_ldap_data(
                    self,
                    ldap_data: Sequence[t.DbtLdapCore.DataDict],
                    enrichment_sources: Sequence[t.DbtLdapCore.DataDict],
                ) -> "p_meltano.Result[Sequence[t.DbtLdapCore.DataDict]]":
                    """Enrich LDAP data with additional data sources.

                    Args:
                    ldap_data: Base LDAP data
                    enrichment_sources: Additional data sources for enrichment

                    Returns:
                    p_meltano.Result[Sequence[t.DbtLdapCore.DataDict]]: Enriched LDAP data or error

                    """
                    ...

                def apply_business_rules(
                    self,
                    data: Sequence[t.DbtLdapCore.DataDict],
                    business_rules: t.DbtTransformation.TransformationRule,
                ) -> "p_meltano.Result[Sequence[t.DbtLdapCore.DataDict]]":
                    """Apply business rules to LDAP data transformations.

                    Args:
                    data: LDAP data to transform
                    business_rules: Business transformation rules

                    Returns:
                    p_meltano.Result[Sequence[t.DbtLdapCore.DataDict]]: Transformed data or error

                    """
                    ...

                def generate_derived_attributes(
                    self,
                    ldap_data: Sequence[t.DbtLdapCore.DataDict],
                    derivation_config: t.DbtTransformation.TransformationConfig,
                ) -> "p_meltano.Result[Sequence[t.DbtLdapCore.DataDict]]":
                    """Generate derived attributes from LDAP base attributes.

                    Args:
                    ldap_data: Base LDAP data
                    derivation_config: Attribute derivation configuration

                    Returns:
                    p_meltano.Result[Sequence[t.DbtLdapCore.DataDict]]: Data with derived attributes or error

                    """
                    ...

            @runtime_checkable
            class MacroProtocol(p_ldap.Service[object], Protocol):
                """Protocol for DBT macro operations with LDAP data."""

                def generate_ldap_source_macro(
                    self,
                    source_config: t.DbtSource.SourceDefinition,
                ) -> "p_meltano.Result[str]":
                    """Generate DBT macro for LDAP data sources.

                    Args:
                    source_config: LDAP source configuration

                    Returns:
                    p_meltano.Result[str]: Generated DBT macro or error

                    """
                    ...

                def create_ldap_test_macro(
                    self,
                    test_config: t.DbtProject.TestConfiguration,
                ) -> "p_meltano.Result[str]":
                    """Create DBT test macro for LDAP data validation.

                    Args:
                    test_config: LDAP test configuration

                    Returns:
                    p_meltano.Result[str]: Generated test macro or error

                    """
                    ...

                def generate_ldap_transformation_macro(
                    self,
                    transformation_config: t.DbtTransformation.TransformationConfig,
                ) -> "p_meltano.Result[str]":
                    """Generate DBT transformation macro for LDAP data.

                    Args:
                    transformation_config: Transformation configuration

                    Returns:
                    p_meltano.Result[str]: Generated transformation macro or error

                    """
                    ...

                def create_ldap_snapshot_macro(
                    self,
                    snapshot_config: t.DbtLdapCore.ConfigDict,
                ) -> "p_meltano.Result[str]":
                    """Create DBT snapshot macro for LDAP data versioning.

                    Args:
                    snapshot_config: Snapshot configuration

                    Returns:
                    p_meltano.Result[str]: Generated snapshot macro or error

                    """
                    ...

            @runtime_checkable
            class QualityProtocol(p_ldap.Service[object], Protocol):
                """Protocol for LDAP data quality operations."""

                def validate_ldap_schema_compliance(
                    self,
                    ldap_data: Sequence[t.DbtLdapCore.DataDict],
                    schema_rules: t.LdapData.LdapSchema,
                ) -> "p_meltano.Result[t.DbtLdapCore.ValidationDict]":
                    """Validate LDAP data against schema compliance rules.

                    Args:
                    ldap_data: LDAP data to validate
                    schema_rules: Schema compliance rules

                    Returns:
                    p_meltano.Result[t.DbtLdapCore.ValidationDict]: Schema validation results or error

                    """
                    ...

                def check_data_completeness(
                    self,
                    data: Sequence[t.DbtLdapCore.DataDict],
                    completeness_config: t.DbtTransformation.DataValidation,
                ) -> "p_meltano.Result[t.DbtLdapCore.ValidationDict]":
                    """Check LDAP data completeness for DBT processing.

                    Args:
                    data: LDAP data to check
                    completeness_config: Completeness validation configuration

                    Returns:
                    p_meltano.Result[t.DbtLdapCore.ValidationDict]: Completeness check results or error

                    """
                    ...

                def detect_data_anomalies(
                    self,
                    data: Sequence[t.DbtLdapCore.DataDict],
                    anomaly_config: t.DbtTransformation.DataValidation,
                ) -> "p_meltano.Result[Sequence[t.DbtLdapCore.DataDict]]":
                    """Detect anomalies in LDAP data for quality assurance.

                    Args:
                    data: LDAP data to analyze
                    anomaly_config: Anomaly detection configuration

                    Returns:
                    p_meltano.Result[Sequence[t.DbtLdapCore.DataDict]]: Detected anomalies or error

                    """
                    ...

                def generate_quality_report(
                    self,
                    quality_results: Sequence[t.DbtLdapCore.ValidationDict],
                    report_config: t.DbtLdapCore.ConfigDict,
                ) -> "p_meltano.Result[t.DbtLdapCore.ResultDict]":
                    """Generate data quality report for LDAP DBT processing.

                    Args:
                    quality_results: Quality validation results
                    report_config: Report generation configuration

                    Returns:
                    p_meltano.Result[t.DbtLdapCore.ResultDict]: Quality report or error

                    """
                    ...

            @runtime_checkable
            class PerformanceProtocol(p_ldap.Service[object], Protocol):
                """Protocol for DBT LDAP performance optimization operations."""

                def optimize_dbt_models(
                    self,
                    model_config: t.DbtProject.ModelConfiguration,
                    performance_metrics: t.DbtLdapCore.MetricsDict,
                ) -> "p_meltano.Result[t.DbtProject.ModelConfiguration]":
                    """Optimize DBT models for LDAP data processing performance.

                    Args:
                    model_config: DBT model configuration
                    performance_metrics: Current performance metrics

                    Returns:
                    p_meltano.Result[t.DbtProject.ModelConfiguration]: Optimization recommendations or error

                    """
                    ...

                def cache_ldap_extractions(
                    self,
                    extraction_config: t.DbtTransformation.TransformationConfig,
                    cache_config: t.DbtLdapCore.ConfigDict,
                ) -> "p_meltano.Result[bool]":
                    """Cache LDAP data extractions for improved performance.

                    Args:
                    extraction_config: LDAP extraction configuration
                    cache_config: Caching configuration

                    Returns:
                    p_meltano.Result[bool]: Caching setup success status

                    """
                    ...

                def monitor_dbt_performance(
                    self,
                    run_results: t.DbtLdapCore.ResultDict,
                ) -> "p_meltano.Result[t.DbtLdapCore.MetricsDict]":
                    """Monitor DBT performance with LDAP data processing.

                    Args:
                    run_results: DBT run results

                    Returns:
                    p_meltano.Result[t.DbtLdapCore.MetricsDict]: Performance metrics or error

                    """
                    ...

                def optimize_ldap_queries(
                    self,
                    query_config: t.LdapData.LdapQuery,
                ) -> "p_meltano.Result[t.LdapData.LdapQuery]":
                    """Optimize LDAP queries for DBT data extraction.

                    Args:
                    query_config: LDAP query configuration

                    Returns:
                    p_meltano.Result[t.LdapData.LdapQuery]: Query optimization results or error

                    """
                    ...

            @runtime_checkable
            class MonitoringProtocol(p_ldap.Service[object], Protocol):
                """Protocol for DBT LDAP monitoring operations."""

                def track_dbt_run_metrics(
                    self,
                    run_id: str,
                    metrics: t.DbtLdapCore.MetricsDict,
                ) -> "p_meltano.Result[bool]":
                    """Track DBT run metrics for LDAP data processing.

                    Args:
                    run_id: DBT run identifier
                    metrics: Run metrics data

                    Returns:
                    p_meltano.Result[bool]: Metric tracking success status

                    """
                    ...

                def monitor_ldap_data_freshness(
                    self,
                    freshness_config: t.DbtSource.SourceFreshness,
                ) -> "p_meltano.Result[t.DbtSource.SourceFreshness]":
                    """Monitor LDAP data freshness for DBT processing.

                    Args:
                    freshness_config: Data freshness monitoring configuration

                    Returns:
                    p_meltano.Result[t.DbtSource.SourceFreshness]: Data freshness status or error

                    """
                    ...

                def get_health_status(
                    self,
                ) -> "p_meltano.Result[t.DbtLdapCore.ResultDict]":
                    """Get DBT LDAP integration health status.

                    Returns:
                    p_meltano.Result[t.DbtLdapCore.ResultDict]: Health status or error

                    """
                    ...

                def create_monitoring_dashboard(
                    self,
                    dashboard_config: t.DbtLdapCore.ConfigDict,
                ) -> "p_meltano.Result[t.DbtLdapCore.ResultDict]":
                    """Create monitoring dashboard for DBT LDAP operations.

                    Args:
                    dashboard_config: Dashboard configuration

                    Returns:
                    p_meltano.Result[t.DbtLdapCore.ResultDict]: Dashboard creation result or error

                    """
                    ...


# Runtime alias for simplified usage
p = FlextDbtLdapProtocols

__all__ = [
    "FlextDbtLdapProtocols",
    "p",
]
