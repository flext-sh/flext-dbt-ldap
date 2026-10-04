"""Test protocol definitions for flext-dbt-ldap.

Provides TestsFlextDbtLdapProtocols, combining TestsFlextProtocols with
FlextDbtLdapProtocols for test-specific protocol definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, runtime_checkable

from flext_tests import FlextTestsProtocols

from flext_dbt_ldap import FlextDbtLdapProtocols, FlextDbtLdapTypes, t

if TYPE_CHECKING:
    from contextlib import AbstractContextManager


class TestsFlextDbtLdapProtocols(FlextTestsProtocols, FlextDbtLdapProtocols):
    """Test protocols combining TestsFlextProtocols and FlextDbtLdapProtocols."""

    class DbtLdap(FlextDbtLdapProtocols.DbtLdap):
        """DbtLdap test protocols namespace."""

        class Tests:
            """DbtLdap-specific test protocols."""

    @runtime_checkable
    class DbCursor(Protocol):
        """DB-API 2.0 cursor protocol for type-safe database operations."""

        def execute(
            self,
            query: str | object,
            params: t.StrSequence | None = None,
        ) -> TestsFlextDbtLdapProtocols.DbCursor:
            """Provide ``execute``."""
            ...

        def fetchall(self) -> t.SequenceOf[tuple[FlextDbtLdapTypes.JsonValue, ...]]:
            """Provide ``fetchall``."""
            ...

        def fetchone(self) -> tuple[FlextDbtLdapTypes.JsonValue, ...] | None:
            """Provide ``fetchone``."""
            ...

    @runtime_checkable
    class DbConnection(Protocol):
        """DB-API 2.0 connection protocol for type-safe database operations."""

        autocommit: bool

        def cursor(
            self,
        ) -> AbstractContextManager[TestsFlextDbtLdapProtocols.DbCursor]:
            """Provide ``cursor``."""
            ...

        def close(self) -> None:
            """Provide ``close``."""
            ...


p = TestsFlextDbtLdapProtocols
__all__: list[str] = ["TestsFlextDbtLdapProtocols", "p"]
