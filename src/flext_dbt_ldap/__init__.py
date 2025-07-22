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
from flext_core import (
    BaseConfig,
    BaseConfig as LDAPBaseConfig,  # Configuration base
    DomainBaseModel,
    DomainBaseModel as BaseModel,  # Base for LDAP models
    DomainError as LDAPError,  # LDAP-specific errors
    ValidationError as ValidationError,  # Validation errors
)
from flext_core.domain.shared_types import ServiceResult

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
try:
    from flext_dbt_ldap.models import (
        GroupDimension,
        LDAPTransformer,
        UserDimension,
    )
except ImportError:
    # DBT models module not yet implemented - will be created as part of dbt project setup
    pass

# DBT Integration exports - conditional imports (modules being developed)
try:
    from flext_dbt_ldap.macros import (
        DNParser,
        LDAPMacros,
        TimestampConverter,
    )
except ImportError:
    # DBT macros module not yet implemented - will be created as part of dbt project setup
    pass

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
