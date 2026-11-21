"""Test type definitions for flext-dbt-ldap.

Provides TestsFlextDbtLdapTypes, combining TestsFlextTypes with
FlextDbtLdapTypes for test-specific type definitions.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Callable, MutableMapping
from pathlib import Path
from typing import TYPE_CHECKING

from flext_tests import FlextTestsTypes

from tests import FlextDbtLdapTypes

if TYPE_CHECKING:
    from tests import InMemoryDbtRunnerLdap


class TestsFlextDbtLdapTypes(FlextTestsTypes, FlextDbtLdapTypes):
    """Test types combining TestsFlextTypes with flext-dbt-ldap types."""

    class Tests(FlextTestsTypes.Tests):
        """Internal tests declarations."""

        type SyncState = MutableMapping[str, str] | None
        type ServiceFactory = Callable[
            [Path, SyncState],
            tuple[
                InMemoryDbtRunnerLdap,
                Path,
            ],
        ]


t = TestsFlextDbtLdapTypes
__all__: list[str] = ["TestsFlextDbtLdapTypes", "t"]
