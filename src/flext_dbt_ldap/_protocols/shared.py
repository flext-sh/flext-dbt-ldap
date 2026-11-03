# AUTO-GENERATED FILE — Regenerate with: make gen
"""Source-derived structural model contracts.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_ldap/_protocols/shared
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Protocol, runtime_checkable

from flext_meltano import FlextMeltanoProtocols

from flext_dbt_ldap import t

if TYPE_CHECKING:
    from flext_core import p


class FlextDbtLdapProtocolsShared:
    """Own the structural contracts declared by its model source."""

    @runtime_checkable
    class DbtSerializable(FlextMeltanoProtocols.Model, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def domain_events(self) -> Sequence[p.DomainEvent]:
            """List of uncommitted domain events for event sourcing."""
            ...

        def to_dbt_dict(self) -> t.ConfigurationMapping:
            """Dump models to DBT-friendly dictionaries."""
            ...

    @runtime_checkable
    class DbtDimensionBase(FlextMeltanoProtocols.Model, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def domain_events(self) -> Sequence[p.DomainEvent]:
            """List of uncommitted domain events for event sourcing."""
            ...

        @property
        def common_name(self) -> str:
            """Canonical common name."""
            ...

        @property
        def is_active(self) -> bool:
            """Whether the directory record is active."""
            ...

        @property
        def created_date(self) -> str | None:
            """Source creation timestamp."""
            ...

        @property
        def modified_date(self) -> str | None:
            """Source modification timestamp."""
            ...

        def to_dbt_dict(self) -> t.ConfigurationMapping:
            """Dump models to DBT-friendly dictionaries."""
            ...


__all__: list[str] = [
    "FlextDbtLdapProtocolsShared",
]
