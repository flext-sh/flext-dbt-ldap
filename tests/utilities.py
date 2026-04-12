"""Test utilities for flext-dbt-ldap.

Provides TestsFlextDbtLdapUtilities, combining TestsFlextUtilities with
FlextDbtLdapUtilities for test-specific utility definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsUtilities

from flext_dbt_ldap import FlextDbtLdapUtilities


class TestsFlextDbtLdapUtilities(FlextTestsUtilities, FlextDbtLdapUtilities):
    """Test utilities combining TestsFlextUtilities with flext-dbt-ldap utilities."""

    class DbtLdap(FlextDbtLdapUtilities.DbtLdap):
        """DbtLdap test utilities namespace."""

        class Tests:
            """Internal tests declarations."""


u = TestsFlextDbtLdapUtilities
__all__: list[str] = ["TestsFlextDbtLdapUtilities", "u"]
