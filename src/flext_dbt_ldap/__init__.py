# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Ldap package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

from flext_dbt_ldap.__version__ import __version__

if TYPE_CHECKING:
    from flext_meltano import d, e, h, r, x

    from flext_dbt_ldap import _constants, _models, _utilities, services
    from flext_dbt_ldap.__version__ import (
        FlextDbtLdapVersion,
        __author__,
        __author_email__,
        __description__,
        __license__,
        __title__,
        __url__,
        __version_info__,
    )
    from flext_dbt_ldap._config import FlextDbtLdapConfig, config
    from flext_dbt_ldap._settings import FlextDbtLdapSettings, settings
    from flext_dbt_ldap.api import FlextDbtLdap, dbt_ldap
    from flext_dbt_ldap.base import FlextDbtLdapServiceBase, s
    from flext_dbt_ldap.cli import main
    from flext_dbt_ldap.constants import FlextDbtLdapConstants, c
    from flext_dbt_ldap.models import FlextDbtLdapModels, m
    from flext_dbt_ldap.protocols import FlextDbtLdapProtocols, p
    from flext_dbt_ldap.typings import FlextDbtLdapTypes, t
    from flext_dbt_ldap.utilities import FlextDbtLdapUtilities, u


__all__: tuple[str, ...] = (
    "FlextDbtLdap",
    "FlextDbtLdapConfig",
    "FlextDbtLdapConstants",
    "FlextDbtLdapModels",
    "FlextDbtLdapProtocols",
    "FlextDbtLdapServiceBase",
    "FlextDbtLdapSettings",
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
    "_constants",
    "_models",
    "_utilities",
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

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "FlextDbtLdap": ".api",
        "FlextDbtLdapConfig": "._config",
        "FlextDbtLdapConstants": ".constants",
        "FlextDbtLdapModels": ".models",
        "FlextDbtLdapProtocols": ".protocols",
        "FlextDbtLdapServiceBase": ".base",
        "FlextDbtLdapSettings": "._settings",
        "FlextDbtLdapTypes": ".typings",
        "FlextDbtLdapUtilities": ".utilities",
        "FlextDbtLdapVersion": ".__version__",
        "__author__": ".__version__",
        "__author_email__": ".__version__",
        "__description__": ".__version__",
        "__license__": ".__version__",
        "__title__": ".__version__",
        "__url__": ".__version__",
        "__version_info__": ".__version__",
        "_constants": "._constants",
        "_models": "._models",
        "_utilities": "._utilities",
        "c": ".constants",
        "config": "._config",
        "d": "flext_meltano",
        "dbt_ldap": ".api",
        "e": "flext_meltano",
        "h": "flext_meltano",
        "m": ".models",
        "main": ".cli",
        "p": ".protocols",
        "r": "flext_meltano",
        "s": ".base",
        "services": ".services",
        "settings": "._settings",
        "t": ".typings",
        "u": ".utilities",
        "x": "flext_meltano",
    }),
    public_exports=__all__,
)
