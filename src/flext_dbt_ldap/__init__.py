"""FLEXT DBT LDAP - Enterprise LDAP integration for DBT workflows.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Final

from flext_dbt_ldap.__version__ import __version__, __version_info__
from flext_dbt_ldap.config import FlextDbtLdapConfig
from flext_dbt_ldap.dbt_client import FlextDbtLdapClient
from flext_dbt_ldap.dbt_exceptions import (
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
from flext_dbt_ldap.deprecation_warnings import (
    FlextDbtLdapDeprecationWarning,
)
from flext_dbt_ldap.ldap_integration import (
    process_ldap_entries_for_dbt,
    validate_ldap_data_quality,
)
from flext_dbt_ldap.simple_api import FlextDbtLdap, FlextDbtLdapAPI
from flext_dbt_ldap.type_aliases import (
    DomainBaseModel,
    FlextDbtLdapResult,
)
from flext_dbt_ldap.typings import FlextDbtLdapTypes
from flext_dbt_ldap.utilities import FlextDbtLdapUtilities
from flext_dbt_ldap.version import VERSION, FlextDbtLdapVersion

PROJECT_VERSION: Final[FlextDbtLdapVersion] = VERSION


__all__ = [
    "PROJECT_VERSION",
    "VERSION",
    "DomainBaseModel",
    "FlextCore.Config",
    "FlextCore.Models",
    "FlextCore.Result",
    "FlextDbtLdap",
    "FlextDbtLdap",
    "FlextDbtLdapAPI",
    "FlextDbtLdapAuthenticationError",
    "FlextDbtLdapClient",
    "FlextDbtLdapConfig",
    "FlextDbtLdapConfigurationError",
    "FlextDbtLdapConnectionError",
    "FlextDbtLdapDeprecationWarning",
    "FlextDbtLdapError",
    "FlextDbtLdapMacroError",
    "FlextDbtLdapModelError",
    "FlextDbtLdapProcessingError",
    "FlextDbtLdapResult",
    "FlextDbtLdapTestError",
    "FlextDbtLdapTimeoutError",
    "FlextDbtLdapTypes",
    "FlextDbtLdapUtilities",
    "FlextDbtLdapValidationError",
    "FlextDbtLdapVersion",
    "__version__",
    "__version_info__",
    "_show_deprecation_warning",
    "process_ldap_entries_for_dbt",
    "validate_ldap_data_quality",
]
