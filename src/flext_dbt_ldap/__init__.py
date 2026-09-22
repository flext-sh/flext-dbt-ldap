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
    from flext_cli import cli
    from flext_ldap import ldap
    from flext_ldif import ldif
    from flext_meltano import main, meltano
    from pydantic_core import from_json, to_json, to_jsonable_python

    from flext_core import core, d, e, h, lazy_attribute, r, x

    from . import services
    from .__version__ import FlextDbtLdapVersion
    from ._config import FlextDbtLdapConfig, config
    from ._settings import FlextDbtLdapSettings, settings
    from .api import FlextDbtLdap, dbt_ldap
    from .base import FlextDbtLdapServiceBase, FlextDbtLdapServiceBase as s
    from .constants import FlextDbtLdapConstants, FlextDbtLdapConstants as c
    from .models import FlextDbtLdapModels, FlextDbtLdapModels as m
    from .protocols import FlextDbtLdapProtocols, FlextDbtLdapProtocols as p
    from .services.client import FlextDbtLdapClientMixin
    from .services.sync import FlextDbtLdapSyncMixin
    from .typings import FlextDbtLdapTypes, FlextDbtLdapTypes as t
    from .utilities import FlextDbtLdapUtilities, FlextDbtLdapUtilities as u
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
    "FlextDbtLdapVersion",
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
            ".__version__": ("FlextDbtLdapVersion",),
            "._config": ("FlextDbtLdapConfig", "config"),
            "._settings": ("FlextDbtLdapSettings", "settings"),
            ".api": ("FlextDbtLdap", "dbt_ldap"),
            ".base": ("FlextDbtLdapServiceBase", "s"),
            ".constants": ("FlextDbtLdapConstants", "c"),
            ".models": ("FlextDbtLdapModels", "m"),
            ".protocols": ("FlextDbtLdapProtocols", "p"),
            ".services": ("services",),
            ".services.client": ("FlextDbtLdapClientMixin",),
            ".services.sync": ("FlextDbtLdapSyncMixin",),
            ".typings": ("FlextDbtLdapTypes", "t"),
            ".utilities": ("FlextDbtLdapUtilities", "u"),
            "flext_cli": ("cli",),
            "flext_core": ("core", "d", "e", "h", "lazy_attribute", "r", "x"),
            "flext_ldap": ("ldap",),
            "flext_ldif": ("ldif",),
            "flext_meltano": ("main", "meltano"),
            "pydantic_core": ("from_json", "to_json", "to_jsonable_python"),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
