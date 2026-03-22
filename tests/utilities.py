"""Test utilities for flext-dbt-ldap.

Provides FlextDbtLdapTestUtilities, combining FlextTestsUtilities with
FlextDbtLdapUtilities for test-specific utility definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsUtilities

from flext_dbt_ldap import FlextDbtLdapUtilities


class FlextDbtLdapTestUtilities(FlextTestsUtilities, FlextDbtLdapUtilities):
    """Test utilities combining FlextTestsUtilities with flext-dbt-ldap utilities."""

    class DbtLdap(FlextDbtLdapUtilities.DbtLdap):
        """DbtLdap test utilities namespace."""

        class Tests:
            """Internal tests declarations."""


u = FlextDbtLdapTestUtilities
__all__ = ["FlextDbtLdapTestUtilities", "u"]
