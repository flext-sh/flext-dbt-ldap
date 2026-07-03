"""Service base for flext-dbt-ldap tests."""

from __future__ import annotations

from typing import override

from flext_tests import s as tests_s

from flext_dbt_ldap import m
from tests.settings import TestsFlextDbtLdapSettings


class TestsFlextDbtLdapServiceBase(tests_s):
    """DBT LDAP test service base with source and test settings namespaces."""

    @classmethod
    @override
    def fetch_settings(cls) -> TestsFlextDbtLdapSettings:
        """Return the typed DBT LDAP+Tests settings singleton."""
        return TestsFlextDbtLdapSettings.fetch_global()

    @classmethod
    @override
    def _runtime_bootstrap_options(cls) -> m.RuntimeBootstrapOptions:
        return m.RuntimeBootstrapOptions(settings_type=TestsFlextDbtLdapSettings)


s = TestsFlextDbtLdapServiceBase

__all__: list[str] = ["TestsFlextDbtLdapServiceBase", "s"]
