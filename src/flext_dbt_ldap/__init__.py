"""Enterprise DBT Models for LDAP Directory Transformations and Analytics.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import importlib.metadata
import warnings

from flext_core import (
    FlextConfig,
    FlextFields,
    FlextLogger,
    FlextModels,
    FlextResult,
    FlextTypes,
)

from flext_dbt_ldap.ldap_integration import (
    process_ldap_entries_for_dbt,
    validate_ldap_data_quality,
)

# FlextDbtLdap-specific aliases (following FlextXxx pattern)
FlextDbtLdap: type | None = None  # Will be set to platform when available
FlextDbtLdapResult = FlextResult  # FlextDbtLdap result pattern
# Legacy compatibility - use FlextModels.Config directly instead
DomainBaseModel = FlextModels.Config  # Domain base model
DomainEntity = FlextModels.Entity  # Domain entity
DomainValueObject = FlextModels.Value  # Domain value object

# Define exports that are listed in __all__
Config = FlextModels.Config  # Base configuration model
Field = FlextFields  # Field definitions

flext_dbt_ldap_transform_entry: object | None = None
flext_dbt_ldap_create_dimension: object | None = None
flext_dbt_ldap_parse_dn: object | None = None
flext_dbt_ldap_convert_timestamp: object | None = None

# Backwards compatibility aliases
LDAPBaseConfig = FlextConfig  # Configuration base
LDAPError = Exception  # LDAP-specific errors
ValidationError = Exception  # Validation errors

__version__ = importlib.metadata.version("flext-dbt-ldap")

__version_info__ = tuple(int(x) for x in __version__.split(".") if x.isdigit())


class FlextDbtLdapDeprecationWarning(DeprecationWarning):
    """Custom deprecation warning for FLEXT DBT LDAP import changes."""


def _show_deprecation_warning(old_import: str, new_import: str) -> None:
    """Show deprecation warning for import paths."""
    message_parts = [
        f"⚠️  DEPRECATED IMPORT: {old_import}",
        f"✅ USE INSTEAD: {new_import}",
        "🔗 This will be removed in version 1.0.0",
        "📖 See FLEXT DBT LDAP docs for migration guide",
    ]
    warnings.warn(
        "\n".join(message_parts),
        FlextDbtLdapDeprecationWarning,
        stacklevel=3,
    )


# ================================
# SIMPLIFIED PUBLIC API EXPORTS
# ================================

# Import from new PEP8 modules
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
from flext_dbt_ldap.dbt_services import FlextDbtLdapService

# DBT Integration exports
from flext_dbt_ldap.macros import (
    # Backward compatibility aliases
    DNParser,
    FlextDbtLdapDNParser,
    FlextDbtLdapMacros,
    FlextDbtLdapTimestampConverter,
    LDAPMacros,
    TimestampConverter,
)
from flext_dbt_ldap.models import (
    FlextDbtLdapGroupDimension,
    FlextDbtLdapMembershipFact,
    FlextDbtLdapTransformer,
    FlextDbtLdapUserDimension,
    # Backward compatibility aliases
    GroupDimension,
    LDAPTransformer,
    UserDimension,
)

# Simple API exports
from flext_dbt_ldap.simple_api import (
    create_flext_dbt_ldap_client,
    create_flext_dbt_ldap_config,
    create_flext_dbt_ldap_service,
    create_flext_group_dimension,
    create_flext_ldap_transformer,
    create_flext_user_dimension,
    create_simple_dbt_ldap_pipeline,
)

# ================================
# PUBLIC API EXPORTS
# ================================

__all__: FlextTypes.Core.StringList = [
    # Core patterns from flext-core
    "Config",
    # DBT Macros (legacy names)
    "DNParser",
    "DomainBaseModel",
    "DomainEntity",
    "DomainValueObject",
    "Field",
    # FlextDbtLdap-specific aliases
    "FlextDbtLdap",  # Main FlextDbtLdap class alias
    "FlextDbtLdapAuthenticationError",
    "FlextDbtLdapBaseModel",  # FlextDbtLdap base model alias
    # Client and Services
    "FlextDbtLdapClient",
    # === FLEXT-MELTANO DBT RE-EXPORTS ===
    # "FlextMeltanoDbtService",  # Service doesn't exist yet
    # === NEW DBT LDAP COMPONENTS (PEP8 NAMES) ===
    # Configuration
    "FlextDbtLdapConfig",
    "FlextDbtLdapConfigurationError",
    "FlextDbtLdapConnectionError",
    # Macros and Utilities
    "FlextDbtLdapDNParser",
    # Deprecation utilities
    "FlextDbtLdapDeprecationWarning",
    # Exceptions
    "FlextDbtLdapError",
    # Data Models
    "FlextDbtLdapGroupDimension",
    "FlextDbtLdapMacroError",
    "FlextDbtLdapMacros",
    "FlextDbtLdapMembershipFact",
    "FlextDbtLdapModelError",
    "FlextDbtLdapProcessingError",
    "FlextDbtLdapResult",  # FlextDbtLdap result pattern alias
    "FlextDbtLdapService",
    "FlextDbtLdapTestError",
    "FlextDbtLdapTimeoutError",
    "FlextDbtLdapTimestampConverter",
    "FlextDbtLdapTransformer",
    "FlextDbtLdapUserDimension",
    "FlextDbtLdapValidationError",
    "FlextLogger",
    "FlextModels",
    "FlextResult",
    # === BACKWARD COMPATIBILITY ALIASES ===
    # DBT Models (legacy names)
    "GroupDimension",
    # Legacy configuration and errors
    "LDAPBaseConfig",
    "LDAPError",
    "LDAPMacros",
    "LDAPTransformer",
    "TimestampConverter",
    "UserDimension",
    "ValidationError",
    # Metadata
    "__version__",
    "__version_info__",
    "create_flext_dbt_ldap_client",
    "create_flext_dbt_ldap_config",
    "create_flext_dbt_ldap_service",
    "create_flext_group_dimension",
    "create_flext_ldap_transformer",
    "create_flext_user_dimension",
    "create_simple_dbt_ldap_pipeline",
    # Prefixed helper function placeholders
    "flext_dbt_ldap_convert_timestamp",
    "flext_dbt_ldap_create_dimension",
    "flext_dbt_ldap_parse_dn",
    "flext_dbt_ldap_transform_entry",
    # Integration helper functions
    "process_ldap_entries_for_dbt",
    "validate_ldap_data_quality",
]
