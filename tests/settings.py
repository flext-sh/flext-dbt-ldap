"""Runtime settings for flext-dbt-ldap tests."""

from __future__ import annotations

from flext_tests.settings import FlextTestsSettings

from flext_dbt_ldap import FlextDbtLdapSettings


class TestsFlextDbtLdapSettings(FlextDbtLdapSettings, FlextTestsSettings):
    """DBT LDAP settings extended with the shared test namespace."""


__all__: list[str] = ["TestsFlextDbtLdapSettings"]
