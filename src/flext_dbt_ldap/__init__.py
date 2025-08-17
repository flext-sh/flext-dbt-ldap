"""Enterprise DBT Models for LDAP Directory Transformations and Analytics."""

from __future__ import annotations

import contextlib
import importlib.metadata
import warnings

from flext_core import (
    FlextSettings as BaseConfig,
    FlextEntity as DomainEntity,
    FlextFields as Field,
    FlextResult,
    FlextValueObject as BaseModel,
    FlextValueObject as DomainBaseModel,
    FlextValueObject as DomainValueObject,
    get_logger,
)

from flext_meltano import (
    FlextDbtHub,
    FlextDbtInMemoryExecutor,
    FlextDbtModelRegistry,
    FlextDbtPackageManager,
    create_dbt_hub,
)

from flext_dbt_ldap.ldap_integration import (
    process_ldap_entries_for_dbt,
    validate_ldap_data_quality,
)

# FlextDbtLdap-specific aliases (following FlextXxx pattern)
FlextDbtLdap: type | None = None  # Will be set to platform when available
FlextDbtLdapResult = FlextResult  # FlextDbtLdap result pattern
FlextDbtLdapBaseModel = DomainBaseModel  # FlextDbtLdap base model
FlextValueObject = DomainValueObject  # Standard value object pattern

flext_dbt_ldap_transform_entry: object | None = None
flext_dbt_ldap_create_dimension: object | None = None
flext_dbt_ldap_parse_dn: object | None = None
flext_dbt_ldap_convert_timestamp: object | None = None

# Backwards compatibility aliases
LDAPBaseConfig = BaseConfig  # Configuration base
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
from flext_dbt_ldap.dbt_config import FlextDbtLdapConfig
from flext_dbt_ldap.dbt_client import FlextDbtLdapClient
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
from flext_dbt_ldap.dbt_exceptions import (
    FlextDbtLdapError,
    FlextDbtLdapValidationError,
    FlextDbtLdapConfigurationError,
    FlextDbtLdapConnectionError,
    FlextDbtLdapProcessingError,
    FlextDbtLdapAuthenticationError,
    FlextDbtLdapTimeoutError,
    FlextDbtLdapModelError,
    FlextDbtLdapMacroError,
    FlextDbtLdapTestError,
)
from flext_dbt_ldap.dbt_services import FlextDbtLdapService

# DBT Integration exports
from flext_dbt_ldap.macros import (
    FlextDbtLdapDNParser,
    FlextDbtLdapMacros,
    FlextDbtLdapTimestampConverter,
    # Backward compatibility aliases
    DNParser,
    LDAPMacros,
    TimestampConverter,
)

# Simple API exports
from flext_dbt_ldap.simple_api import (
    create_flext_dbt_ldap_config,
    create_flext_dbt_ldap_client,
    create_flext_dbt_ldap_service,
    create_flext_group_dimension,
    create_flext_ldap_transformer,
    create_flext_user_dimension,
    create_simple_dbt_ldap_pipeline,
)

# ================================
# PUBLIC API EXPORTS
# ================================

__all__: list[str] = [
    # Core patterns from flext-core
    "BaseConfig",
    "BaseModel",
    "DomainBaseModel",
    "DomainEntity",
    "DomainValueObject",
    "Field",
    "FlextResult",
    "FlextValueObject",
    "get_logger",
    # === FLEXT-MELTANO DBT RE-EXPORTS ===
    "FlextDbtHub",
    "FlextDbtInMemoryExecutor",
    "FlextDbtModelRegistry",
    "FlextDbtPackageManager",
    "create_dbt_hub",
    # === NEW DBT LDAP COMPONENTS (PEP8 NAMES) ===
    # Configuration
    "FlextDbtLdapConfig",
    # Client and Services
    "FlextDbtLdapClient",
    "FlextDbtLdapService",
    # Data Models
    "FlextDbtLdapGroupDimension",
    "FlextDbtLdapMembershipFact",
    "FlextDbtLdapTransformer",
    "FlextDbtLdapUserDimension",
    # Macros and Utilities
    "FlextDbtLdapDNParser",
    "FlextDbtLdapMacros",
    "FlextDbtLdapTimestampConverter",
    # Exceptions
    "FlextDbtLdapError",
    "FlextDbtLdapValidationError",
    "FlextDbtLdapConfigurationError",
    "FlextDbtLdapConnectionError",
    "FlextDbtLdapProcessingError",
    "FlextDbtLdapAuthenticationError",
    "FlextDbtLdapTimeoutError",
    "FlextDbtLdapModelError",
    "FlextDbtLdapMacroError",
    "FlextDbtLdapTestError",
    # Simple API Factory Functions
    "create_flext_dbt_ldap_config",
    "create_flext_dbt_ldap_client",
    "create_flext_dbt_ldap_service",
    "create_flext_group_dimension",
    "create_flext_ldap_transformer",
    "create_flext_user_dimension",
    "create_simple_dbt_ldap_pipeline",
    # === BACKWARD COMPATIBILITY ALIASES ===
    # DBT Models (legacy names)
    "GroupDimension",
    "LDAPTransformer",
    "UserDimension",
    # DBT Macros (legacy names)
    "DNParser",
    "LDAPMacros",
    "TimestampConverter",
    # Legacy configuration and errors
    "LDAPBaseConfig",
    "LDAPError",
    "ValidationError",
    # Deprecation utilities
    "FlextDbtLdapDeprecationWarning",
    # FlextDbtLdap-specific aliases
    "FlextDbtLdap",  # Main FlextDbtLdap class alias
    "FlextDbtLdapBaseModel",  # FlextDbtLdap base model alias
    "FlextDbtLdapResult",  # FlextDbtLdap result pattern alias
    # Integration helper functions
    "process_ldap_entries_for_dbt",
    "validate_ldap_data_quality",
    # Metadata
    "__version__",
    "__version_info__",
    # Prefixed helper function placeholders
    "flext_dbt_ldap_convert_timestamp",
    "flext_dbt_ldap_create_dimension",
    "flext_dbt_ldap_parse_dn",
    "flext_dbt_ldap_transform_entry",
]
