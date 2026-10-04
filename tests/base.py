"""Service base for flext-dbt-ldap tests.

Copyright (c) 2026 FLEXT Team. All rights reserved.
tests/base
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import override

from flext_tests import FlextTestsServiceBase

from flext_dbt_ldap import m
from tests.settings import TestsFlextDbtLdapSettings


class TestsFlextDbtLdapServiceBase(FlextTestsServiceBase):
    """DBT LDAP test service base with source and test settings namespaces."""

    # NOTE (multi-agent): flext-tests owns fetch_settings; this project
    # declares only its more-specific bootstrap settings type.
    @classmethod
    @override
    def runtime_bootstrap_options(cls) -> m.RuntimeBootstrapOptions:
        return m.RuntimeBootstrapOptions(settings_type=TestsFlextDbtLdapSettings)


s = TestsFlextDbtLdapServiceBase

__all__: list[str] = ["TestsFlextDbtLdapServiceBase", "s"]
