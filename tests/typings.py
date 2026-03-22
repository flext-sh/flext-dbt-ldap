"""Test type definitions for flext-dbt-ldap.

Provides FlextDbtLdapTestTypes, combining FlextTestsTypes with
FlextDbtLdapTypes for test-specific type definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsTypes

from flext_dbt_ldap import FlextDbtLdapTypes


class FlextDbtLdapTestTypes(FlextTestsTypes, FlextDbtLdapTypes):
    """Test types combining FlextTestsTypes with flext-dbt-ldap types."""

    class DbtLdap(FlextDbtLdapTypes.DbtLdap):
        """DbtLdap test types namespace."""

        class Tests:
            """Internal tests declarations."""


t = FlextDbtLdapTestTypes
__all__ = ["FlextDbtLdapTestTypes", "t"]
