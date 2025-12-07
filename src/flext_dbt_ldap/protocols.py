"""DBT LDAP protocols for FLEXT ecosystem."""

from collections.abc import Sequence
from typing import Protocol, runtime_checkable

from flext_core import p as p_core, r
from flext_dbt_ldap_core.typings import FlextDbtLdapTypes


class FlextDbtLdapProtocols:
    """DBT LDAP protocols with explicit re-exports from p foundation.

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
        class DbtProtocol(p_core.Service, Protocol):
            """Protocol for DBT operations with LDAP data."""

            def run_dbt_models(
                self,
                models: Sequence[str] | None = None,
                config: FlextDbtLdapTypes.DbtLdapCore.DbtConfigDict | None = None,
            ) -> "p_core.ResultProtocol[FlextDbtLdapTypes.DbtLdapCore.ResultDict]":
                """Run DBT models with LDAP data sources.

                Args:
                models: Specific models to run, or None for all models
                config: DBT configuration parameters

                Returns:
                r[FlextDbtLdapTypes.DbtLdapCore.ResultDict]: DBT run results or error

                """
                ...

            def test_dbt_models(
                self,
                models: Sequence[str] | None = None,
                config: FlextDbtLdapTypes.DbtLdapCore.DbtConfigDict | None = None,
            ) -> "p_core.ResultProtocol[FlextDbtLdapTypes.DbtLdapCore.ResultDict]":
                """Test DBT models with LDAP data validation.

                Args:
                models: Specific models to test, or None for all models
                config: DBT test configuration

                Returns:
                r[FlextDbtLdapTypes.DbtLdapCore.ResultDict]: DBT test results or error

                """

            def compile_dbt_models(
                self,
                models: Sequence[str] | None = None,
                config: FlextDbtLdapTypes.DbtLdapCore.DbtConfigDict | None = None,
            ) -> "p_core.ResultProtocol[FlextDbtLdapTypes.DbtLdapCore.ResultDict]":
                """Compile DBT models for LDAP data processing.

                Args:
                models: Specific models to compile, or None for all models
                config: DBT compilation configuration

                Returns:
                r[FlextDbtLdapTypes.DbtLdapCore.ResultDict]: DBT compilation results or error

                """

            def get_dbt_manifest(
                self,
            ) -> "p_core.ResultProtocol[FlextDbtLdapTypes.DbtProject.ProjectConfiguration]":
                """Get DBT manifest with LDAP model definitions.

                Returns:
                p_core.ResultProtocol[FlextDbtLdapTypes.DbtLdapCore.ResultDict]: DBT manifest or error

                """

            def validate_dbt_project(self, project_path: str) -> r[bool]:
                """Validate DBT project configuration for LDAP integration.

                Args:
                project_path: Path to DBT project directory

                Returns:
                r[bool]: Validation status or error

                """

        @runtime_checkable
        class LdapIntegrationProtocol(p_core.Service, Protocol):
            """Protocol for LDAP data integration operations."""

            def extract_ldap_data(
                self,
                ldap_config: FlextDbtLdapTypes.LdapConnection.ConnectionConfig,
                extraction_config: FlextDbtLdapTypes.DbtTransformation.TransformationConfig,
            ) -> "p_core.ResultProtocol[Sequence[FlextDbtLdapTypes.DbtLdapCore.DataDict]]":
                """Extract data from LDAP directory for DBT processing.

                Args:
                ldap_config: LDAP connection configuration
                extraction_config: Data extraction parameters

                Returns:
                p_core.ResultProtocol[Sequence[FlextDbtLdapTypes.DbtLdapCore.DataDict]]: Extracted LDAP data or error

                """

            def transform_ldap_to_dbt_format(
                self,
                ldap_data: Sequence[FlextDbtLdapTypes.DbtLdapCore.DataDict],
                transformation_config: FlextDbtLdapTypes.DbtTransformation.TransformationConfig,
            ) -> "p_core.ResultProtocol[Sequence[FlextDbtLdapTypes.DbtLdapCore.DataDict]]":
                """Transform LDAP data to DBT-compatible format.

                Args:
                ldap_data: Raw LDAP data
                transformation_config: Transformation parameters

                Returns:
                p_core.ResultProtocol[Sequence[FlextDbtLdapTypes.DbtLdapCore.DataDict]]: Transformed data or error

                """

            def validate_ldap_data_quality(
                self,
                data: Sequence[FlextDbtLdapTypes.DbtLdapCore.DataDict],
                quality_rules: FlextDbtLdapTypes.DbtTransformation.DataValidation,
            ) -> "p_core.ResultProtocol[FlextDbtLdapTypes.DbtLdapCore.ValidationDict]":
                """Validate LDAP data quality for DBT processing.

                Args:
                data: LDAP data to validate
                quality_rules: Data quality validation rules

                Returns:
                p_core.ResultProtocol[FlextDbtLdapTypes.DbtLdapCore.ValidationDict]: Quality validation results or error

                """

            def sync_ldap_to_warehouse(
                self,
                ldap_data: Sequence[FlextDbtLdapTypes.DbtLdapCore.DataDict],
                warehouse_config: FlextDbtLdapTypes.DbtLdapCore.ConfigDict,
            ) -> "p_core.ResultProtocol[FlextDbtLdapTypes.DbtLdapCore.ResultDict]":
                """Sync LDAP data to data warehouse for DBT processing.

                Args:
                ldap_data: LDAP data to sync
                warehouse_config: Data warehouse configuration

                Returns:
                r[ResultDict]: Sync operation results or error

                """

        @runtime_checkable
        class ModelingProtocol(p_core.Service, Protocol):
            """Protocol for LDAP data modeling operations."""

            def create_user_dimension(
                self,
                ldap_users: Sequence[FlextDbtLdapTypes.DbtLdapCore.DataDict],
                dimension_config: FlextDbtLdapTypes.DbtModel.ModelDefinition,
            ) -> "p_core.ResultProtocol[FlextDbtLdapTypes.DbtModel.ModelDefinition]":
                """Create user dimension model from LDAP user data.

                Args:
                ldap_users: LDAP user data
                dimension_config: Dimension modeling configuration

                Returns:
                p_core.ResultProtocol[FlextDbtLdapTypes.DbtModel.ModelDefinition]: User dimension model or error

                """

            def create_group_dimension(
                self,
                ldap_groups: Sequence[FlextDbtLdapTypes.DbtLdapCore.DataDict],
                dimension_config: FlextDbtLdapTypes.DbtModel.ModelDefinition,
            ) -> "p_core.ResultProtocol[FlextDbtLdapTypes.DbtModel.ModelDefinition]":
                """Create group dimension model from LDAP group data.

                Args:
                ldap_groups: LDAP group data
                dimension_config: Dimension modeling configuration

                Returns:
                p_core.ResultProtocol[FlextDbtLdapTypes.DbtModel.ModelDefinition]: Group dimension model or error

                """

            def create_organizational_hierarchy(
                self,
                ldap_data: Sequence[FlextDbtLdapTypes.DbtLdapCore.DataDict],
                hierarchy_config: FlextDbtLdapTypes.DbtModel.ModelDefinition,
            ) -> "p_core.ResultProtocol[FlextDbtLdapTypes.DbtModel.ModelDefinition]":
                """Create organizational hierarchy from LDAP organizational units.

                Args:
                ldap_data: LDAP organizational data
                hierarchy_config: Hierarchy modeling configuration

                Returns:
                p_core.ResultProtocol[FlextDbtLdapTypes.DbtModel.ModelDefinition]: Organizational hierarchy or error

                """

            def generate_fact_tables(
                self,
                dimensions: Sequence[FlextDbtLdapTypes.DbtModel.ModelDefinition],
                fact_config: FlextDbtLdapTypes.DbtModel.ModelDefinition,
            ) -> "p_core.ResultProtocol[Sequence[FlextDbtLdapTypes.DbtModel.ModelDefinition]]":
                """Generate fact tables from LDAP dimensions.

                Args:
                dimensions: LDAP dimension models
                fact_config: Fact table configuration

                Returns:
                p_core.ResultProtocol[Sequence[FlextDbtLdapTypes.DbtModel.ModelDefinition]]: Generated fact tables or error

                """

        @runtime_checkable
        class TransformationProtocol(p_core.Service, Protocol):
            """Protocol for LDAP data transformation operations."""

            def normalize_ldap_attributes(
                self,
                ldap_entries: Sequence[FlextDbtLdapTypes.DbtLdapCore.DataDict],
                normalization_rules: FlextDbtLdapTypes.DbtTransformation.TransformationRule,
            ) -> "p_core.ResultProtocol[Sequence[FlextDbtLdapTypes.DbtLdapCore.DataDict]]":
                """Normalize LDAP attributes for consistent data processing.

                Args:
                ldap_entries: Raw LDAP entries
                normalization_rules: Attribute normalization rules

                Returns:
                p_core.ResultProtocol[Sequence[FlextDbtLdapTypes.DbtLdapCore.DataDict]]: Normalized LDAP data or error

                """

            def enrich_ldap_data(
                self,
                ldap_data: Sequence[FlextDbtLdapTypes.DbtLdapCore.DataDict],
                enrichment_sources: Sequence[FlextDbtLdapTypes.DbtLdapCore.DataDict],
            ) -> "p_core.ResultProtocol[Sequence[FlextDbtLdapTypes.DbtLdapCore.DataDict]]":
                """Enrich LDAP data with additional data sources.

                Args:
                ldap_data: Base LDAP data
                enrichment_sources: Additional data sources for enrichment

                Returns:
                p_core.ResultProtocol[Sequence[FlextDbtLdapTypes.DbtLdapCore.DataDict]]: Enriched LDAP data or error

                """

            def apply_business_rules(
                self,
                data: Sequence[FlextDbtLdapTypes.DbtLdapCore.DataDict],
                business_rules: FlextDbtLdapTypes.DbtTransformation.TransformationRule,
            ) -> "p_core.ResultProtocol[Sequence[FlextDbtLdapTypes.DbtLdapCore.DataDict]]":
                """Apply business rules to LDAP data transformations.

                Args:
                data: LDAP data to transform
                business_rules: Business transformation rules

                Returns:
                p_core.ResultProtocol[Sequence[FlextDbtLdapTypes.DbtLdapCore.DataDict]]: Transformed data or error

                """

            def generate_derived_attributes(
                self,
                ldap_data: Sequence[FlextDbtLdapTypes.DbtLdapCore.DataDict],
                derivation_config: FlextDbtLdapTypes.DbtTransformation.TransformationConfig,
            ) -> "p_core.ResultProtocol[Sequence[FlextDbtLdapTypes.DbtLdapCore.DataDict]]":
                """Generate derived attributes from LDAP base attributes.

                Args:
                ldap_data: Base LDAP data
                derivation_config: Attribute derivation configuration

                Returns:
                p_core.ResultProtocol[Sequence[FlextDbtLdapTypes.DbtLdapCore.DataDict]]: Data with derived attributes or error

                """

        @runtime_checkable
        class MacroProtocol(p_core.Service, Protocol):
            """Protocol for DBT macro operations with LDAP data."""

            def generate_ldap_source_macro(
                self,
                source_config: FlextDbtLdapTypes.DbtSource.SourceDefinition,
            ) -> "p_core.ResultProtocol[str]":
                """Generate DBT macro for LDAP data sources.

                Args:
                source_config: LDAP source configuration

                Returns:
                p_core.ResultProtocol[str]: Generated DBT macro or error

                """

            def create_ldap_test_macro(
                self,
                test_config: FlextDbtLdapTypes.DbtProject.TestConfiguration,
            ) -> "p_core.ResultProtocol[str]":
                """Create DBT test macro for LDAP data validation.

                Args:
                test_config: LDAP test configuration

                Returns:
                p_core.ResultProtocol[str]: Generated test macro or error

                """

            def generate_ldap_transformation_macro(
                self,
                transformation_config: FlextDbtLdapTypes.DbtTransformation.TransformationConfig,
            ) -> "p_core.ResultProtocol[str]":
                """Generate DBT transformation macro for LDAP data.

                Args:
                transformation_config: Transformation configuration

                Returns:
                p_core.ResultProtocol[str]: Generated transformation macro or error

                """

            def create_ldap_snapshot_macro(
                self,
                snapshot_config: FlextDbtLdapTypes.DbtLdapCore.ConfigDict,
            ) -> "p_core.ResultProtocol[str]":
                """Create DBT snapshot macro for LDAP data versioning.

                Args:
                snapshot_config: Snapshot configuration

                Returns:
                p_core.ResultProtocol[str]: Generated snapshot macro or error

                """

        @runtime_checkable
        class QualityProtocol(p_core.Service, Protocol):
            """Protocol for LDAP data quality operations."""

            def validate_ldap_schema_compliance(
                self,
                ldap_data: Sequence[FlextDbtLdapTypes.DbtLdapCore.DataDict],
                schema_rules: FlextDbtLdapTypes.LdapData.LdapSchema,
            ) -> "p_core.ResultProtocol[FlextDbtLdapTypes.DbtLdapCore.ValidationDict]":
                """Validate LDAP data against schema compliance rules.

                Args:
                ldap_data: LDAP data to validate
                schema_rules: Schema compliance rules

                Returns:
                p_core.ResultProtocol[FlextDbtLdapCore.ValidationDict]: Schema validation results or error

                """

            def check_data_completeness(
                self,
                data: Sequence[FlextDbtLdapTypes.DbtLdapCore.DataDict],
                completeness_config: FlextDbtLdapTypes.DbtTransformation.DataValidation,
            ) -> "p_core.ResultProtocol[FlextDbtLdapTypes.DbtLdapCore.ValidationDict]":
                """Check LDAP data completeness for DBT processing.

                Args:
                data: LDAP data to check
                completeness_config: Completeness validation configuration

                Returns:
                p_core.ResultProtocol[FlextDbtLdapCore.ValidationDict]: Completeness check results or error

                """

            def detect_data_anomalies(
                self,
                data: Sequence[FlextDbtLdapTypes.DbtLdapCore.DataDict],
                anomaly_config: FlextDbtLdapTypes.DbtTransformation.DataValidation,
            ) -> "p_core.ResultProtocol[Sequence[FlextDbtLdapTypes.DbtLdapCore.DataDict]]":
                """Detect anomalies in LDAP data for quality assurance.

                Args:
                data: LDAP data to analyze
                anomaly_config: Anomaly detection configuration

                Returns:
                p_core.ResultProtocol[Sequence[FlextDbtLdapCore.DataDict]]: Detected anomalies or error

                """

            def generate_quality_report(
                self,
                quality_results: Sequence[FlextDbtLdapTypes.DbtLdapCore.ValidationDict],
                report_config: FlextDbtLdapTypes.DbtLdapCore.ConfigDict,
            ) -> "p_core.ResultProtocol[FlextDbtLdapTypes.DbtLdapCore.ResultDict]":
                """Generate data quality report for LDAP DBT processing.

                Args:
                quality_results: Quality validation results
                report_config: Report generation configuration

                Returns:
                p_core.ResultProtocol[FlextDbtLdapCore.ResultDict]: Quality report or error

                """

        @runtime_checkable
        class PerformanceProtocol(p_core.Service, Protocol):
            """Protocol for DBT LDAP performance optimization operations."""

            def optimize_dbt_models(
                self,
                model_config: FlextDbtLdapTypes.DbtProject.ModelConfiguration,
                performance_metrics: FlextDbtLdapTypes.DbtLdapCore.MetricsDict,
            ) -> (
                "p_core.ResultProtocol[FlextDbtLdapTypes.DbtProject.ModelConfiguration]"
            ):
                """Optimize DBT models for LDAP data processing performance.

                Args:
                model_config: DBT model configuration
                performance_metrics: Current performance metrics

                Returns:
                p_core.ResultProtocol[FlextDbtLdapTypes.DbtProject.ModelConfiguration]: Optimization recommendations or error

                """

            def cache_ldap_extractions(
                self,
                extraction_config: FlextDbtLdapTypes.DbtTransformation.TransformationConfig,
                cache_config: FlextDbtLdapTypes.DbtLdapCore.ConfigDict,
            ) -> "p_core.ResultProtocol[bool]":
                """Cache LDAP data extractions for improved performance.

                Args:
                extraction_config: LDAP extraction configuration
                cache_config: Caching configuration

                Returns:
                p_core.ResultProtocol[bool]: Caching setup success status

                """

            def monitor_dbt_performance(
                self,
                run_results: FlextDbtLdapTypes.DbtLdapCore.ResultDict,
            ) -> "p_core.ResultProtocol[FlextDbtLdapTypes.DbtLdapCore.MetricsDict]":
                """Monitor DBT performance with LDAP data processing.

                Args:
                run_results: DBT run results

                Returns:
                p_core.ResultProtocol[FlextDbtLdapTypes.DbtLdapCore.MetricsDict]: Performance metrics or error

                """

            def optimize_ldap_queries(
                self,
                query_config: FlextDbtLdapTypes.LdapData.LdapQuery,
            ) -> "p_core.ResultProtocol[FlextDbtLdapTypes.LdapData.LdapQuery]":
                """Optimize LDAP queries for DBT data extraction.

                Args:
                query_config: LDAP query configuration

                Returns:
                p_core.ResultProtocol[FlextDbtLdapTypes.LdapData.LdapQuery]: Query optimization results or error

                """

        @runtime_checkable
        class MonitoringProtocol(p_core.Service, Protocol):
            """Protocol for DBT LDAP monitoring operations."""

            def track_dbt_run_metrics(
                self,
                run_id: str,
                metrics: FlextDbtLdapTypes.DbtLdapCore.MetricsDict,
            ) -> "p_core.ResultProtocol[bool]":
                """Track DBT run metrics for LDAP data processing.

                Args:
                run_id: DBT run identifier
                metrics: Run metrics data

                Returns:
                p_core.ResultProtocol[bool]: Metric tracking success status

                """

            def monitor_ldap_data_freshness(
                self,
                freshness_config: FlextDbtLdapTypes.DbtSource.SourceFreshness,
            ) -> "p_core.ResultProtocol[FlextDbtLdapTypes.DbtSource.SourceFreshness]":
                """Monitor LDAP data freshness for DBT processing.

                Args:
                freshness_config: Data freshness monitoring configuration

                Returns:
                p_core.ResultProtocol[FlextDbtLdapTypes.DbtSource.SourceFreshness]: Data freshness status or error

                """

            def get_health_status(
                self,
            ) -> "p_core.ResultProtocol[FlextDbtLdapTypes.DbtLdapCore.ResultDict]":
                """Get DBT LDAP integration health status.

                Returns:
                p_core.ResultProtocol[FlextDbtLdapTypes.DbtLdapCore.ResultDict]: Health status or error

                """

            def create_monitoring_dashboard(
                self,
                dashboard_config: FlextDbtLdapTypes.DbtLdapCore.ConfigDict,
            ) -> "p_core.ResultProtocol[FlextDbtLdapTypes.DbtLdapCore.ResultDict]":
                """Create monitoring dashboard for DBT LDAP operations.

                Args:
                dashboard_config: Dashboard configuration

                Returns:
                p_core.ResultProtocol[FlextDbtLdapTypes.DbtLdapCore.ResultDict]: Dashboard creation result or error

                """

    # ============================================================================
    # BACKWARD COMPATIBILITY - Real Inheritance Protocol Classes
    # ============================================================================

    # DBT operations - real inheritance (DbtLdap.DbtProtocol already inherits Protocol)
    @runtime_checkable
    class DbtProtocol(DbtLdap.DbtProtocol):
        """DBT Protocol - real inheritance."""

    # LDAP integration - real inheritance
    @runtime_checkable
    class LdapIntegrationProtocol(DbtLdap.LdapIntegrationProtocol):
        """LDAP Integration Protocol - real inheritance."""

    # Data modeling - real inheritance
    @runtime_checkable
    class ModelingProtocol(DbtLdap.ModelingProtocol):
        """Modeling Protocol - real inheritance."""

    # Transformations - real inheritance
    @runtime_checkable
    class TransformationProtocol(DbtLdap.TransformationProtocol):
        """Transformation Protocol - real inheritance."""

    # DBT macros - real inheritance
    @runtime_checkable
    class MacroProtocol(DbtLdap.MacroProtocol):
        """Macro Protocol - real inheritance."""

    # Data quality - real inheritance
    @runtime_checkable
    class QualityProtocol(DbtLdap.QualityProtocol):
        """Quality Protocol - real inheritance."""

    # Performance optimization - real inheritance
    @runtime_checkable
    class PerformanceProtocol(DbtLdap.PerformanceProtocol):
        """Performance Protocol - real inheritance."""

    # Monitoring - real inheritance
    @runtime_checkable
    class MonitoringProtocol(DbtLdap.MonitoringProtocol):
        """Monitoring Protocol - real inheritance."""


__all__ = [
    "FlextDbtLdapProtocols",
]
