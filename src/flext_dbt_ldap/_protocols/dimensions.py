# AUTO-GENERATED FILE — Regenerate with: make gen
"""Source-derived structural model contracts.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_ldap/_protocols/dimensions
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Protocol, runtime_checkable

from flext_meltano import FlextMeltanoProtocols

from flext_dbt_ldap import t

if TYPE_CHECKING:
    from flext_core import p


class FlextDbtLdapProtocolsDimensions:
    """Own the structural contracts declared by its model source."""

    @runtime_checkable
    class UserDimension(FlextMeltanoProtocols.Model, Protocol):
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

        @property
        def user_id(self) -> str:
            """Canonical user identifier."""
            ...

        @property
        def email(self) -> str | None:
            """Primary user email."""
            ...

        @property
        def display_name(self) -> str | None:
            """Display name shown to users."""
            ...

        @property
        def department(self) -> str | None:
            """User department name."""
            ...

        @property
        def manager_dn(self) -> str | None:
            """Distinguished name of the manager."""
            ...

        @property
        def employee_number(self) -> str | None:
            """Employee number from LDAP."""
            ...

        @property
        def phone(self) -> str | None:
            """Primary phone number."""
            ...

        def to_dbt_dict(self) -> t.ConfigurationMapping:
            """Dump models to DBT-friendly dictionaries."""
            ...

    @runtime_checkable
    class GroupDimension(FlextMeltanoProtocols.Model, Protocol):
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

        @property
        def group_id(self) -> str:
            """Canonical group identifier."""
            ...

        @property
        def description(self) -> str | None:
            """Group description from LDAP."""
            ...

        @property
        def group_type(self) -> str | None:
            """Group type classification."""
            ...

        @property
        def member_count(self) -> int:
            """Number of direct group members."""
            ...

        def to_dbt_dict(self) -> t.ConfigurationMapping:
            """Dump models to DBT-friendly dictionaries."""
            ...

    @runtime_checkable
    class MembershipFact(FlextMeltanoProtocols.Model, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def domain_events(self) -> Sequence[p.DomainEvent]:
            """List of uncommitted domain events for event sourcing."""
            ...

        @property
        def user_dn(self) -> str:
            """Member distinguished name."""
            ...

        @property
        def group_dn(self) -> str:
            """Group distinguished name."""
            ...

        @property
        def membership_type(self) -> str:
            """Membership relationship type."""
            ...

        @property
        def is_primary(self) -> bool:
            """Whether the membership is the primary assignment."""
            ...

        @property
        def effective_date(self) -> str | None:
            """Membership effective timestamp."""
            ...

        @property
        def expiry_date(self) -> str | None:
            """Membership expiry timestamp."""
            ...

        def to_dbt_dict(self) -> t.ConfigurationMapping:
            """Dump models to DBT-friendly dictionaries."""
            ...


__all__: list[str] = [
    "FlextDbtLdapProtocolsDimensions",
]
