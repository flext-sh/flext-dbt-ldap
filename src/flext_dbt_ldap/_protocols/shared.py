# AUTO-GENERATED FILE — Regenerate with: make gen
"""Source-derived structural model contracts.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_ldap/_protocols/shared
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Sequence
from datetime import datetime
from typing import TYPE_CHECKING, Protocol, runtime_checkable

from flext_meltano import FlextMeltanoProtocols

if TYPE_CHECKING:
    from flext_core import p

    from flext_dbt_ldap import t


class FlextDbtLdapProtocolsShared:
    """Own the structural contracts declared by its model source."""

    @runtime_checkable
    class DbtSerializable(FlextMeltanoProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        version: t.NonNegativeInt
        unique_id: t.NonEmptyStr

        @property
        def created_at(self) -> datetime:
            """Creation timestamp (configured timezone)."""
            ...

        updated_at: datetime | None

        @property
        def domain_events(self) -> Sequence[p.DomainEvent]:
            """List of uncommitted domain events for event sourcing."""
            ...

        def to_dbt_dict(self) -> t.ConfigurationMapping:
            """Dump models to DBT-friendly dictionaries."""
            ...

    @runtime_checkable
    class DbtDimensionBase(DbtSerializable, Protocol):
        """Structural data contract projected from the owning model."""

        common_name: str
        is_active: bool
        created_date: str | None
        modified_date: str | None


__all__: list[str] = [
    "FlextDbtLdapProtocolsShared",
]
