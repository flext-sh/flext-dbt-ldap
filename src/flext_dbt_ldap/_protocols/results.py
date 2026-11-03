# AUTO-GENERATED FILE — Regenerate with: make gen
"""Source-derived structural model contracts.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_ldap/_protocols/results
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Protocol, runtime_checkable

from flext_meltano import FlextMeltanoProtocols

if TYPE_CHECKING:
    from flext_dbt_ldap import t


class FlextDbtLdapProtocolsResults:
    """Own the structural contracts declared by its model source."""

    @runtime_checkable
    class ValidationMetrics(FlextMeltanoProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def total_entries(self) -> t.NonNegativeInt:
            """Total LDAP entries evaluated."""
            ...

        @property
        def valid_dns(self) -> t.NonNegativeInt:
            """Entries with valid DNs."""
            ...

        @property
        def valid_entries(self) -> t.NonNegativeInt:
            """Entries satisfying required attributes."""
            ...

        @property
        def quality_score(self) -> t.NonNegativeFloat:
            """Validation quality score."""
            ...

        @property
        def validation_passed(self) -> bool:
            """Whether validation met the configured threshold."""
            ...

    @runtime_checkable
    class DbtRunStatus(FlextMeltanoProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def status(self) -> str:
            """Lifecycle status for the DBT execution."""
            ...

        @property
        def models_run(self) -> Sequence[str]:
            """DBT models executed during the run."""
            ...

        @property
        def entries_processed(self) -> t.NonNegativeInt:
            """LDAP entries processed by the run."""
            ...

    @runtime_checkable
    class DbtLdapPipelineResult(FlextMeltanoProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def extracted_entries(self) -> t.NonNegativeInt:
            """LDAP entries extracted by the pipeline."""
            ...

    @runtime_checkable
    class SyncResult(FlextMeltanoProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def overall_success(self) -> bool:
            """Whether every sync component completed successfully."""
            ...

        @property
        def successful_components(self) -> t.NonNegativeInt:
            """Number of successful sync components."""
            ...

        @property
        def total_components(self) -> t.NonNegativeInt:
            """Total sync components evaluated."""
            ...

    @runtime_checkable
    class PerformanceAnalysis(FlextMeltanoProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def execution_time(self) -> t.NonNegativeFloat:
            """Execution time in seconds."""
            ...

        @property
        def rows_processed(self) -> t.NonNegativeInt:
            """Rows processed by the run."""
            ...

        @property
        def memory_usage(self) -> t.NonNegativeFloat:
            """Peak memory usage in megabytes."""
            ...

        @property
        def recommendations(self) -> Sequence[str]:
            """Performance tuning recommendations."""
            ...

    @runtime_checkable
    class ServiceStatus(FlextMeltanoProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def status(self) -> str:
            """Current service health status."""
            ...

        @property
        def service(self) -> str:
            """Service name."""
            ...

        @property
        def capabilities(self) -> Sequence[str]:
            """Supported public service capabilities."""
            ...

    @runtime_checkable
    class AnalyticsReport(FlextMeltanoProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def report_type(self) -> str:
            """Report category."""
            ...

        @property
        def generated_at(self) -> str:
            """Report generation timestamp."""
            ...


__all__: list[str] = [
    "FlextDbtLdapProtocolsResults",
]
