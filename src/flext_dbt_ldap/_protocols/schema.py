# AUTO-GENERATED FILE — Regenerate with: make gen
"""Source-derived structural model contracts.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_ldap/_protocols/schema
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING, Protocol, runtime_checkable

from flext_meltano import FlextMeltanoProtocols

if TYPE_CHECKING:
    from flext_dbt_ldap import t


class FlextDbtLdapProtocolsSchema:
    """Own the structural contracts declared by its model source."""

    @runtime_checkable
    class DbtModelDefinition(FlextMeltanoProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def version(self) -> str:
            """DBT schema.yml version."""
            ...

        @property
        def models(self) -> Sequence[t.JsonMapping]:
            """DBT model definitions."""
            ...

    @runtime_checkable
    class DbtTestConfig(FlextMeltanoProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def version(self) -> str:
            """DBT schema.yml version."""
            ...

        @property
        def models(self) -> Sequence[t.JsonMapping]:
            """DBT test model definitions."""
            ...

        @property
        def columns(self) -> t.Ldap.OperationAttributes:
            """Column-level DBT tests keyed by attribute name."""
            ...

    @runtime_checkable
    class TransformationConfig(FlextMeltanoProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def source_table(self) -> str:
            """Source table used by the transformation."""
            ...

        @property
        def transformations(self) -> Mapping[str, str]:
            """Column transformation expressions."""
            ...

        @property
        def filters(self) -> Sequence[str]:
            """Filter expressions applied before transformation."""
            ...

    @runtime_checkable
    class TransformationRule(FlextMeltanoProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def name(self) -> str:
            """Transformation rule name."""
            ...

        @property
        def rules(self) -> Mapping[str, str]:
            """Named transformation rules."""
            ...

    @runtime_checkable
    class DataValidationConfig(FlextMeltanoProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def min_quality_threshold(self) -> t.NonNegativeFloat:
            """Minimum validation score accepted for LDAP data."""
            ...

        @property
        def required_attributes(self) -> Sequence[str]:
            """LDAP attributes required for a valid entry."""
            ...

        @property
        def validate_dns(self) -> bool:
            """Whether distinguished names must be present."""
            ...

        @property
        def columns(self) -> t.Ldap.OperationAttributes:
            """Column validation configuration keyed by attribute."""
            ...

    @runtime_checkable
    class LdapSchema(FlextMeltanoProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def object_classes(self) -> Sequence[str]:
            """LDAP object classes associated with the schema."""
            ...

        @property
        def required_attributes(self) -> Sequence[str]:
            """LDAP attributes required by the schema."""
            ...

    @runtime_checkable
    class LdapQuery(FlextMeltanoProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def base_dn(self) -> str:
            """LDAP base DN for the query."""
            ...

        @property
        def filter_str(self) -> str:
            """LDAP search filter."""
            ...

        @property
        def attributes(self) -> Sequence[str]:
            """LDAP attributes requested by the query."""
            ...

        @property
        def scope(self) -> str:
            """LDAP search scope."""
            ...


__all__: list[str] = [
    "FlextDbtLdapProtocolsSchema",
]
