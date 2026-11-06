# AUTO-GENERATED FILE — Regenerate with: make gen
"""Source-derived structural model contracts.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_ldap/_protocols/dbt
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Protocol, runtime_checkable

from flext_meltano import FlextMeltanoProtocols

if TYPE_CHECKING:
    from flext_dbt_ldap import t


class FlextDbtLdapProtocolsDbt:
    """Own the structural contracts declared by its model source."""

    @runtime_checkable
    class DbtConnectionProfile(FlextMeltanoProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def type(self) -> str:
            """Dbt adapter type identifier."""
            ...

        @property
        def host(self) -> str:
            """LDAP server hostname."""
            ...

        @property
        def port(self) -> int:
            """LDAP server port."""
            ...

        @property
        def use_tls(self) -> bool:
            """Use TLS for LDAP connection."""
            ...

        @property
        def base_dn(self) -> str:
            """LDAP base DN."""
            ...

        @property
        def project(self) -> str:
            """Dbt project name owning this profile."""
            ...

    @runtime_checkable
    class DbtProjectConfig(FlextMeltanoProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def name(self) -> str:
            """DBT project name."""
            ...

        @property
        def version(self) -> str:
            """DBT project version."""
            ...

        @property
        def profile(self) -> str:
            """DBT profile name."""
            ...

        @property
        def model_paths(self) -> Sequence[str]:
            """Directories containing DBT models."""
            ...

        @property
        def analysis_paths(self) -> Sequence[str]:
            """Directories containing DBT analyses."""
            ...

        @property
        def test_paths(self) -> Sequence[str]:
            """Directories containing DBT tests."""
            ...

        @property
        def seed_paths(self) -> Sequence[str]:
            """Directories containing DBT seeds."""
            ...

        @property
        def macro_paths(self) -> Sequence[str]:
            """Directories containing DBT macros."""
            ...

        @property
        def snapshot_paths(self) -> Sequence[str]:
            """Directories containing DBT snapshots."""
            ...

        @property
        def target_path(self) -> str:
            """Directory used for DBT build artifacts."""
            ...

        @property
        def clean_targets(self) -> Sequence[str]:
            """Directories cleaned by DBT maintenance commands."""
            ...

        @property
        def target_schema(self) -> str:
            """Default database schema for DBT relations."""
            ...

        @property
        def tags(self) -> Sequence[str]:
            """Tags applied to generated DBT resources."""
            ...

        @property
        def materialized(self) -> str:
            """Default DBT materialization strategy."""
            ...

    @runtime_checkable
    class DbtSourceFreshness(FlextMeltanoProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def warn_after(self) -> t.IntMapping:
            """Warning freshness thresholds."""
            ...

        @property
        def error_after(self) -> t.IntMapping:
            """Error freshness thresholds."""
            ...

    @runtime_checkable
    class DbtSourceDefinition(FlextMeltanoProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def name(self) -> str:
            """DBT source name."""
            ...

        @property
        def description(self) -> str:
            """DBT source description."""
            ...

        @property
        def tables(self) -> Sequence[t.JsonMapping]:
            """Tables declared for the DBT source."""
            ...

    @runtime_checkable
    class DbtConfig(FlextMeltanoProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def target(self) -> str:
            """Named DBT target to execute against."""
            ...

        @property
        def profiles_dir(self) -> str:
            """Path to the DBT profiles directory."""
            ...

        @property
        def project_dir(self) -> str:
            """Path to the DBT project directory."""
            ...


__all__: list[str] = [
    "FlextDbtLdapProtocolsDbt",
]
