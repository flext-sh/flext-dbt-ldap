"""Test protocol definitions for flext-dbt-ldap.

Provides FlextDbtLdapTestProtocols, combining FlextTestsProtocols with
FlextDbtLdapProtocols for test-specific protocol definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsProtocols

from flext_dbt_ldap.protocols import FlextDbtLdapProtocols


class FlextDbtLdapTestProtocols(FlextTestsProtocols, FlextDbtLdapProtocols):
    """Test protocols combining FlextTestsProtocols and FlextDbtLdapProtocols."""

    class DbtLdap(FlextDbtLdapProtocols.DbtLdap):
        """DbtLdap test protocols namespace."""

        class Tests:
            """DbtLdap-specific test protocols."""


p = FlextDbtLdapTestProtocols
__all__ = ["FlextDbtLdapTestProtocols", "p"]
