"""Service base for flext-dbt-ldap tests."""

from __future__ import annotations

from typing import override

from flext_dbt_ldap import m
from flext_tests import s as tests_s
from tests.settings import TestsFlextDbtLdapSettings


class TestsFlextDbtLdapServiceBase(tests_s):
    """DBT LDAP test service base with source and test settings namespaces."""

    # NOTE (multi-agent): flext-tests owns fetch_settings; this project
    # declares only its more-specific bootstrap settings type.
    @classmethod
    @override
    def _runtime_bootstrap_options(cls) -> m.RuntimeBootstrapOptions:
        return m.RuntimeBootstrapOptions(settings_type=TestsFlextDbtLdapSettings)


s = TestsFlextDbtLdapServiceBase

__all__: list[str] = ["TestsFlextDbtLdapServiceBase", "s"]
