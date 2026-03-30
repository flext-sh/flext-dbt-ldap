# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""FLEXT DBT LDAP - Enterprise LDAP integration for DBT workflows.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

from flext_dbt_ldap.__version__ import (
    __author__ as __author__,
    __author_email__ as __author_email__,
    __description__ as __description__,
    __license__ as __license__,
    __title__ as __title__,
    __url__ as __url__,
    __version__,
    __version_info__,
)

if TYPE_CHECKING:
    from flext_dbt_ldap import (
        _utilities as _utilities,
        constants as constants,
        errors as errors,
        models as models,
        protocols as protocols,
        settings as settings,
        simple_api as simple_api,
        typings as typings,
        utilities as utilities,
        version_info as version_info,
    )
    from flext_dbt_ldap._utilities import (
        client as client,
        integration as integration,
        macros as macros,
        sync as sync,
    )
    from flext_dbt_ldap._utilities.client import (
        FlextDbtLdapUtilitiesClient as FlextDbtLdapUtilitiesClient,
    )
    from flext_dbt_ldap._utilities.integration import (
        FlextDbtLdapUtilitiesIntegration as FlextDbtLdapUtilitiesIntegration,
    )
    from flext_dbt_ldap._utilities.macros import (
        FlextDbtLdapUtilitiesMacros as FlextDbtLdapUtilitiesMacros,
    )
    from flext_dbt_ldap._utilities.sync import (
        FlextDbtLdapUtilitiesSync as FlextDbtLdapUtilitiesSync,
    )
    from flext_dbt_ldap.constants import (
        FlextDbtLdapConstants as FlextDbtLdapConstants,
        FlextDbtLdapConstants as c,
    )
    from flext_dbt_ldap.errors import (
        FlextDbtLdapAuthenticationError as FlextDbtLdapAuthenticationError,
        FlextDbtLdapConfigurationError as FlextDbtLdapConfigurationError,
        FlextDbtLdapConnectionError as FlextDbtLdapConnectionError,
        FlextDbtLdapError as FlextDbtLdapError,
        FlextDbtLdapMacroError as FlextDbtLdapMacroError,
        FlextDbtLdapModelError as FlextDbtLdapModelError,
        FlextDbtLdapProcessingError as FlextDbtLdapProcessingError,
        FlextDbtLdapTestError as FlextDbtLdapTestError,
        FlextDbtLdapTimeoutError as FlextDbtLdapTimeoutError,
        FlextDbtLdapValidationError as FlextDbtLdapValidationError,
    )
    from flext_dbt_ldap.models import (
        FlextDbtLdapModels as FlextDbtLdapModels,
        FlextDbtLdapModels as m,
    )
    from flext_dbt_ldap.protocols import (
        FlextDbtLdapProtocols as FlextDbtLdapProtocols,
        FlextDbtLdapProtocols as p,
    )
    from flext_dbt_ldap.settings import (
        FlextDbtLdapSettings as FlextDbtLdapSettings,
        logger as logger,
    )
    from flext_dbt_ldap.simple_api import FlextDbtLdap as FlextDbtLdap
    from flext_dbt_ldap.typings import (
        FlextDbtLdapTypes as FlextDbtLdapTypes,
        FlextDbtLdapTypes as t,
    )
    from flext_dbt_ldap.utilities import (
        FlextDbtLdapUtilities as FlextDbtLdapUtilities,
        FlextDbtLdapUtilities as u,
    )
    from flext_dbt_ldap.version_info import (
        __version__ as __version__,
        __version_info__ as __version_info__,
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
    "__version__": ["flext_dbt_ldap.version_info", "__version__"],
    "__version_info__": ["flext_dbt_ldap.version_info", "__version_info__"],
    "_utilities": ["flext_dbt_ldap._utilities", ""],
    "c": ["flext_dbt_ldap.constants", "FlextDbtLdapConstants"],
    "client": ["flext_dbt_ldap._utilities.client", ""],
    "constants": ["flext_dbt_ldap.constants", ""],
    "d": ["flext_ldap", "d"],
    "e": ["flext_ldap", "e"],
    "errors": ["flext_dbt_ldap.errors", ""],
    "h": ["flext_ldap", "h"],
    "integration": ["flext_dbt_ldap._utilities.integration", ""],
    "logger": ["flext_dbt_ldap.settings", "logger"],
    "m": ["flext_dbt_ldap.models", "FlextDbtLdapModels"],
    "macros": ["flext_dbt_ldap._utilities.macros", ""],
    "models": ["flext_dbt_ldap.models", ""],
    "p": ["flext_dbt_ldap.protocols", "FlextDbtLdapProtocols"],
    "protocols": ["flext_dbt_ldap.protocols", ""],
    "r": ["flext_ldap", "r"],
    "s": ["flext_ldap", "s"],
    "settings": ["flext_dbt_ldap.settings", ""],
    "simple_api": ["flext_dbt_ldap.simple_api", ""],
    "sync": ["flext_dbt_ldap._utilities.sync", ""],
    "t": ["flext_dbt_ldap.typings", "FlextDbtLdapTypes"],
    "typings": ["flext_dbt_ldap.typings", ""],
    "u": ["flext_dbt_ldap.utilities", "FlextDbtLdapUtilities"],
    "utilities": ["flext_dbt_ldap.utilities", ""],
    "version_info": ["flext_dbt_ldap.version_info", ""],
    "x": ["flext_ldap", "x"],
}

_EXPORTS: Sequence[str] = [
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
    "client",
    "constants",
    "d",
    "e",
    "errors",
    "h",
    "integration",
    "logger",
    "m",
    "macros",
    "models",
    "p",
    "protocols",
    "r",
    "s",
    "settings",
    "simple_api",
    "sync",
    "t",
    "typings",
    "u",
    "utilities",
    "version_info",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, _EXPORTS)
