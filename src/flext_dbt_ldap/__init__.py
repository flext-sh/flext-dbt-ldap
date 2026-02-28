"""FLEXT DBT LDAP - Enterprise LDAP integration for DBT workflows.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_core import FlextModels, FlextResult, FlextSettings

from flext_dbt_ldap.__version__ import __version__, __version_info__
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
from flext_dbt_ldap.deprecation_warnings import (
    FlextDbtLdapDeprecationWarning,
)
from flext_dbt_ldap.ldap_integration import (
    process_ldap_entries_for_dbt,
    validate_ldap_data_quality,
)
from flext_dbt_ldap.models import FlextDbtLdapModels, m
from flext_dbt_ldap.settings import FlextDbtLdapSettings
from flext_dbt_ldap.simple_api import FlextDbtLdap
from flext_dbt_ldap.typings import FlextDbtLdapTypes, t
from flext_dbt_ldap.utilities import FlextDbtLdapUtilities
from flext_dbt_ldap.version import VERSION, FlextDbtLdapVersion

__all__ = [
    "VERSION",
    "FlextDbtLdap",
    "FlextDbtLdapAuthenticationError",
    "FlextDbtLdapClient",
    "FlextDbtLdapConnectionError",
    "FlextDbtLdapConstants",
    "FlextDbtLdapDeprecationWarning",
    "FlextDbtLdapError",
    "FlextDbtLdapMacroError",
    "FlextDbtLdapModelError",
    "FlextDbtLdapModels",
    "FlextDbtLdapProcessingError",
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
    "process_ldap_entries_for_dbt",
    "t",
    "validate_ldap_data_quality",
]
