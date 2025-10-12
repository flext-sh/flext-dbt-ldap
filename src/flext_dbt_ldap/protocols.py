"""DBT LDAP protocols for FLEXT ecosystem."""

from typing import Protocol, runtime_checkable

from flext_core import FlextCore


class FlextDbtLdapProtocols:
    """DBT LDAP protocols with explicit re-exports from FlextCore.Protocols foundation.

    This class provides protocol definitions for DBT operations with LDAP data integration,
    data transformation, modeling, and enterprise LDAP analytics patterns.

    Domain Extension Pattern (Phase 3):
    - Explicit re-export of foundation protocols (not inheritance)
    - Domain-specific protocols organized in DbtLdap namespace
    - 100% backward compatibility through aliases
    """

    # ============================================================================
    # RE-EXPORT FOUNDATION PROTOCOLS (EXPLICIT PATTERN)
    # ============================================================================

    Foundation = FlextCore.Protocols.Foundation
    Domain = FlextCore.Protocols.Domain
    Application = FlextCore.Protocols.Application
    Infrastructure = FlextCore.Protocols.Infrastructure
    Extensions = FlextCore.Protocols.Extensions
    Commands = FlextCore.Protocols.Commands

    # ============================================================================
    # DBT LDAP-SPECIFIC PROTOCOLS (DOMAIN NAMESPACE)
    # ============================================================================

    class DbtLdap:
        """DBT LDAP domain protocols for LDAP data transformation and analytics."""

        @runtime_checkable
        class DbtProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for DBT operations with LDAP data."""

            def run_dbt_models(
                self,
                models: FlextCore.Types.StringList | None = None,
                config: FlextCore.Types.Dict | None = None,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Run DBT models with LDAP data sources.

                Args:
                    models: Specific models to run, or None for all models
                    config: DBT configuration parameters

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: DBT run results or error

                """
                ...

            def test_dbt_models(
                self,
                models: FlextCore.Types.StringList | None = None,
                config: FlextCore.Types.Dict | None = None,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Test DBT models with LDAP data validation.

                Args:
                    models: Specific models to test, or None for all models
                    config: DBT test configuration

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: DBT test results or error

                """

            def compile_dbt_models(
                self,
                models: FlextCore.Types.StringList | None = None,
                config: FlextCore.Types.Dict | None = None,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Compile DBT models for LDAP data processing.

                Args:
                    models: Specific models to compile, or None for all models
                    config: DBT compilation configuration

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: DBT compilation results or error

                """

            def get_dbt_manifest(self) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Get DBT manifest with LDAP model definitions.

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: DBT manifest or error

                """

            def validate_dbt_project(self, project_path: str) -> FlextCore.Result[bool]:
                """Validate DBT project configuration for LDAP integration.

                Args:
                    project_path: Path to DBT project directory

                Returns:
                    FlextCore.Result[bool]: Validation status or error

                """

        @runtime_checkable
        class LdapIntegrationProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for LDAP data integration operations."""

            def extract_ldap_data(
                self,
                ldap_config: FlextCore.Types.Dict,
                extraction_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[list[FlextCore.Types.Dict]]:
                """Extract data from LDAP directory for DBT processing.

                Args:
                    ldap_config: LDAP connection configuration
                    extraction_config: Data extraction parameters

                Returns:
                    FlextCore.Result[list[FlextCore.Types.Dict]]: Extracted LDAP data or error

                """

            def transform_ldap_to_dbt_format(
                self,
                ldap_data: list[FlextCore.Types.Dict],
                transformation_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[list[FlextCore.Types.Dict]]:
                """Transform LDAP data to DBT-compatible format.

                Args:
                    ldap_data: Raw LDAP data
                    transformation_config: Transformation parameters

                Returns:
                    FlextCore.Result[list[FlextCore.Types.Dict]]: Transformed data or error

                """

            def validate_ldap_data_quality(
                self,
                data: list[FlextCore.Types.Dict],
                quality_rules: FlextCore.Types.Dict,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Validate LDAP data quality for DBT processing.

                Args:
                    data: LDAP data to validate
                    quality_rules: Data quality validation rules

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Quality validation results or error

                """

            def sync_ldap_to_warehouse(
                self,
                ldap_data: list[FlextCore.Types.Dict],
                warehouse_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Sync LDAP data to data warehouse for DBT processing.

                Args:
                    ldap_data: LDAP data to sync
                    warehouse_config: Data warehouse configuration

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Sync operation results or error

                """

        @runtime_checkable
        class ModelingProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for LDAP data modeling operations."""

            def create_user_dimension(
                self,
                ldap_users: list[FlextCore.Types.Dict],
                dimension_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Create user dimension model from LDAP user data.

                Args:
                    ldap_users: LDAP user data
                    dimension_config: Dimension modeling configuration

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: User dimension model or error

                """

            def create_group_dimension(
                self,
                ldap_groups: list[FlextCore.Types.Dict],
                dimension_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Create group dimension model from LDAP group data.

                Args:
                    ldap_groups: LDAP group data
                    dimension_config: Dimension modeling configuration

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Group dimension model or error

                """

            def create_organizational_hierarchy(
                self,
                ldap_data: list[FlextCore.Types.Dict],
                hierarchy_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Create organizational hierarchy from LDAP organizational units.

                Args:
                    ldap_data: LDAP organizational data
                    hierarchy_config: Hierarchy modeling configuration

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Organizational hierarchy or error

                """

            def generate_fact_tables(
                self,
                dimensions: list[FlextCore.Types.Dict],
                fact_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[list[FlextCore.Types.Dict]]:
                """Generate fact tables from LDAP dimensions.

                Args:
                    dimensions: LDAP dimension models
                    fact_config: Fact table configuration

                Returns:
                    FlextCore.Result[list[FlextCore.Types.Dict]]: Generated fact tables or error

                """

        @runtime_checkable
        class TransformationProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for LDAP data transformation operations."""

            def normalize_ldap_attributes(
                self,
                ldap_entries: list[FlextCore.Types.Dict],
                normalization_rules: FlextCore.Types.Dict,
            ) -> FlextCore.Result[list[FlextCore.Types.Dict]]:
                """Normalize LDAP attributes for consistent data processing.

                Args:
                    ldap_entries: Raw LDAP entries
                    normalization_rules: Attribute normalization rules

                Returns:
                    FlextCore.Result[list[FlextCore.Types.Dict]]: Normalized LDAP data or error

                """

            def enrich_ldap_data(
                self,
                ldap_data: list[FlextCore.Types.Dict],
                enrichment_sources: list[FlextCore.Types.Dict],
            ) -> FlextCore.Result[list[FlextCore.Types.Dict]]:
                """Enrich LDAP data with additional data sources.

                Args:
                    ldap_data: Base LDAP data
                    enrichment_sources: Additional data sources for enrichment

                Returns:
                    FlextCore.Result[list[FlextCore.Types.Dict]]: Enriched LDAP data or error

                """

            def apply_business_rules(
                self,
                data: list[FlextCore.Types.Dict],
                business_rules: FlextCore.Types.Dict,
            ) -> FlextCore.Result[list[FlextCore.Types.Dict]]:
                """Apply business rules to LDAP data transformations.

                Args:
                    data: LDAP data to transform
                    business_rules: Business transformation rules

                Returns:
                    FlextCore.Result[list[FlextCore.Types.Dict]]: Transformed data or error

                """

            def generate_derived_attributes(
                self,
                ldap_data: list[FlextCore.Types.Dict],
                derivation_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[list[FlextCore.Types.Dict]]:
                """Generate derived attributes from LDAP base attributes.

                Args:
                    ldap_data: Base LDAP data
                    derivation_config: Attribute derivation configuration

                Returns:
                    FlextCore.Result[list[FlextCore.Types.Dict]]: Data with derived attributes or error

                """

        @runtime_checkable
        class MacroProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for DBT macro operations with LDAP data."""

            def generate_ldap_source_macro(
                self, source_config: FlextCore.Types.Dict
            ) -> FlextCore.Result[str]:
                """Generate DBT macro for LDAP data sources.

                Args:
                    source_config: LDAP source configuration

                Returns:
                    FlextCore.Result[str]: Generated DBT macro or error

                """

            def create_ldap_test_macro(
                self, test_config: FlextCore.Types.Dict
            ) -> FlextCore.Result[str]:
                """Create DBT test macro for LDAP data validation.

                Args:
                    test_config: LDAP test configuration

                Returns:
                    FlextCore.Result[str]: Generated test macro or error

                """

            def generate_ldap_transformation_macro(
                self, transformation_config: FlextCore.Types.Dict
            ) -> FlextCore.Result[str]:
                """Generate DBT transformation macro for LDAP data.

                Args:
                    transformation_config: Transformation configuration

                Returns:
                    FlextCore.Result[str]: Generated transformation macro or error

                """

            def create_ldap_snapshot_macro(
                self, snapshot_config: FlextCore.Types.Dict
            ) -> FlextCore.Result[str]:
                """Create DBT snapshot macro for LDAP data versioning.

                Args:
                    snapshot_config: Snapshot configuration

                Returns:
                    FlextCore.Result[str]: Generated snapshot macro or error

                """

        @runtime_checkable
        class QualityProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for LDAP data quality operations."""

            def validate_ldap_schema_compliance(
                self,
                ldap_data: list[FlextCore.Types.Dict],
                schema_rules: FlextCore.Types.Dict,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Validate LDAP data against schema compliance rules.

                Args:
                    ldap_data: LDAP data to validate
                    schema_rules: Schema compliance rules

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Schema validation results or error

                """

            def check_data_completeness(
                self,
                data: list[FlextCore.Types.Dict],
                completeness_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Check LDAP data completeness for DBT processing.

                Args:
                    data: LDAP data to check
                    completeness_config: Completeness validation configuration

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Completeness check results or error

                """

            def detect_data_anomalies(
                self,
                data: list[FlextCore.Types.Dict],
                anomaly_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[list[FlextCore.Types.Dict]]:
                """Detect anomalies in LDAP data for quality assurance.

                Args:
                    data: LDAP data to analyze
                    anomaly_config: Anomaly detection configuration

                Returns:
                    FlextCore.Result[list[FlextCore.Types.Dict]]: Detected anomalies or error

                """

            def generate_quality_report(
                self,
                quality_results: list[FlextCore.Types.Dict],
                report_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Generate data quality report for LDAP DBT processing.

                Args:
                    quality_results: Quality validation results
                    report_config: Report generation configuration

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Quality report or error

                """

        @runtime_checkable
        class PerformanceProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for DBT LDAP performance optimization operations."""

            def optimize_dbt_models(
                self,
                model_config: FlextCore.Types.Dict,
                performance_metrics: FlextCore.Types.Dict,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Optimize DBT models for LDAP data processing performance.

                Args:
                    model_config: DBT model configuration
                    performance_metrics: Current performance metrics

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Optimization recommendations or error

                """

            def cache_ldap_extractions(
                self,
                extraction_config: FlextCore.Types.Dict,
                cache_config: FlextCore.Types.Dict,
            ) -> FlextCore.Result[bool]:
                """Cache LDAP data extractions for improved performance.

                Args:
                    extraction_config: LDAP extraction configuration
                    cache_config: Caching configuration

                Returns:
                    FlextCore.Result[bool]: Caching setup success status

                """

            def monitor_dbt_performance(
                self, run_results: FlextCore.Types.Dict
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Monitor DBT performance with LDAP data processing.

                Args:
                    run_results: DBT run results

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Performance metrics or error

                """

            def optimize_ldap_queries(
                self, query_config: FlextCore.Types.Dict
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Optimize LDAP queries for DBT data extraction.

                Args:
                    query_config: LDAP query configuration

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Query optimization results or error

                """

        @runtime_checkable
        class MonitoringProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for DBT LDAP monitoring operations."""

            def track_dbt_run_metrics(
                self, run_id: str, metrics: FlextCore.Types.Dict
            ) -> FlextCore.Result[bool]:
                """Track DBT run metrics for LDAP data processing.

                Args:
                    run_id: DBT run identifier
                    metrics: Run metrics data

                Returns:
                    FlextCore.Result[bool]: Metric tracking success status

                """

            def monitor_ldap_data_freshness(
                self, freshness_config: FlextCore.Types.Dict
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Monitor LDAP data freshness for DBT processing.

                Args:
                    freshness_config: Data freshness monitoring configuration

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Data freshness status or error

                """

            def get_health_status(self) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Get DBT LDAP integration health status.

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Health status or error

                """

            def create_monitoring_dashboard(
                self, dashboard_config: FlextCore.Types.Dict
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Create monitoring dashboard for DBT LDAP operations.

                Args:
                    dashboard_config: Dashboard configuration

                Returns:
                    FlextCore.Result[FlextCore.Types.Dict]: Dashboard creation result or error

                """

    # ============================================================================
    # BACKWARD COMPATIBILITY ALIASES (100% COMPATIBILITY)
    # ============================================================================

    # DBT operations
    DbtProtocol = DbtLdap.DbtProtocol

    # LDAP integration
    LdapIntegrationProtocol = DbtLdap.LdapIntegrationProtocol

    # Data modeling
    ModelingProtocol = DbtLdap.ModelingProtocol

    # Transformations
    TransformationProtocol = DbtLdap.TransformationProtocol

    # DBT macros
    MacroProtocol = DbtLdap.MacroProtocol

    # Data quality
    QualityProtocol = DbtLdap.QualityProtocol

    # Performance optimization
    PerformanceProtocol = DbtLdap.PerformanceProtocol

    # Monitoring
    MonitoringProtocol = DbtLdap.MonitoringProtocol


__all__ = [
    "FlextDbtLdapProtocols",
]
