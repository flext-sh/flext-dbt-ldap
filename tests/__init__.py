# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_ldap import adapters, ldap, ldif, servers
    from flext_meltano import meltano
    from flext_tests import (
        api,
        cli,
        config,
        core,
        d,
        e,
        h,
        install_local_packages,
        lazy_attribute,
        load_infra_report,
        r,
        services,
        settings,
        td,
        tf,
        tk,
        tm,
        tv,
        x,
    )

    from flext_dbt_ldap import dbt_ldap, main

    from . import e2e, unit
    from .base import TestsFlextDbtLdapServiceBase, TestsFlextDbtLdapServiceBase as s
    from .constants import TestsFlextDbtLdapConstants, TestsFlextDbtLdapConstants as c
    from .models import TestsFlextDbtLdapModels, TestsFlextDbtLdapModels as m
    from .protocols import TestsFlextDbtLdapProtocols, TestsFlextDbtLdapProtocols as p
    from .settings import TestsFlextDbtLdapSettings
    from .typings import TestsFlextDbtLdapTypes, TestsFlextDbtLdapTypes as t
    from .utilities import TestsFlextDbtLdapUtilities, u


__all__: tuple[str, ...] = (
    "TestsFlextDbtLdapConstants",
    "TestsFlextDbtLdapModels",
    "TestsFlextDbtLdapProtocols",
    "TestsFlextDbtLdapServiceBase",
    "TestsFlextDbtLdapSettings",
    "TestsFlextDbtLdapTypes",
    "TestsFlextDbtLdapUtilities",
    "adapters",
    "api",
    "c",
    "cli",
    "config",
    "core",
    "d",
    "dbt_ldap",
    "e",
    "e2e",
    "h",
    "install_local_packages",
    "lazy_attribute",
    "ldap",
    "ldif",
    "load_infra_report",
    "m",
    "main",
    "meltano",
    "p",
    "r",
    "s",
    "servers",
    "services",
    "settings",
    "t",
    "td",
    "tf",
    "tk",
    "tm",
    "tv",
    "u",
    "unit",
    "x",
)

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            ".base": ("TestsFlextDbtLdapServiceBase", "s"),
            ".constants": ("TestsFlextDbtLdapConstants", "c"),
            ".e2e": ("e2e",),
            ".models": ("TestsFlextDbtLdapModels", "m"),
            ".protocols": ("TestsFlextDbtLdapProtocols", "p"),
            ".settings": ("TestsFlextDbtLdapSettings",),
            ".typings": ("TestsFlextDbtLdapTypes", "t"),
            ".unit": ("unit",),
            ".utilities": ("TestsFlextDbtLdapUtilities", "u"),
            "flext_dbt_ldap": ("dbt_ldap", "main"),
            "flext_ldap": ("adapters", "ldap", "ldif", "servers"),
            "flext_meltano": ("meltano",),
            "flext_tests": (
                "api",
                "cli",
                "config",
                "core",
                "d",
                "e",
                "h",
                "install_local_packages",
                "lazy_attribute",
                "load_infra_report",
                "r",
                "services",
                "settings",
                "td",
                "tf",
                "tk",
                "tm",
                "tv",
                "x",
            ),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
