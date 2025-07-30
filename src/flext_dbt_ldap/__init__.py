"""FLEXT DBT LDAP - LDAP Directory Data Transformations with simplified imports.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

Version 0.9.0 - DBT LDAP Transformations with simplified public API:
- All common imports available from root: from flext_dbt_ldap import LDAPTransformer
- Built on flext-core foundation for robust LDAP data transformations
- Deprecation warnings for internal imports
"""

from __future__ import annotations

import contextlib
import importlib.metadata
import warnings

# Import from flext-core for foundational patterns (standardized)
from flext_core import (
    FlextBaseSettings as BaseConfig,
    FlextEntity as DomainEntity,
    FlextFields as Field,
    FlextResult,
    FlextValueObject as BaseModel,
    FlextValueObject as DomainBaseModel,
    FlextValueObject as DomainValueObject,
)

# Import from flext-ldap for centralized LDAP patterns - ACTUAL USAGE
from flext_ldap import (
    FlextLdapAuth,
    FlextLdapClient,
    FlextLdapConfig,
    FlextLdapParser,
    FlextLdapResult,
    format_ldap_timestamp,
    parse_dn,
    validate_dn,
)

# Import from flext-meltano for DBT integration
# MIGRATED: Singer SDK imports centralized via flext-meltano
from flext_meltano.dbt import (
    FlextMeltanoDbtManager,
    FlextMeltanoDbtProject,
    FlextMeltanoDbtRunner,
)

# Import local integration functions that use flext-ldap
with contextlib.suppress(ImportError):
    from flext_dbt_ldap.ldap_integration import (
        process_ldap_entries_for_dbt,
        validate_ldap_data_quality,
    )

# FlextDbtLdap-specific aliases (following FlextXxx pattern)
FlextDbtLdap: type | None = None  # Will be set to platform when available
FlextDbtLdapResult = FlextResult  # FlextDbtLdap result pattern
FlextDbtLdapBaseModel = DomainBaseModel  # FlextDbtLdap base model
FlextValueObject = DomainValueObject  # Standard value object pattern

# Prefixed helper functions following flext_dbt_ldap_ pattern
with contextlib.suppress(NameError):
    flext_dbt_ldap_transform_entry: object | None = None
    flext_dbt_ldap_create_dimension: object | None = None
    flext_dbt_ldap_parse_dn: object | None = None
    flext_dbt_ldap_convert_timestamp: object | None = None

# Backwards compatibility aliases
LDAPBaseConfig = BaseConfig  # Configuration base
LDAPError = Exception  # LDAP-specific errors
ValidationError = Exception  # Validation errors

try:
    __version__ = importlib.metadata.version("flext-dbt-ldap")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.9.0"

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

# DBT LDAP Components exports - simplified imports
with contextlib.suppress(ImportError):
    from flext_dbt_ldap.models import (
        GroupDimension,
        LDAPTransformer,
        UserDimension,
    )

# DBT Integration exports - simplified imports
with contextlib.suppress(ImportError):
    from flext_dbt_ldap.macros import (
        DNParser,
        LDAPMacros,
        TimestampConverter,
    )

# Simple API for common operations - simplified imports
with contextlib.suppress(ImportError):
    from flext_dbt_ldap.simple_api import (
        create_flext_group_dimension,
        create_flext_ldap_transformer,
        create_flext_user_dimension,
    )

# ================================
# PUBLIC API EXPORTS
# ================================

__all__ = [
    # Core patterns from flext-core
    "BaseConfig",
    "BaseModel",
    # DBT Macros (modern FlextXxx)
    "DNParser",
    "DomainBaseModel",
    "DomainEntity",
    "DomainValueObject",
    "Field",
    # FlextDbtLdap-specific classes (main patterns)
    "FlextDbtLdap",  # Main FlextDbtLdap class
    "FlextDbtLdapBaseModel",  # FlextDbtLdap base model
    # Deprecation utilities
    "FlextDbtLdapDeprecationWarning",
    "FlextDbtLdapResult",  # FlextDbtLdap result pattern
    "FlextResult",
    "FlextValueObject",
    # DBT Models (modern FlextXxx)
    "GroupDimension",
    # Legacy compatibility
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
    # Simple API (modern FlextXxx)
    "create_flext_group_dimension",
    "create_flext_ldap_transformer",
    "create_flext_user_dimension",
    # Prefixed helper functions
    "flext_dbt_ldap_convert_timestamp",
    "flext_dbt_ldap_create_dimension",
    "flext_dbt_ldap_parse_dn",
    "flext_dbt_ldap_transform_entry",
]
