# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_tests import (
        api,
        cli,
        config,
        d,
        e,
        h,
        install_local_packages,
        main,
        r,
        settings,
        td,
        tf,
        tk,
        tm,
        u,
        x,
    )

    from flext_dbt_ldap import dbt_ldap, ldap, ldif, meltano
    from tests.base import TestsFlextDbtLdapServiceBase, s
    from tests.constants import TestsFlextDbtLdapConstants, c
    from tests.models import TestsFlextDbtLdapModels, m
    from tests.protocols import TestsFlextDbtLdapProtocols, p
    from tests.settings import TestsFlextDbtLdapSettings
    from tests.typings import TestsFlextDbtLdapTypes, t
    from tests.utilities import (
        InMemoryDbtRunnerLdap,
        InMemoryLdapDirectory,
        TestsFlextDbtLdapUtilities,
        tu,
    )


__all__: tuple[str, ...] = (
    "InMemoryDbtRunnerLdap",
    "InMemoryLdapDirectory",
    "TestsFlextDbtLdapConstants",
    "TestsFlextDbtLdapModels",
    "TestsFlextDbtLdapProtocols",
    "TestsFlextDbtLdapServiceBase",
    "TestsFlextDbtLdapSettings",
    "TestsFlextDbtLdapTypes",
    "TestsFlextDbtLdapUtilities",
    "api",
    "c",
    "cli",
    "config",
    "d",
    "dbt_ldap",
    "e",
    "h",
    "install_local_packages",
    "ldap",
    "ldif",
    "m",
    "main",
    "meltano",
    "p",
    "r",
    "s",
    "settings",
    "t",
    "td",
    "tf",
    "tk",
    "tm",
    "tu",
    "u",
    "x",
)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "InMemoryDbtRunnerLdap": ".utilities",
        "InMemoryLdapDirectory": ".utilities",
        "TestsFlextDbtLdapConstants": ".constants",
        "TestsFlextDbtLdapModels": ".models",
        "TestsFlextDbtLdapProtocols": ".protocols",
        "TestsFlextDbtLdapServiceBase": ".base",
        "TestsFlextDbtLdapSettings": ".settings",
        "TestsFlextDbtLdapTypes": ".typings",
        "TestsFlextDbtLdapUtilities": ".utilities",
        "api": "flext_tests",
        "c": ".constants",
        "cli": "flext_tests",
        "config": "flext_tests",
        "d": "flext_tests",
        "dbt_ldap": "flext_dbt_ldap",
        "e": "flext_tests",
        "h": "flext_tests",
        "install_local_packages": "flext_tests",
        "ldap": "flext_dbt_ldap",
        "ldif": "flext_dbt_ldap",
        "m": ".models",
        "main": "flext_tests",
        "meltano": "flext_dbt_ldap",
        "p": ".protocols",
        "r": "flext_tests",
        "s": ".base",
        "settings": "flext_tests",
        "t": ".typings",
        "td": "flext_tests",
        "tf": "flext_tests",
        "tk": "flext_tests",
        "tm": "flext_tests",
        "tu": ".utilities",
        "u": "flext_tests",
        "x": "flext_tests",
    }),
    public_exports=__all__,
)
