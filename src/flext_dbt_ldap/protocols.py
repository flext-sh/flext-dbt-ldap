"""DBT LDAP protocols for FLEXT ecosystem."""

from typing import Protocol, runtime_checkable

from flext_core import (
    FlextProtocols,
    FlextResult,
)


class FlextDbtLdapProtocols:
    """DBT LDAP protocols with explicit re-exports from FlextProtocols foundation.

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

    # ============================================================================
    # DBT LDAP-SPECIFIC PROTOCOLS (DOMAIN NAMESPACE)
    # ============================================================================

    class DbtLdap:
        """DBT LDAP domain protocols for LDAP data transformation and analytics."""

        @runtime_checkable
        class DbtProtocol(FlextProtocols.Service, Protocol):
            """Protocol for DBT operations with LDAP data."""

            def run_dbt_models(
                self,
                models: list[str] | None = None,
                config: dict[str, object] | None = None,
            ) -> FlextResult[dict[str, object]]:
                """Run DBT models with LDAP data sources.

                Args:
                    models: Specific models to run, or None for all models
                    config: DBT configuration parameters

                Returns:
                    FlextResult[dict[str, object]]: DBT run results or error

                """
                ...

            def test_dbt_models(
                self,
                models: list[str] | None = None,
                config: dict[str, object] | None = None,
            ) -> FlextResult[dict[str, object]]:
                """Test DBT models with LDAP data validation.

                Args:
                    models: Specific models to test, or None for all models
                    config: DBT test configuration

                Returns:
                    FlextResult[dict[str, object]]: DBT test results or error

                """

            def compile_dbt_models(
                self,
                models: list[str] | None = None,
                config: dict[str, object] | None = None,
            ) -> FlextResult[dict[str, object]]:
                """Compile DBT models for LDAP data processing.

                Args:
                    models: Specific models to compile, or None for all models
                    config: DBT compilation configuration

                Returns:
                    FlextResult[dict[str, object]]: DBT compilation results or error

                """

            def get_dbt_manifest(self) -> FlextResult[dict[str, object]]:
                """Get DBT manifest with LDAP model definitions.

                Returns:
                    FlextResult[dict[str, object]]: DBT manifest or error

                """

            def validate_dbt_project(self, project_path: str) -> FlextResult[bool]:
                """Validate DBT project configuration for LDAP integration.

                Args:
                    project_path: Path to DBT project directory

                Returns:
                    FlextResult[bool]: Validation status or error

                """

        @runtime_checkable
        class LdapIntegrationProtocol(FlextProtocols.Service, Protocol):
            """Protocol for LDAP data integration operations."""

            def extract_ldap_data(
                self,
                ldap_config: dict[str, object],
                extraction_config: dict[str, object],
            ) -> FlextResult[list[dict[str, object]]]:
                """Extract data from LDAP directory for DBT processing.

                Args:
                    ldap_config: LDAP connection configuration
                    extraction_config: Data extraction parameters

                Returns:
                    FlextResult[list[dict[str, object]]]: Extracted LDAP data or error

                """

            def transform_ldap_to_dbt_format(
                self,
                ldap_data: list[dict[str, object]],
                transformation_config: dict[str, object],
            ) -> FlextResult[list[dict[str, object]]]:
                """Transform LDAP data to DBT-compatible format.

                Args:
                    ldap_data: Raw LDAP data
                    transformation_config: Transformation parameters

                Returns:
                    FlextResult[list[dict[str, object]]]: Transformed data or error

                """

            def validate_ldap_data_quality(
                self,
                data: list[dict[str, object]],
                quality_rules: dict[str, object],
            ) -> FlextResult[dict[str, object]]:
                """Validate LDAP data quality for DBT processing.

                Args:
                    data: LDAP data to validate
                    quality_rules: Data quality validation rules

                Returns:
                    FlextResult[dict[str, object]]: Quality validation results or error

                """

            def sync_ldap_to_warehouse(
                self,
                ldap_data: list[dict[str, object]],
                warehouse_config: dict[str, object],
            ) -> FlextResult[dict[str, object]]:
                """Sync LDAP data to data warehouse for DBT processing.

                Args:
                    ldap_data: LDAP data to sync
                    warehouse_config: Data warehouse configuration

                Returns:
                    FlextResult[dict[str, object]]: Sync operation results or error

                """

        @runtime_checkable
        class ModelingProtocol(FlextProtocols.Service, Protocol):
            """Protocol for LDAP data modeling operations."""

            def create_user_dimension(
                self,
                ldap_users: list[dict[str, object]],
                dimension_config: dict[str, object],
            ) -> FlextResult[dict[str, object]]:
                """Create user dimension model from LDAP user data.

                Args:
                    ldap_users: LDAP user data
                    dimension_config: Dimension modeling configuration

                Returns:
                    FlextResult[dict[str, object]]: User dimension model or error

                """

            def create_group_dimension(
                self,
                ldap_groups: list[dict[str, object]],
                dimension_config: dict[str, object],
            ) -> FlextResult[dict[str, object]]:
                """Create group dimension model from LDAP group data.

                Args:
                    ldap_groups: LDAP group data
                    dimension_config: Dimension modeling configuration

                Returns:
                    FlextResult[dict[str, object]]: Group dimension model or error

                """

            def create_organizational_hierarchy(
                self,
                ldap_data: list[dict[str, object]],
                hierarchy_config: dict[str, object],
            ) -> FlextResult[dict[str, object]]:
                """Create organizational hierarchy from LDAP organizational units.

                Args:
                    ldap_data: LDAP organizational data
                    hierarchy_config: Hierarchy modeling configuration

                Returns:
                    FlextResult[dict[str, object]]: Organizational hierarchy or error

                """

            def generate_fact_tables(
                self,
                dimensions: list[dict[str, object]],
                fact_config: dict[str, object],
            ) -> FlextResult[list[dict[str, object]]]:
                """Generate fact tables from LDAP dimensions.

                Args:
                    dimensions: LDAP dimension models
                    fact_config: Fact table configuration

                Returns:
                    FlextResult[list[dict[str, object]]]: Generated fact tables or error

                """

        @runtime_checkable
        class TransformationProtocol(FlextProtocols.Service, Protocol):
            """Protocol for LDAP data transformation operations."""

            def normalize_ldap_attributes(
                self,
                ldap_entries: list[dict[str, object]],
                normalization_rules: dict[str, object],
            ) -> FlextResult[list[dict[str, object]]]:
                """Normalize LDAP attributes for consistent data processing.

                Args:
                    ldap_entries: Raw LDAP entries
                    normalization_rules: Attribute normalization rules

                Returns:
                    FlextResult[list[dict[str, object]]]: Normalized LDAP data or error

                """

            def enrich_ldap_data(
                self,
                ldap_data: list[dict[str, object]],
                enrichment_sources: list[dict[str, object]],
            ) -> FlextResult[list[dict[str, object]]]:
                """Enrich LDAP data with additional data sources.

                Args:
                    ldap_data: Base LDAP data
                    enrichment_sources: Additional data sources for enrichment

                Returns:
                    FlextResult[list[dict[str, object]]]: Enriched LDAP data or error

                """

            def apply_business_rules(
                self,
                data: list[dict[str, object]],
                business_rules: dict[str, object],
            ) -> FlextResult[list[dict[str, object]]]:
                """Apply business rules to LDAP data transformations.

                Args:
                    data: LDAP data to transform
                    business_rules: Business transformation rules

                Returns:
                    FlextResult[list[dict[str, object]]]: Transformed data or error

                """

            def generate_derived_attributes(
                self,
                ldap_data: list[dict[str, object]],
                derivation_config: dict[str, object],
            ) -> FlextResult[list[dict[str, object]]]:
                """Generate derived attributes from LDAP base attributes.

                Args:
                    ldap_data: Base LDAP data
                    derivation_config: Attribute derivation configuration

                Returns:
                    FlextResult[list[dict[str, object]]]: Data with derived attributes or error

                """

        @runtime_checkable
        class MacroProtocol(FlextProtocols.Service, Protocol):
            """Protocol for DBT macro operations with LDAP data."""

            def generate_ldap_source_macro(
                self, source_config: dict[str, object]
            ) -> FlextResult[str]:
                """Generate DBT macro for LDAP data sources.

                Args:
                    source_config: LDAP source configuration

                Returns:
                    FlextResult[str]: Generated DBT macro or error

                """

            def create_ldap_test_macro(
                self, test_config: dict[str, object]
            ) -> FlextResult[str]:
                """Create DBT test macro for LDAP data validation.

                Args:
                    test_config: LDAP test configuration

                Returns:
                    FlextResult[str]: Generated test macro or error

                """

            def generate_ldap_transformation_macro(
                self, transformation_config: dict[str, object]
            ) -> FlextResult[str]:
                """Generate DBT transformation macro for LDAP data.

                Args:
                    transformation_config: Transformation configuration

                Returns:
                    FlextResult[str]: Generated transformation macro or error

                """

            def create_ldap_snapshot_macro(
                self, snapshot_config: dict[str, object]
            ) -> FlextResult[str]:
                """Create DBT snapshot macro for LDAP data versioning.

                Args:
                    snapshot_config: Snapshot configuration

                Returns:
                    FlextResult[str]: Generated snapshot macro or error

                """

        @runtime_checkable
        class QualityProtocol(FlextProtocols.Service, Protocol):
            """Protocol for LDAP data quality operations."""

            def validate_ldap_schema_compliance(
                self,
                ldap_data: list[dict[str, object]],
                schema_rules: dict[str, object],
            ) -> FlextResult[dict[str, object]]:
                """Validate LDAP data against schema compliance rules.

                Args:
                    ldap_data: LDAP data to validate
                    schema_rules: Schema compliance rules

                Returns:
                    FlextResult[dict[str, object]]: Schema validation results or error

                """

            def check_data_completeness(
                self,
                data: list[dict[str, object]],
                completeness_config: dict[str, object],
            ) -> FlextResult[dict[str, object]]:
                """Check LDAP data completeness for DBT processing.

                Args:
                    data: LDAP data to check
                    completeness_config: Completeness validation configuration

                Returns:
                    FlextResult[dict[str, object]]: Completeness check results or error

                """

            def detect_data_anomalies(
                self,
                data: list[dict[str, object]],
                anomaly_config: dict[str, object],
            ) -> FlextResult[list[dict[str, object]]]:
                """Detect anomalies in LDAP data for quality assurance.

                Args:
                    data: LDAP data to analyze
                    anomaly_config: Anomaly detection configuration

                Returns:
                    FlextResult[list[dict[str, object]]]: Detected anomalies or error

                """

            def generate_quality_report(
                self,
                quality_results: list[dict[str, object]],
                report_config: dict[str, object],
            ) -> FlextResult[dict[str, object]]:
                """Generate data quality report for LDAP DBT processing.

                Args:
                    quality_results: Quality validation results
                    report_config: Report generation configuration

                Returns:
                    FlextResult[dict[str, object]]: Quality report or error

                """

        @runtime_checkable
        class PerformanceProtocol(FlextProtocols.Service, Protocol):
            """Protocol for DBT LDAP performance optimization operations."""

            def optimize_dbt_models(
                self,
                model_config: dict[str, object],
                performance_metrics: dict[str, object],
            ) -> FlextResult[dict[str, object]]:
                """Optimize DBT models for LDAP data processing performance.

                Args:
                    model_config: DBT model configuration
                    performance_metrics: Current performance metrics

                Returns:
                    FlextResult[dict[str, object]]: Optimization recommendations or error

                """

            def cache_ldap_extractions(
                self,
                extraction_config: dict[str, object],
                cache_config: dict[str, object],
            ) -> FlextResult[bool]:
                """Cache LDAP data extractions for improved performance.

                Args:
                    extraction_config: LDAP extraction configuration
                    cache_config: Caching configuration

                Returns:
                    FlextResult[bool]: Caching setup success status

                """

            def monitor_dbt_performance(
                self, run_results: dict[str, object]
            ) -> FlextResult[dict[str, object]]:
                """Monitor DBT performance with LDAP data processing.

                Args:
                    run_results: DBT run results

                Returns:
                    FlextResult[dict[str, object]]: Performance metrics or error

                """

            def optimize_ldap_queries(
                self, query_config: dict[str, object]
            ) -> FlextResult[dict[str, object]]:
                """Optimize LDAP queries for DBT data extraction.

                Args:
                    query_config: LDAP query configuration

                Returns:
                    FlextResult[dict[str, object]]: Query optimization results or error

                """

        @runtime_checkable
        class MonitoringProtocol(FlextProtocols.Service, Protocol):
            """Protocol for DBT LDAP monitoring operations."""

            def track_dbt_run_metrics(
                self, run_id: str, metrics: dict[str, object]
            ) -> FlextResult[bool]:
                """Track DBT run metrics for LDAP data processing.

                Args:
                    run_id: DBT run identifier
                    metrics: Run metrics data

                Returns:
                    FlextResult[bool]: Metric tracking success status

                """

            def monitor_ldap_data_freshness(
                self, freshness_config: dict[str, object]
            ) -> FlextResult[dict[str, object]]:
                """Monitor LDAP data freshness for DBT processing.

                Args:
                    freshness_config: Data freshness monitoring configuration

                Returns:
                    FlextResult[dict[str, object]]: Data freshness status or error

                """

            def get_health_status(self) -> FlextResult[dict[str, object]]:
                """Get DBT LDAP integration health status.

                Returns:
                    FlextResult[dict[str, object]]: Health status or error

                """

            def create_monitoring_dashboard(
                self, dashboard_config: dict[str, object]
            ) -> FlextResult[dict[str, object]]:
                """Create monitoring dashboard for DBT LDAP operations.

                Args:
                    dashboard_config: Dashboard configuration

                Returns:
                    FlextResult[dict[str, object]]: Dashboard creation result or error

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
