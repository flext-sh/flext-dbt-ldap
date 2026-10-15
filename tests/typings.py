"""Test type definitions for flext-dbt-ldap.

Provides TestsFlextDbtLdapTypes, combining TestsFlextTypes with
FlextDbtLdapTypes for test-specific type definitions.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path
from typing import TYPE_CHECKING

from flext_tests import FlextTestsTypes

from flext_dbt_ldap import FlextDbtLdapTypes

if TYPE_CHECKING:
    from tests import InMemoryDbtRunnerLdap


class TestsFlextDbtLdapTypes(FlextTestsTypes, FlextDbtLdapTypes):
    """Test types combining TestsFlextTypes with flext-dbt-ldap types."""

    class DbtLdap(FlextDbtLdapTypes.DbtLdap):
        """DbtLdap test types namespace."""

        class Tests:
            """Internal tests declarations."""

            type SyncState = FlextDbtLdapTypes.MutableMappingKV[str, str] | None
            type ServiceFactory = Callable[
                [Path, SyncState],
                FlextDbtLdapTypes.Pair[
                    InMemoryDbtRunnerLdap,
                    Path,
                ],
            ]


t = TestsFlextDbtLdapTypes
__all__: list[str] = ["TestsFlextDbtLdapTypes", "t"]
