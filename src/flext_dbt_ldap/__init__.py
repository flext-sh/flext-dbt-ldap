"""FLEXT DBT LDAP - LDAP Directory Data Transformations with simplified imports.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

Version 0.7.0 - DBT LDAP Transformations with simplified public API:
- All common imports available from root: from flext_dbt_ldap import LDAPTransformer
- Built on flext-core foundation for robust LDAP data transformations
- Deprecation warnings for internal imports
"""

from __future__ import annotations

import contextlib
import importlib.metadata
import warnings

# Import from flext-core for foundational patterns
# Re-export commonly used imports from flext-core
# Foundation patterns - ALWAYS from flext-core
# 🚨 ARCHITECTURAL COMPLIANCE: Using DI container
from flext_dbt_ldap.infrastructure.di_container import (
    get_base_config,
    get_domain_entity,
    get_domain_value_object,
    get_field,
    get_service_result,
)

ServiceResult = get_service_result()
DomainEntity = get_domain_entity()
Field = get_field()
DomainValueObject = get_domain_value_object()
BaseConfig = get_base_config()

# Re-export for simplified access
BaseModel = DomainEntity  # Base for LDAP models
LDAPBaseConfig = BaseConfig  # Configuration base
LDAPError = Exception  # LDAP-specific errors
ValidationError = Exception  # Validation errors

try:
    __version__ = importlib.metadata.version("flext-dbt-ldap")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.7.0"

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

# DBT LDAP Components exports - conditional imports (modules being developed)
with contextlib.suppress(ImportError):
    from flext_dbt_ldap.models import (
        GroupDimension,
        LDAPTransformer,
        UserDimension,
    )

# DBT Integration exports - conditional imports (modules being developed)
with contextlib.suppress(ImportError):
    from flext_dbt_ldap.macros import (
        DNParser,
        LDAPMacros,
        TimestampConverter,
    )

# ================================
# PUBLIC API EXPORTS
# ================================

__all__ = [
    "BaseModel",  # from flext_dbt_ldap import BaseModel
    # DBT Macros (simplified access)
    "DNParser",  # from flext_dbt_ldap import DNParser
    # Deprecation utilities
    "FlextDbtLdapDeprecationWarning",
    "GroupDimension",  # from flext_dbt_ldap import GroupDimension
    # Core Patterns (from flext-core)
    "LDAPBaseConfig",  # from flext_dbt_ldap import LDAPBaseConfig
    "LDAPError",  # from flext_dbt_ldap import LDAPError
    # DBT Models (simplified access)
    "LDAPMacros",  # from flext_dbt_ldap import LDAPMacros
    "LDAPTransformer",  # from flext_dbt_ldap import LDAPTransformer
    "ServiceResult",  # from flext_dbt_ldap import ServiceResult
    # Time Conversion (simplified access)
    "TimestampConverter",  # from flext_dbt_ldap import TimestampConverter
    "UserDimension",  # from flext_dbt_ldap import UserDimension
    "ValidationError",  # from flext_dbt_ldap import ValidationError
    # Version
    "__version__",
    "__version_info__",
]
