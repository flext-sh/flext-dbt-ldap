"""Test models for flext-dbt-ldap.

Provides TestsFlextDbtLdapModels, combining TestsFlextModels with
FlextDbtLdapModels for test-specific model definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsModels

from flext_dbt_ldap import FlextDbtLdapModels


class TestsFlextDbtLdapModels(FlextTestsModels, FlextDbtLdapModels):
    """Test models combining FlextTestsModels with flext-dbt-ldap models."""

    class DbtLdap(FlextDbtLdapModels.DbtLdap):
        """DbtLdap test models namespace."""

        class Tests:
            """Test-specific models."""


m = TestsFlextDbtLdapModels

__all__: list[str] = [
    "TestsFlextDbtLdapModels",
    "m",
]
