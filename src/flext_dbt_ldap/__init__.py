# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Ldap package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core import build_lazy_import_map, install_lazy_exports
from flext_dbt_ldap.__version__ import (
    __author__,
    __author_email__,
    __description__,
    __license__,
    __title__,
    __url__,
    __version__,
    __version_info__,
)

if TYPE_CHECKING:
    from flext_meltano import d, e, h, r, x

    from flext_dbt_ldap import services
    from flext_dbt_ldap._config import FlextDbtLdapConfig, config
    from flext_dbt_ldap._settings import FlextDbtLdapSettings, settings
    from flext_dbt_ldap.api import FlextDbtLdap, dbt_ldap
    from flext_dbt_ldap.base import FlextDbtLdapServiceBase, s
    from flext_dbt_ldap.cli import main
    from flext_dbt_ldap.constants import FlextDbtLdapConstants, c
    from flext_dbt_ldap.models import FlextDbtLdapModels, m
    from flext_dbt_ldap.protocols import FlextDbtLdapProtocols, p
    from flext_dbt_ldap.services.client import FlextDbtLdapClientMixin
    from flext_dbt_ldap.services.sync import FlextDbtLdapSyncMixin
    from flext_dbt_ldap.typings import FlextDbtLdapTypes, t
    from flext_dbt_ldap.utilities import FlextDbtLdapUtilities, u


__all__: tuple[str, ...] = (
    "FlextDbtLdap",
    "FlextDbtLdapClientMixin",
    "FlextDbtLdapConfig",
    "FlextDbtLdapConstants",
    "FlextDbtLdapModels",
    "FlextDbtLdapProtocols",
    "FlextDbtLdapServiceBase",
    "FlextDbtLdapSettings",
    "FlextDbtLdapSyncMixin",
    "FlextDbtLdapTypes",
    "FlextDbtLdapUtilities",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "c",
    "config",
    "d",
    "dbt_ldap",
    "e",
    "h",
    "m",
    "main",
    "p",
    "r",
    "s",
    "services",
    "settings",
    "t",
    "u",
    "x",
)

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            "._config": ("FlextDbtLdapConfig", "config"),
            "._settings": ("FlextDbtLdapSettings", "settings"),
            ".api": ("FlextDbtLdap", "dbt_ldap"),
            ".base": ("FlextDbtLdapServiceBase", "s"),
            ".cli": ("main",),
            ".constants": ("FlextDbtLdapConstants", "c"),
            ".models": ("FlextDbtLdapModels", "m"),
            ".protocols": ("FlextDbtLdapProtocols", "p"),
            ".services": ("services",),
            ".services.client": ("FlextDbtLdapClientMixin",),
            ".services.sync": ("FlextDbtLdapSyncMixin",),
            ".typings": ("FlextDbtLdapTypes", "t"),
            ".utilities": ("FlextDbtLdapUtilities", "u"),
            "flext_meltano": ("d", "e", "h", "r", "x"),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    ),
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
