# AUTO-GENERATED FILE — Regenerate with: make gen
"""Source-derived structural model contracts.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_ldap/_protocols/dimensions
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from flext_dbt_ldap._protocols import FlextDbtLdapProtocolsShared


class FlextDbtLdapProtocolsDimensions:
    """Own the structural contracts declared by its model source."""

    @runtime_checkable
    class UserDimension(FlextDbtLdapProtocolsShared.DbtDimensionBase, Protocol):
        """Structural data contract projected from the owning model."""

        user_id: str
        email: str | None
        display_name: str | None
        department: str | None
        manager_dn: str | None
        employee_number: str | None
        phone: str | None

    @runtime_checkable
    class GroupDimension(FlextDbtLdapProtocolsShared.DbtDimensionBase, Protocol):
        """Structural data contract projected from the owning model."""

        group_id: str
        description: str | None
        group_type: str | None
        member_count: int

    @runtime_checkable
    class MembershipFact(FlextDbtLdapProtocolsShared.DbtSerializable, Protocol):
        """Structural data contract projected from the owning model."""

        user_dn: str
        group_dn: str
        membership_type: str
        is_primary: bool
        effective_date: str | None
        expiry_date: str | None


__all__: list[str] = [
    "FlextDbtLdapProtocolsDimensions",
]
