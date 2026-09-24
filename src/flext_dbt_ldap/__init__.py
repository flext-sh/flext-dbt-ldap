# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Ldap package."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

from .__version__ import (
    __author__ as __author__,
    __author_email__ as __author_email__,
    __description__ as __description__,
    __license__ as __license__,
    __title__ as __title__,
    __url__ as __url__,
    __version__ as __version__,
    __version_info__ as __version_info__,
)

if TYPE_CHECKING:
    from flext_meltano import d, e, h, r, x

    from . import services
    from ._config import FlextDbtLdapConfig, config
    from ._settings import FlextDbtLdapSettings, settings
    from .api import FlextDbtLdap, dbt_ldap
    from .base import FlextDbtLdapServiceBase, FlextDbtLdapServiceBase as s
    from .cli import main
    from .constants import FlextDbtLdapConstants, c
    from .models import FlextDbtLdapModels, m
    from .protocols import FlextDbtLdapProtocols, p
    from .services.client import FlextDbtLdapClientMixin
    from .services.sync import FlextDbtLdapSyncMixin
    from .typings import FlextDbtLdapTypes, t
    from .utilities import FlextDbtLdapUtilities, u


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
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
