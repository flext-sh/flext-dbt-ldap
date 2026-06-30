# AUTO-GENERATED FILE — Regenerate with: make gen
"""Lazy export map part."""

from __future__ import annotations

from flext_core.lazy import build_lazy_import_map

FLEXT_DBT_LDAP_LAZY_IMPORTS_PART_01 = build_lazy_import_map(
    {
        "._constants.attributes": ("FlextDbtLdapConstantsAttributes",),
        "._constants.base": ("FlextDbtLdapConstantsBase",),
        "._constants.search": ("FlextDbtLdapConstantsSearch",),
        "._constants.transformation": ("FlextDbtLdapConstantsTransformation",),
        "._models.configuration": ("FlextDbtLdapModelsConfiguration",),
        "._models.dimensions": ("FlextDbtLdapModelsDimensions",),
        "._models.results": ("FlextDbtLdapModelsResults",),
        "._models.schema": ("FlextDbtLdapModelsSchema",),
        "._models.shared": ("FlextDbtLdapModelsShared",),
        "._utilities.client": ("FlextDbtLdapUtilitiesClient",),
        "._utilities.entry": ("FlextDbtLdapUtilitiesEntry",),
        "._utilities.integration": ("FlextDbtLdapUtilitiesIntegration",),
        "._utilities.macros": ("FlextDbtLdapUtilitiesMacros",),
        "._utilities.sync": ("FlextDbtLdapUtilitiesSync",),
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
    },
)

__all__: list[str] = ["FLEXT_DBT_LDAP_LAZY_IMPORTS_PART_01"]
