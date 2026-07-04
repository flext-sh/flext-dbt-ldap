# AUTO-GENERATED FILE — Regenerate with: make gen
"""Lazy export map part."""

from __future__ import annotations

from flext_core.lazy import build_lazy_import_map

FLEXT_DBT_LDAP_LAZY_IMPORTS_PART_01 = build_lazy_import_map(
    {
        "._constants": ("_constants",),
        "._models": ("_models",),
        "._utilities": ("_utilities",),
        ".api": (
            "FlextDbtLdap",
            "dbt_ldap",
        ),
        ".base": (
            "FlextDbtLdapServiceBase",
            "s",
        ),
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
        ".services": ("services",),
        ".services.client": ("FlextDbtLdapClientMixin",),
        ".services.sync": ("FlextDbtLdapSyncMixin",),
        ".settings": ("FlextDbtLdapSettings",),
        ".typings": (
            "FlextDbtLdapTypes",
            "t",
        ),
        ".utilities": (
            "FlextDbtLdapUtilities",
            "u",
        ),
        "flext_ldap": (
            "d",
            "e",
            "h",
            "r",
            "x",
        ),
    },
)

__all__: list[str] = ["FLEXT_DBT_LDAP_LAZY_IMPORTS_PART_01"]
