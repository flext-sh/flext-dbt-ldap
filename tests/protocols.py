"""Test protocol definitions for flext-dbt-ldap.

Provides TestsFlextDbtLdapProtocols, combining p with
FlextDbtLdapProtocols for test-specific protocol definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import p

from flext_dbt_ldap.protocols import FlextDbtLdapProtocols


class TestsFlextDbtLdapProtocols(p, FlextDbtLdapProtocols):
    """Test protocols combining p and FlextDbtLdapProtocols.

    Provides access to:
    - p.Tests.Docker.* (from p)
    - p.Tests.Factory.* (from p)
    - p.DbtLdap.* (from FlextDbtLdapProtocols)
    """

    class Tests(p.Tests):
        """Project-specific test protocols.

        Extends p.Tests with DbtLdap-specific protocols.
        """

        class DbtLdap:
            """DbtLdap-specific test protocols."""


__all__ = ["TestsFlextDbtLdapProtocols", "p"]

p = TestsFlextDbtLdapProtocols
