# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""FLEXT DBT LDAP - Enterprise LDAP integration for DBT workflows.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping, MutableMapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_ldap import d, e, h, r, s, x

    from flext_dbt_ldap import _utilities
    from flext_dbt_ldap.__version__ import (
        __all__,
        __author__,
        __author_email__,
        __description__,
        __license__,
        __title__,
        __url__,
        __version__,
        __version_info__,
    )
    from flext_dbt_ldap._utilities.client import FlextDbtLdapUtilitiesClient
    from flext_dbt_ldap._utilities.integration import FlextDbtLdapUtilitiesIntegration
    from flext_dbt_ldap._utilities.macros import FlextDbtLdapUtilitiesMacros
    from flext_dbt_ldap._utilities.sync import FlextDbtLdapUtilitiesSync
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
    from flext_dbt_ldap.settings import FlextDbtLdapSettings, logger
    from flext_dbt_ldap.simple_api import FlextDbtLdap
    from flext_dbt_ldap.typings import FlextDbtLdapTypes, FlextDbtLdapTypes as t
    from flext_dbt_ldap.utilities import (
        FlextDbtLdapUtilities,
        FlextDbtLdapUtilities as u,
    )

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "FlextDbtLdap": ["flext_dbt_ldap.simple_api", "FlextDbtLdap"],
    "FlextDbtLdapAuthenticationError": [
        "flext_dbt_ldap.errors",
        "FlextDbtLdapAuthenticationError",
    ],
    "FlextDbtLdapConfigurationError": [
        "flext_dbt_ldap.errors",
        "FlextDbtLdapConfigurationError",
    ],
    "FlextDbtLdapConnectionError": [
        "flext_dbt_ldap.errors",
        "FlextDbtLdapConnectionError",
    ],
    "FlextDbtLdapConstants": ["flext_dbt_ldap.constants", "FlextDbtLdapConstants"],
    "FlextDbtLdapError": ["flext_dbt_ldap.errors", "FlextDbtLdapError"],
    "FlextDbtLdapMacroError": ["flext_dbt_ldap.errors", "FlextDbtLdapMacroError"],
    "FlextDbtLdapModelError": ["flext_dbt_ldap.errors", "FlextDbtLdapModelError"],
    "FlextDbtLdapModels": ["flext_dbt_ldap.models", "FlextDbtLdapModels"],
    "FlextDbtLdapProcessingError": [
        "flext_dbt_ldap.errors",
        "FlextDbtLdapProcessingError",
    ],
    "FlextDbtLdapProtocols": ["flext_dbt_ldap.protocols", "FlextDbtLdapProtocols"],
    "FlextDbtLdapSettings": ["flext_dbt_ldap.settings", "FlextDbtLdapSettings"],
    "FlextDbtLdapTestError": ["flext_dbt_ldap.errors", "FlextDbtLdapTestError"],
    "FlextDbtLdapTimeoutError": ["flext_dbt_ldap.errors", "FlextDbtLdapTimeoutError"],
    "FlextDbtLdapTypes": ["flext_dbt_ldap.typings", "FlextDbtLdapTypes"],
    "FlextDbtLdapUtilities": ["flext_dbt_ldap.utilities", "FlextDbtLdapUtilities"],
    "FlextDbtLdapUtilitiesClient": [
        "flext_dbt_ldap._utilities.client",
        "FlextDbtLdapUtilitiesClient",
    ],
    "FlextDbtLdapUtilitiesIntegration": [
        "flext_dbt_ldap._utilities.integration",
        "FlextDbtLdapUtilitiesIntegration",
    ],
    "FlextDbtLdapUtilitiesMacros": [
        "flext_dbt_ldap._utilities.macros",
        "FlextDbtLdapUtilitiesMacros",
    ],
    "FlextDbtLdapUtilitiesSync": [
        "flext_dbt_ldap._utilities.sync",
        "FlextDbtLdapUtilitiesSync",
    ],
    "FlextDbtLdapValidationError": [
        "flext_dbt_ldap.errors",
        "FlextDbtLdapValidationError",
    ],
    "__all__": ["flext_dbt_ldap.__version__", "__all__"],
    "__author__": ["flext_dbt_ldap.__version__", "__author__"],
    "__author_email__": ["flext_dbt_ldap.__version__", "__author_email__"],
    "__description__": ["flext_dbt_ldap.__version__", "__description__"],
    "__license__": ["flext_dbt_ldap.__version__", "__license__"],
    "__title__": ["flext_dbt_ldap.__version__", "__title__"],
    "__url__": ["flext_dbt_ldap.__version__", "__url__"],
    "__version__": ["flext_dbt_ldap.__version__", "__version__"],
    "__version_info__": ["flext_dbt_ldap.__version__", "__version_info__"],
    "_utilities": ["flext_dbt_ldap._utilities", ""],
    "c": ["flext_dbt_ldap.constants", "FlextDbtLdapConstants"],
    "d": ["flext_ldap", "d"],
    "e": ["flext_ldap", "e"],
    "h": ["flext_ldap", "h"],
    "logger": ["flext_dbt_ldap.settings", "logger"],
    "m": ["flext_dbt_ldap.models", "FlextDbtLdapModels"],
    "p": ["flext_dbt_ldap.protocols", "FlextDbtLdapProtocols"],
    "r": ["flext_ldap", "r"],
    "s": ["flext_ldap", "s"],
    "t": ["flext_dbt_ldap.typings", "FlextDbtLdapTypes"],
    "u": ["flext_dbt_ldap.utilities", "FlextDbtLdapUtilities"],
    "x": ["flext_ldap", "x"],
}

__all__ = [
    "FlextDbtLdap",
    "FlextDbtLdapAuthenticationError",
    "FlextDbtLdapConfigurationError",
    "FlextDbtLdapConnectionError",
    "FlextDbtLdapConstants",
    "FlextDbtLdapError",
    "FlextDbtLdapMacroError",
    "FlextDbtLdapModelError",
    "FlextDbtLdapModels",
    "FlextDbtLdapProcessingError",
    "FlextDbtLdapProtocols",
    "FlextDbtLdapSettings",
    "FlextDbtLdapTestError",
    "FlextDbtLdapTimeoutError",
    "FlextDbtLdapTypes",
    "FlextDbtLdapUtilities",
    "FlextDbtLdapUtilitiesClient",
    "FlextDbtLdapUtilitiesIntegration",
    "FlextDbtLdapUtilitiesMacros",
    "FlextDbtLdapUtilitiesSync",
    "FlextDbtLdapValidationError",
    "__all__",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "_utilities",
    "c",
    "d",
    "e",
    "h",
    "logger",
    "m",
    "p",
    "r",
    "s",
    "t",
    "u",
    "x",
]


_LAZY_CACHE: MutableMapping[str, FlextTypes.ModuleExport] = {}


def __getattr__(name: str) -> FlextTypes.ModuleExport:
    """Lazy-load module attributes on first access (PEP 562).

    A local cache ``_LAZY_CACHE`` persists resolved objects across repeated
    accesses during process lifetime.

    Args:
        name: Attribute name requested by dir()/import.

    Returns:
        Lazy-loaded module export type.

    Raises:
        AttributeError: If attribute not registered.

    """
    if name in _LAZY_CACHE:
        return _LAZY_CACHE[name]

    value = lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)
    _LAZY_CACHE[name] = value
    return value


def __dir__() -> Sequence[str]:
    """Return list of available attributes for dir() and autocomplete.

    Returns:
        List of public names from module exports.

    """
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
