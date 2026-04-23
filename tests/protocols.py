"""Test protocol definitions for flext-dbt-ldap.

Provides TestsFlextDbtLdapProtocols, combining TestsFlextProtocols with
FlextDbtLdapProtocols for test-specific protocol definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import (
    Sequence,
)
from contextlib import AbstractContextManager
from typing import Protocol, runtime_checkable

from flext_tests import FlextTestsProtocols

from flext_dbt_ldap import FlextDbtLdapProtocols, FlextDbtLdapTypes


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
            params: tuple[str, ...] | None = None,
        ) -> TestsFlextDbtLdapProtocols.DbCursor: ...

        def fetchall(
            self,
        ) -> Sequence[tuple[FlextDbtLdapTypes.JsonValue, ...]]: ...

        def fetchone(
            self,
        ) -> tuple[FlextDbtLdapTypes.JsonValue, ...] | None: ...

    @runtime_checkable
    class DbConnection(Protocol):
        """DB-API 2.0 connection protocol for type-safe database operations."""

        autocommit: bool

        def cursor(
            self,
        ) -> AbstractContextManager[TestsFlextDbtLdapProtocols.DbCursor]: ...

        def close(self) -> None: ...


p = TestsFlextDbtLdapProtocols
__all__: list[str] = ["TestsFlextDbtLdapProtocols", "p"]
