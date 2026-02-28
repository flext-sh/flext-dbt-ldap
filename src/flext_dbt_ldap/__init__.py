"""FLEXT DBT LDAP - Enterprise LDAP integration for DBT workflows.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from flext_core import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core import FlextModels, FlextResult, FlextSettings

    from flext_dbt_ldap.__version__ import __version__, __version_info__
    from flext_dbt_ldap.constants import (
        FlextDbtLdapConstants,
        FlextDbtLdapConstants as c,
    )
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
    from flext_dbt_ldap.ldap_integration import (
        process_ldap_entries_for_dbt,
        validate_ldap_data_quality,
    )
    from flext_dbt_ldap.models import FlextDbtLdapModels, FlextDbtLdapModels as m
    from flext_dbt_ldap.protocols import (
        FlextDbtLdapProtocols,
        FlextDbtLdapProtocols as p,
    )
    from flext_dbt_ldap.settings import FlextDbtLdapSettings
    from flext_dbt_ldap.simple_api import FlextDbtLdap
    from flext_dbt_ldap.typings import FlextDbtLdapTypes, FlextDbtLdapTypes as t
    from flext_dbt_ldap.utilities import (
        FlextDbtLdapUtilities,
        FlextDbtLdapUtilities as u,
    )
    from flext_dbt_ldap.version import VERSION, FlextDbtLdapVersion

# Lazy import mapping: export_name -> (module_path, attr_name)
_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "FlextDbtLdap": ("flext_dbt_ldap.simple_api", "FlextDbtLdap"),
    "FlextDbtLdapAuthenticationError": ("flext_dbt_ldap.dbt_exceptions", "FlextDbtLdapAuthenticationError"),
    "FlextDbtLdapClient": ("flext_dbt_ldap.dbt_client", "FlextDbtLdapClient"),
    "FlextDbtLdapConnectionError": ("flext_dbt_ldap.dbt_exceptions", "FlextDbtLdapConnectionError"),
    "FlextDbtLdapConstants": ("flext_dbt_ldap.constants", "FlextDbtLdapConstants"),
    "FlextDbtLdapError": ("flext_dbt_ldap.dbt_exceptions", "FlextDbtLdapError"),
    "FlextDbtLdapMacroError": ("flext_dbt_ldap.dbt_exceptions", "FlextDbtLdapMacroError"),
    "FlextDbtLdapModelError": ("flext_dbt_ldap.dbt_exceptions", "FlextDbtLdapModelError"),
    "FlextDbtLdapModels": ("flext_dbt_ldap.models", "FlextDbtLdapModels"),
    "FlextDbtLdapProcessingError": ("flext_dbt_ldap.dbt_exceptions", "FlextDbtLdapProcessingError"),
    "FlextDbtLdapProtocols": ("flext_dbt_ldap.protocols", "FlextDbtLdapProtocols"),
    "FlextDbtLdapSettings": ("flext_dbt_ldap.settings", "FlextDbtLdapSettings"),
    "FlextDbtLdapSettingsurationError": ("flext_dbt_ldap.dbt_exceptions", "FlextDbtLdapSettingsurationError"),
    "FlextDbtLdapTestError": ("flext_dbt_ldap.dbt_exceptions", "FlextDbtLdapTestError"),
    "FlextDbtLdapTimeoutError": ("flext_dbt_ldap.dbt_exceptions", "FlextDbtLdapTimeoutError"),
    "FlextDbtLdapTypes": ("flext_dbt_ldap.typings", "FlextDbtLdapTypes"),
    "FlextDbtLdapUtilities": ("flext_dbt_ldap.utilities", "FlextDbtLdapUtilities"),
    "FlextDbtLdapValidationError": ("flext_dbt_ldap.dbt_exceptions", "FlextDbtLdapValidationError"),
    "FlextDbtLdapVersion": ("flext_dbt_ldap.version", "FlextDbtLdapVersion"),
    "FlextModels": ("flext_core", "FlextModels"),
    "FlextResult": ("flext_core", "FlextResult"),
    "FlextSettings": ("flext_core", "FlextSettings"),
    "VERSION": ("flext_dbt_ldap.version", "VERSION"),
    "__version__": ("flext_dbt_ldap.__version__", "__version__"),
    "__version_info__": ("flext_dbt_ldap.__version__", "__version_info__"),
    "c": ("flext_dbt_ldap.constants", "FlextDbtLdapConstants"),
    "m": ("flext_dbt_ldap.models", "FlextDbtLdapModels"),
    "p": ("flext_dbt_ldap.protocols", "FlextDbtLdapProtocols"),
    "process_ldap_entries_for_dbt": ("flext_dbt_ldap.ldap_integration", "process_ldap_entries_for_dbt"),
    "t": ("flext_dbt_ldap.typings", "FlextDbtLdapTypes"),
    "u": ("flext_dbt_ldap.utilities", "FlextDbtLdapUtilities"),
    "validate_ldap_data_quality": ("flext_dbt_ldap.ldap_integration", "validate_ldap_data_quality"),
}

__all__ = [
    "VERSION",
    "FlextDbtLdap",
    "FlextDbtLdapAuthenticationError",
    "FlextDbtLdapClient",
    "FlextDbtLdapConnectionError",
    "FlextDbtLdapConstants",
    "FlextDbtLdapError",
    "FlextDbtLdapMacroError",
    "FlextDbtLdapModelError",
    "FlextDbtLdapModels",
    "FlextDbtLdapProcessingError",
    "FlextDbtLdapProtocols",
    "FlextDbtLdapSettings",
    "FlextDbtLdapSettingsurationError",
    "FlextDbtLdapTestError",
    "FlextDbtLdapTimeoutError",
    "FlextDbtLdapTypes",
    "FlextDbtLdapUtilities",
    "FlextDbtLdapValidationError",
    "FlextDbtLdapVersion",
    "FlextModels",
    "FlextResult",
    "FlextSettings",
    "__version__",
    "__version_info__",
    "c",
    "m",
    "p",
    "process_ldap_entries_for_dbt",
    "t",
    "u",
    "validate_ldap_data_quality",
]


def __getattr__(name: str) -> Any:  # noqa: ANN401
    """Lazy-load module attributes on first access (PEP 562)."""
    return lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete."""
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
