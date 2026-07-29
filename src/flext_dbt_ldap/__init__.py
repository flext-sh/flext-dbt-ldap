# @generated AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Ldap package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

from .__version__ import __author__ as __author__
from .__version__ import __author_email__ as __author_email__
from .__version__ import __description__ as __description__
from .__version__ import __license__ as __license__
from .__version__ import __title__ as __title__
from .__version__ import __url__ as __url__
from .__version__ import __version__ as __version__
from .__version__ import __version_info__ as __version_info__

if TYPE_CHECKING:
    from flext_ldap import d as d
    from flext_ldap import e as e
    from flext_ldap import h as h
    from flext_ldap import r as r
    from flext_ldap import x as x

    from ._config import FlextDbtLdapConfig as FlextDbtLdapConfig
    from ._config import config as config
    from ._settings import FlextDbtLdapSettings as FlextDbtLdapSettings
    from ._settings import settings as settings
    from .api import FlextDbtLdap as FlextDbtLdap
    from .api import dbt_ldap as dbt_ldap
    from .base import FlextDbtLdapServiceBase as FlextDbtLdapServiceBase

    s: type[FlextDbtLdapServiceBase]
    from .constants import FlextDbtLdapConstants as FlextDbtLdapConstants

    c: type[FlextDbtLdapConstants]
    from .models import FlextDbtLdapModels as FlextDbtLdapModels

    m: type[FlextDbtLdapModels]
    from .protocols import FlextDbtLdapProtocols as FlextDbtLdapProtocols

    p: type[FlextDbtLdapProtocols]
    from .typings import FlextDbtLdapTypes as FlextDbtLdapTypes

    t: type[FlextDbtLdapTypes]
    from .utilities import FlextDbtLdapUtilities as FlextDbtLdapUtilities

    u: type[FlextDbtLdapUtilities]

_LAZY_MODULES: dict[str, tuple[str, ...]] = {
    "._config": ("FlextDbtLdapConfig", "config"),
    "._settings": ("FlextDbtLdapSettings", "settings"),
    ".api": ("FlextDbtLdap", "dbt_ldap"),
    ".base": ("FlextDbtLdapServiceBase", "s"),
    ".constants": ("FlextDbtLdapConstants", "c"),
    ".models": ("FlextDbtLdapModels", "m"),
    ".protocols": ("FlextDbtLdapProtocols", "p"),
    ".typings": ("FlextDbtLdapTypes", "t"),
    ".utilities": ("FlextDbtLdapUtilities", "u"),
    "flext_ldap": ("d", "e", "h", "r", "x"),
}


_LAZY_ALIAS_GROUPS: dict[str, tuple[tuple[str, str], ...]] = {}


_LAZY_IMPORTS = build_lazy_import_map(
    _LAZY_MODULES, alias_groups=_LAZY_ALIAS_GROUPS, sort_keys=False
)

_PUBLIC_EXPORTS: tuple[str, ...] = (
    "FlextDbtLdap",
    "FlextDbtLdapConfig",
    "FlextDbtLdapConstants",
    "FlextDbtLdapModels",
    "FlextDbtLdapProtocols",
    "FlextDbtLdapServiceBase",
    "FlextDbtLdapSettings",
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
    "p",
    "r",
    "s",
    "settings",
    "t",
    "u",
    "x",
)

__all__: tuple[str, ...] = tuple(_PUBLIC_EXPORTS)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
