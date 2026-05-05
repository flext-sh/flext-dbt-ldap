# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Ldap package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import (
    build_lazy_import_map,
    install_lazy_exports,
    merge_lazy_imports,
)
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

if _t.TYPE_CHECKING:
    from flext_dbt_ldap._constants.attributes import FlextDbtLdapConstantsAttributes
    from flext_dbt_ldap._constants.base import FlextDbtLdapConstantsBase
    from flext_dbt_ldap._constants.search import FlextDbtLdapConstantsSearch
    from flext_dbt_ldap._constants.transformation import (
        FlextDbtLdapConstantsTransformation,
    )
    from flext_dbt_ldap._models.configuration import FlextDbtLdapModelsConfiguration
    from flext_dbt_ldap._models.dimensions import FlextDbtLdapModelsDimensions
    from flext_dbt_ldap._models.results import FlextDbtLdapModelsResults
    from flext_dbt_ldap._models.schema import FlextDbtLdapModelsSchema
    from flext_dbt_ldap._models.shared import FlextDbtLdapModelsShared
    from flext_dbt_ldap._utilities.client import FlextDbtLdapUtilitiesClient
    from flext_dbt_ldap._utilities.entry import FlextDbtLdapUtilitiesEntry
    from flext_dbt_ldap._utilities.integration import FlextDbtLdapUtilitiesIntegration
    from flext_dbt_ldap._utilities.macros import FlextDbtLdapUtilitiesMacros
    from flext_dbt_ldap._utilities.sync import FlextDbtLdapUtilitiesSync
    from flext_dbt_ldap.api import FlextDbtLdap, dbt_ldap
    from flext_dbt_ldap.base import FlextDbtLdapServiceBase
    from flext_dbt_ldap.constants import FlextDbtLdapConstants, c
    from flext_dbt_ldap.models import FlextDbtLdapModels, m
    from flext_dbt_ldap.protocols import FlextDbtLdapProtocols, p
    from flext_dbt_ldap.services.client import FlextDbtLdapClientMixin
    from flext_dbt_ldap.services.sync import FlextDbtLdapSyncMixin
    from flext_dbt_ldap.settings import FlextDbtLdapSettings
    from flext_dbt_ldap.typings import FlextDbtLdapTypes, t
    from flext_dbt_ldap.utilities import FlextDbtLdapUtilities, u
    from flext_meltano import d, e, h, r, s, x
_LAZY_IMPORTS = merge_lazy_imports(
    (
        "._constants",
        "._models",
        "._utilities",
        ".services",
    ),
    build_lazy_import_map(
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
            "flext_meltano": (
                "d",
                "e",
                "h",
                "r",
                "s",
                "x",
            ),
        },
    ),
    exclude_names=(
        "cleanup_submodule_namespace",
        "install_lazy_exports",
        "lazy_getattr",
        "logger",
        "merge_lazy_imports",
        "output",
        "output_reporting",
        "pytest_addoption",
        "pytest_collect_file",
        "pytest_collection_modifyitems",
        "pytest_configure",
        "pytest_runtest_setup",
        "pytest_runtest_teardown",
        "pytest_sessionfinish",
        "pytest_sessionstart",
        "pytest_terminal_summary",
        "pytest_warning_recorded",
    ),
    module_name=__name__,
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    [
        "__author__",
        "__author_email__",
        "__description__",
        "__license__",
        "__title__",
        "__url__",
        "__version__",
        "__version_info__",
    ],
)

__all__: list[str] = [
    "FlextDbtLdap",
    "FlextDbtLdapClientMixin",
    "FlextDbtLdapConstants",
    "FlextDbtLdapConstantsAttributes",
    "FlextDbtLdapConstantsBase",
    "FlextDbtLdapConstantsSearch",
    "FlextDbtLdapConstantsTransformation",
    "FlextDbtLdapModels",
    "FlextDbtLdapModelsConfiguration",
    "FlextDbtLdapModelsDimensions",
    "FlextDbtLdapModelsResults",
    "FlextDbtLdapModelsSchema",
    "FlextDbtLdapModelsShared",
    "FlextDbtLdapProtocols",
    "FlextDbtLdapServiceBase",
    "FlextDbtLdapSettings",
    "FlextDbtLdapSyncMixin",
    "FlextDbtLdapTypes",
    "FlextDbtLdapUtilities",
    "FlextDbtLdapUtilitiesClient",
    "FlextDbtLdapUtilitiesEntry",
    "FlextDbtLdapUtilitiesIntegration",
    "FlextDbtLdapUtilitiesMacros",
    "FlextDbtLdapUtilitiesSync",
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
]
