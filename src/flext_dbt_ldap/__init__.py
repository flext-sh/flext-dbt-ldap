# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make codegen
#
"""FLEXT DBT LDAP - Enterprise LDAP integration for DBT workflows.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core import d, e, h, r, s, x
    from flext_core.typings import FlextTypes

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
    from flext_dbt_ldap.constants import FlextDbtLdapConstants, c
    from flext_dbt_ldap.dbt_client import FlextDbtLdapClient
    from flext_dbt_ldap.dbt_exceptions import (
        FlextDbtLdapAuthenticationError,
        FlextDbtLdapConnectionError,
        FlextDbtLdapError,
        FlextDbtLdapMacroError,
        FlextDbtLdapModelError,
        FlextDbtLdapProcessingError,
        FlextDbtLdapSettingsurationError,
        FlextDbtLdapTestError,
        FlextDbtLdapTimeoutError,
        FlextDbtLdapValidationError,
    )
    from flext_dbt_ldap.dbt_services import FlextDbtLdapService
    from flext_dbt_ldap.ldap_integration import (
        FlextDbtLdapIntegration,
        process_ldap_entries_for_dbt,
        validate_ldap_data_quality,
    )
    from flext_dbt_ldap.macros import FlextDbtLdapMacros
    from flext_dbt_ldap.models import FlextDbtLdapModels, m
    from flext_dbt_ldap.protocols import FlextDbtLdapProtocols, p
    from flext_dbt_ldap.settings import FlextDbtLdapSettings, logger
    from flext_dbt_ldap.simple_api import FlextDbtLdap
    from flext_dbt_ldap.typings import FlextDbtLdapTypes, t
    from flext_dbt_ldap.utilities import FlextDbtLdapUtilities, u

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "FlextDbtLdap": ("flext_dbt_ldap.simple_api", "FlextDbtLdap"),
    "FlextDbtLdapAuthenticationError": (
        "flext_dbt_ldap.dbt_exceptions",
        "FlextDbtLdapAuthenticationError",
    ),
    "FlextDbtLdapClient": ("flext_dbt_ldap.dbt_client", "FlextDbtLdapClient"),
    "FlextDbtLdapConnectionError": (
        "flext_dbt_ldap.dbt_exceptions",
        "FlextDbtLdapConnectionError",
    ),
    "FlextDbtLdapConstants": ("flext_dbt_ldap.constants", "FlextDbtLdapConstants"),
    "FlextDbtLdapError": ("flext_dbt_ldap.dbt_exceptions", "FlextDbtLdapError"),
    "FlextDbtLdapIntegration": (
        "flext_dbt_ldap.ldap_integration",
        "FlextDbtLdapIntegration",
    ),
    "FlextDbtLdapMacroError": (
        "flext_dbt_ldap.dbt_exceptions",
        "FlextDbtLdapMacroError",
    ),
    "FlextDbtLdapMacros": ("flext_dbt_ldap.macros", "FlextDbtLdapMacros"),
    "FlextDbtLdapModelError": (
        "flext_dbt_ldap.dbt_exceptions",
        "FlextDbtLdapModelError",
    ),
    "FlextDbtLdapModels": ("flext_dbt_ldap.models", "FlextDbtLdapModels"),
    "FlextDbtLdapProcessingError": (
        "flext_dbt_ldap.dbt_exceptions",
        "FlextDbtLdapProcessingError",
    ),
    "FlextDbtLdapProtocols": ("flext_dbt_ldap.protocols", "FlextDbtLdapProtocols"),
    "FlextDbtLdapService": ("flext_dbt_ldap.dbt_services", "FlextDbtLdapService"),
    "FlextDbtLdapSettings": ("flext_dbt_ldap.settings", "FlextDbtLdapSettings"),
    "FlextDbtLdapSettingsurationError": (
        "flext_dbt_ldap.dbt_exceptions",
        "FlextDbtLdapSettingsurationError",
    ),
    "FlextDbtLdapTestError": ("flext_dbt_ldap.dbt_exceptions", "FlextDbtLdapTestError"),
    "FlextDbtLdapTimeoutError": (
        "flext_dbt_ldap.dbt_exceptions",
        "FlextDbtLdapTimeoutError",
    ),
    "FlextDbtLdapTypes": ("flext_dbt_ldap.typings", "FlextDbtLdapTypes"),
    "FlextDbtLdapUtilities": ("flext_dbt_ldap.utilities", "FlextDbtLdapUtilities"),
    "FlextDbtLdapValidationError": (
        "flext_dbt_ldap.dbt_exceptions",
        "FlextDbtLdapValidationError",
    ),
    "__all__": ("flext_dbt_ldap.__version__", "__all__"),
    "__author__": ("flext_dbt_ldap.__version__", "__author__"),
    "__author_email__": ("flext_dbt_ldap.__version__", "__author_email__"),
    "__description__": ("flext_dbt_ldap.__version__", "__description__"),
    "__license__": ("flext_dbt_ldap.__version__", "__license__"),
    "__title__": ("flext_dbt_ldap.__version__", "__title__"),
    "__url__": ("flext_dbt_ldap.__version__", "__url__"),
    "__version__": ("flext_dbt_ldap.__version__", "__version__"),
    "__version_info__": ("flext_dbt_ldap.__version__", "__version_info__"),
    "c": ("flext_dbt_ldap.constants", "c"),
    "d": ("flext_core", "d"),
    "e": ("flext_core", "e"),
    "h": ("flext_core", "h"),
    "logger": ("flext_dbt_ldap.settings", "logger"),
    "m": ("flext_dbt_ldap.models", "m"),
    "p": ("flext_dbt_ldap.protocols", "p"),
    "process_ldap_entries_for_dbt": (
        "flext_dbt_ldap.ldap_integration",
        "process_ldap_entries_for_dbt",
    ),
    "r": ("flext_core", "r"),
    "s": ("flext_core", "s"),
    "t": ("flext_dbt_ldap.typings", "t"),
    "u": ("flext_dbt_ldap.utilities", "u"),
    "validate_ldap_data_quality": (
        "flext_dbt_ldap.ldap_integration",
        "validate_ldap_data_quality",
    ),
    "x": ("flext_core", "x"),
}

__all__ = [
    "FlextDbtLdap",
    "FlextDbtLdapAuthenticationError",
    "FlextDbtLdapClient",
    "FlextDbtLdapConnectionError",
    "FlextDbtLdapConstants",
    "FlextDbtLdapError",
    "FlextDbtLdapIntegration",
    "FlextDbtLdapMacroError",
    "FlextDbtLdapMacros",
    "FlextDbtLdapModelError",
    "FlextDbtLdapModels",
    "FlextDbtLdapProcessingError",
    "FlextDbtLdapProtocols",
    "FlextDbtLdapService",
    "FlextDbtLdapSettings",
    "FlextDbtLdapSettingsurationError",
    "FlextDbtLdapTestError",
    "FlextDbtLdapTimeoutError",
    "FlextDbtLdapTypes",
    "FlextDbtLdapUtilities",
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
    "c",
    "d",
    "e",
    "h",
    "logger",
    "m",
    "p",
    "process_ldap_entries_for_dbt",
    "r",
    "s",
    "t",
    "u",
    "validate_ldap_data_quality",
    "x",
]


def __getattr__(name: str) -> FlextTypes.ModuleExport:
    """Lazy-load module attributes on first access (PEP 562)."""
    return lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete."""
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
