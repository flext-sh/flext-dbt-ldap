"""Test protocol definitions for flext-dbt-ldap.

Provides TestsFlextDbtLdapProtocols, combining FlextTestsProtocols with
FlextDbtLdapProtocols for test-specific protocol definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_dbt_ldap.protocols import FlextDbtLdapProtocols
from flext_tests.protocols import FlextTestsProtocols


class TestsFlextDbtLdapProtocols(FlextTestsProtocols, FlextDbtLdapProtocols):
    """Test protocols combining FlextTestsProtocols and FlextDbtLdapProtocols.

    Provides access to:
    - tp.Tests.Docker.* (from FlextTestsProtocols)
    - tp.Tests.Factory.* (from FlextTestsProtocols)
    - tp.DbtLdap.* (from FlextDbtLdapProtocols)
    """

    class Tests:
        """Project-specific test protocols.

        Extends FlextTestsProtocols.Tests with DbtLdap-specific protocols.
        """

        class DbtLdap:
            """DbtLdap-specific test protocols."""


# Runtime aliases
p = TestsFlextDbtLdapProtocols
tp = TestsFlextDbtLdapProtocols

__all__ = ["TestsFlextDbtLdapProtocols", "p", "tp"]
