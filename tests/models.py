"""Test models for flext-dbt-ldap.

Provides FlextDbtLdapTestModels, combining FlextTestsModels with
FlextDbtLdapModels for test-specific model definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsModels

from flext_dbt_ldap import FlextDbtLdapModels


class FlextDbtLdapTestModels(FlextTestsModels, FlextDbtLdapModels):
    """Test models combining FlextTestsModels with flext-dbt-ldap models."""


m = FlextDbtLdapTestModels

__all__ = [
    "FlextDbtLdapTestModels",
    "m",
]
