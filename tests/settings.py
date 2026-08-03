"""Runtime settings for flext-dbt-ldap tests."""

from __future__ import annotations

from flext_dbt_ldap import FlextDbtLdapSettings
from flext_tests import FlextTestsSettings


class TestsFlextDbtLdapSettings(FlextDbtLdapSettings, FlextTestsSettings):
    """DBT LDAP settings extended with the shared test namespace."""


__all__: list[str] = ["TestsFlextDbtLdapSettings"]
