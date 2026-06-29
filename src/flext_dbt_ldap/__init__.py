# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Ldap package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports
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
    from flext_dbt_ldap.api import FlextDbtLdap as FlextDbtLdap, dbt_ldap as dbt_ldap
    from flext_dbt_ldap.base import FlextDbtLdapServiceBase as FlextDbtLdapServiceBase
    from flext_dbt_ldap.constants import (
        FlextDbtLdapConstants as FlextDbtLdapConstants,
        c as c,
    )
    from flext_dbt_ldap.models import FlextDbtLdapModels as FlextDbtLdapModels, m as m
    from flext_dbt_ldap.protocols import (
        FlextDbtLdapProtocols as FlextDbtLdapProtocols,
        p as p,
    )
    from flext_dbt_ldap.settings import FlextDbtLdapSettings as FlextDbtLdapSettings
    from flext_dbt_ldap.typings import FlextDbtLdapTypes as FlextDbtLdapTypes, t as t
    from flext_dbt_ldap.utilities import (
        FlextDbtLdapUtilities as FlextDbtLdapUtilities,
        u as u,
    )
    from flext_meltano import d as d, e as e, h as h, r as r, s as s, x as x
_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".api": (
            "FlextDbtLdap",
            "dbt_ldap",
        ),
        ".base": ("FlextDbtLdapServiceBase",),
        ".constants": (
            "FlextDbtLdapConstants",
            "c",
        ),
        ".models": (
            "FlextDbtLdapModels",
            "m",
        ),
        ".protocols": (
            "FlextDbtLdapProtocols",
            "p",
        ),
        ".settings": ("FlextDbtLdapSettings",),
        ".typings": (
            "FlextDbtLdapTypes",
            "t",
        ),
        ".utilities": (
            "FlextDbtLdapUtilities",
            "u",
        ),
        "flext_meltano": (
            "d",
            "e",
            "h",
            "r",
            "s",
            "x",
        ),
    },
)


__all__: tuple[str, ...] = (
    "FlextDbtLdap",
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
    "d",
    "dbt_ldap",
    "e",
    "h",
    "m",
    "p",
    "r",
    "s",
    "t",
    "u",
    "x",
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    public_exports=__all__,
)
