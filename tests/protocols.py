"""Test protocol definitions for flext-dbt-ldap.

Provides FlextDbtLdapTestProtocols, combining FlextTestsProtocols with
FlextDbtLdapProtocols for test-specific protocol definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Sequence
from contextlib import AbstractContextManager
from typing import Protocol, runtime_checkable

from flext_tests import FlextTestsProtocols

from flext_dbt_ldap import t
from flext_dbt_ldap.protocols import FlextDbtLdapProtocols


class FlextDbtLdapTestProtocols(FlextTestsProtocols, FlextDbtLdapProtocols):
    """Test protocols combining FlextTestsProtocols and FlextDbtLdapProtocols."""

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
        ) -> FlextDbtLdapTestProtocols.DbCursor: ...

        def fetchall(self) -> Sequence[tuple[t.NormalizedValue, ...]]: ...

        def fetchone(self) -> tuple[t.NormalizedValue, ...] | None: ...

    @runtime_checkable
    class DbConnection(Protocol):
        """DB-API 2.0 connection protocol for type-safe database operations."""

        autocommit: bool

        def cursor(
            self,
        ) -> AbstractContextManager[FlextDbtLdapTestProtocols.DbCursor]: ...

        def close(self) -> None: ...


p = FlextDbtLdapTestProtocols
__all__ = ["FlextDbtLdapTestProtocols", "p"]
