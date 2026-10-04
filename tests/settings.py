"""Runtime settings for flext-dbt-ldap tests.

Copyright (c) 2026 FLEXT Team. All rights reserved.
tests/settings
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsSettings

from flext_dbt_ldap import FlextDbtLdapSettings


class TestsFlextDbtLdapSettings(FlextDbtLdapSettings, FlextTestsSettings):
    """DBT LDAP settings extended with the shared test namespace."""


__all__: list[str] = ["TestsFlextDbtLdapSettings"]
