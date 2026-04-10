# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Ldap package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import (
    build_lazy_import_map,
    install_lazy_exports,
    merge_lazy_imports,
)
from flext_dbt_ldap.__version__ import *

if _t.TYPE_CHECKING:
    from flext_core.decorators import d
    from flext_core.exceptions import e
    from flext_core.handlers import h
    from flext_core.mixins import x
    from flext_core.result import r
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
    from flext_dbt_ldap.api import FlextDbtLdap
    from flext_dbt_ldap.base import (
        FlextDbtLdapServiceBase,
        FlextDbtLdapServiceBase as s,
    )
    from flext_dbt_ldap.constants import (
        FlextDbtLdapConstants,
        FlextDbtLdapConstants as c,
    )
    from flext_dbt_ldap.errors import (
        FlextDbtLdapAuthenticationError,
        FlextDbtLdapConfigurationError,
        FlextDbtLdapConnectionError,
        FlextDbtLdapError,
        FlextDbtLdapMacroError,
        FlextDbtLdapModelError,
        FlextDbtLdapProcessingError,
        FlextDbtLdapTestError,
        FlextDbtLdapTimeoutError,
        FlextDbtLdapValidationError,
    )
    from flext_dbt_ldap.models import FlextDbtLdapModels, FlextDbtLdapModels as m
    from flext_dbt_ldap.protocols import (
        FlextDbtLdapProtocols,
        FlextDbtLdapProtocols as p,
    )
    from flext_dbt_ldap.settings import FlextDbtLdapSettings
    from flext_dbt_ldap.typings import FlextDbtLdapTypes, FlextDbtLdapTypes as t
    from flext_dbt_ldap.utilities import (
        FlextDbtLdapUtilities,
        FlextDbtLdapUtilities as u,
    )
_LAZY_IMPORTS = merge_lazy_imports(
    (
        "._constants",
        "._models",
        "._utilities",
    ),
    build_lazy_import_map(
        {
            ".__version__": (
                "__author__",
                "__author_email__",
                "__description__",
                "__license__",
                "__title__",
                "__url__",
                "__version__",
                "__version_info__",
            ),
            ".api": ("FlextDbtLdap",),
            ".base": ("FlextDbtLdapServiceBase",),
            ".constants": ("FlextDbtLdapConstants",),
            ".errors": (
                "FlextDbtLdapAuthenticationError",
                "FlextDbtLdapConfigurationError",
                "FlextDbtLdapConnectionError",
                "FlextDbtLdapError",
                "FlextDbtLdapMacroError",
                "FlextDbtLdapModelError",
                "FlextDbtLdapProcessingError",
                "FlextDbtLdapTestError",
                "FlextDbtLdapTimeoutError",
                "FlextDbtLdapValidationError",
            ),
            ".models": ("FlextDbtLdapModels",),
            ".protocols": ("FlextDbtLdapProtocols",),
            ".settings": ("FlextDbtLdapSettings",),
            ".typings": ("FlextDbtLdapTypes",),
            ".utilities": ("FlextDbtLdapUtilities",),
            "flext_core.decorators": ("d",),
            "flext_core.exceptions": ("e",),
            "flext_core.handlers": ("h",),
            "flext_core.mixins": ("x",),
            "flext_core.result": ("r",),
        },
        alias_groups={
            ".base": (("s", "FlextDbtLdapServiceBase"),),
            ".constants": (("c", "FlextDbtLdapConstants"),),
            ".models": (("m", "FlextDbtLdapModels"),),
            ".protocols": (("p", "FlextDbtLdapProtocols"),),
            ".typings": (("t", "FlextDbtLdapTypes"),),
            ".utilities": (("u", "FlextDbtLdapUtilities"),),
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
    ),
    module_name=__name__,
)

__all__ = [
    "FlextDbtLdap",
    "FlextDbtLdapAuthenticationError",
    "FlextDbtLdapConfigurationError",
    "FlextDbtLdapConnectionError",
    "FlextDbtLdapConstants",
    "FlextDbtLdapConstantsAttributes",
    "FlextDbtLdapConstantsBase",
    "FlextDbtLdapConstantsSearch",
    "FlextDbtLdapConstantsTransformation",
    "FlextDbtLdapError",
    "FlextDbtLdapMacroError",
    "FlextDbtLdapModelError",
    "FlextDbtLdapModels",
    "FlextDbtLdapModelsConfiguration",
    "FlextDbtLdapModelsDimensions",
    "FlextDbtLdapModelsResults",
    "FlextDbtLdapModelsSchema",
    "FlextDbtLdapModelsShared",
    "FlextDbtLdapProcessingError",
    "FlextDbtLdapProtocols",
    "FlextDbtLdapServiceBase",
    "FlextDbtLdapSettings",
    "FlextDbtLdapTestError",
    "FlextDbtLdapTimeoutError",
    "FlextDbtLdapTypes",
    "FlextDbtLdapUtilities",
    "FlextDbtLdapUtilitiesClient",
    "FlextDbtLdapUtilitiesEntry",
    "FlextDbtLdapUtilitiesIntegration",
    "FlextDbtLdapUtilitiesMacros",
    "FlextDbtLdapUtilitiesSync",
    "FlextDbtLdapValidationError",
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


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
