"""DBT LDAP result and reporting models."""

from __future__ import annotations

from typing import Annotated

from pydantic import Field

from flext_dbt_ldap import FlextDbtLdapModelsShared, c, t
from flext_meltano import FlextMeltanoModels


class FlextDbtLdapModelsResults(FlextDbtLdapModelsShared):
    """Project-specific result models for dbt-ldap."""

    class ValidationMetrics(FlextMeltanoModels.Value):
        """Validation metrics for LDAP data quality."""

        total_entries: Annotated[
            t.NonNegativeInt, Field(description="Total LDAP entries evaluated")
        ] = 0
        valid_dns: Annotated[
            t.NonNegativeInt, Field(description="Entries with valid DNs")
        ] = 0
        valid_entries: Annotated[
            t.NonNegativeInt,
            Field(description="Entries satisfying required attributes"),
        ] = 0
        quality_score: Annotated[
            t.NonNegativeFloat, Field(description="Validation quality score")
        ] = 0.0
        validation_passed: Annotated[
            bool,
            Field(description="Whether validation met the configured threshold"),
        ] = False

    class DbtRunStatus(FlextMeltanoModels.Value):
        """Status of a DBT transformation run."""

        status: Annotated[
            str, Field(description="Lifecycle status for the DBT execution")
        ] = c.Meltano.StreamStatus.PENDING
        models_run: Annotated[
            t.StrSequence, Field(description="DBT models executed during the run")
        ] = Field(default_factory=list)
        entries_processed: Annotated[
            t.NonNegativeInt, Field(description="LDAP entries processed by the run")
        ] = 0

    class DbtLdapPipelineResult(FlextMeltanoModels.Value):
        """Result of a complete LDAP-to-DBT pipeline run."""

        extracted_entries: Annotated[
            t.NonNegativeInt,
            Field(description="LDAP entries extracted by the pipeline"),
        ] = 0

    class SyncResult(FlextMeltanoModels.Value):
        """Result of the full warehouse sync."""

        overall_success: Annotated[
            bool,
            Field(description="Whether every sync component completed successfully"),
        ] = False
        successful_components: Annotated[
            t.NonNegativeInt, Field(description="Number of successful sync components")
        ] = 0
        total_components: Annotated[
            t.NonNegativeInt, Field(description="Total sync components evaluated")
        ] = 0

    class PerformanceAnalysis(FlextMeltanoModels.Value):
        """Performance analysis metrics."""

        execution_time: Annotated[
            t.NonNegativeFloat, Field(description="Execution time in seconds")
        ] = 0.0
        rows_processed: Annotated[
            t.NonNegativeInt, Field(description="Rows processed by the run")
        ] = 0
        memory_usage: Annotated[
            t.NonNegativeFloat, Field(description="Peak memory usage in megabytes")
        ] = 0.0
        recommendations: Annotated[
            t.StrSequence, Field(description="Performance tuning recommendations")
        ] = Field(default_factory=list)

    class ServiceStatus(FlextMeltanoModels.Value):
        """Service status and capability summary."""

        status: Annotated[str, Field(description="Current service health status")] = (
            c.DbtLdap.OPERATIONAL
        )
        service: Annotated[str, Field(description="Service name")] = (
            c.DEFAULT_EMPTY_STRING
        )
        capabilities: Annotated[
            t.StrSequence, Field(description="Supported public service capabilities")
        ] = Field(default_factory=list)

    class AnalyticsReport(FlextMeltanoModels.Value):
        """Analytics report metadata."""

        report_type: Annotated[str, Field(description="Report category")] = (
            c.DbtLdap.DEFAULT_REPORT_TYPE
        )
        generated_at: Annotated[
            str, Field(description="Report generation timestamp")
        ] = c.DEFAULT_EMPTY_STRING
