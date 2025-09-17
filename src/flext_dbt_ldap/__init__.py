"""FLEXT DBT LDAP - Enterprise LDAP integration for DBT workflows.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_core import (
    FlextConfig,
    FlextModels,
    FlextResult,
)
from flext_dbt_ldap.dbt_client import FlextDbtLdapClient
from flext_dbt_ldap.dbt_config import FlextDbtLdapConfig
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
    _show_deprecation_warning,
)
from flext_dbt_ldap.ldap_integration import (
    process_ldap_entries_for_dbt,
    validate_ldap_data_quality,
)
from flext_dbt_ldap.type_aliases import (
    DomainBaseModel,
    FlextDbtLdap,
    FlextDbtLdapResult,
)
from flext_dbt_ldap.version_info import __version__, __version_info__

__all__ = [
    "DomainBaseModel",
    "FlextConfig",
    "FlextDbtLdap",
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
    "FlextDbtLdapValidationError",
    "FlextModels",
    "FlextResult",
    "__version__",
    "__version_info__",
    "_show_deprecation_warning",
    "process_ldap_entries_for_dbt",
    "validate_ldap_data_quality",
]
