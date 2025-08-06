"""FLEXT DBT LDAP - Enterprise DBT Models for LDAP Directory Transformations.

**Architecture**: Production-ready DBT project with enterprise patterns
**Integration**: Complete flext-meltano ecosystem integration
**Quality**: Enterprise-grade data models with comprehensive testing

## Enterprise Integration Features:

1. **Complete flext-meltano Integration**: Uses ALL DBT facilities
   - DBT Hub integration for model registry
   - In-memory execution with DuckDB
   - Enterprise patterns from flext-core

2. **Foundation Library Integration**: Full flext-core pattern adoption
   - FlextResult railway-oriented programming throughout
   - Enterprise logging with FlextLogger
   - Dependency injection with flext-core container
   - FlextConfig for configuration management

3. **LDAP Infrastructure Integration**: Complete flext-ldap utilization
   - Uses real LDAP operations from flext-ldap
   - Leverages DN parsing and validation
   - Enterprise-grade directory transformations

4. **Production Readiness**: Zero-tolerance quality standards
   - Comprehensive DBT tests
   - Data quality validation
   - Performance optimization

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import contextlib
import importlib.metadata
import warnings

# === FLEXT-MELTANO COMPLETE INTEGRATION ===
# Import DBT facilities from flext-meltano
from flext_meltano import (
    # DBT Hub integration
    FlextDbtHub,
    FlextDbtPackageManager,
    FlextDbtModelRegistry,
    FlextDbtInMemoryExecutor,
    
    # DBT utilities
    create_dbt_hub,
)

# flext-core imports
from flext_core import (
    FlextBaseSettings as BaseConfig,
    FlextEntity as DomainEntity,
    FlextFields as Field,
    FlextResult,
    FlextValueObject as BaseModel,
    FlextValueObject as DomainBaseModel,
    FlextValueObject as DomainValueObject,
    get_logger,
)

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

__all__: list[str] = [
    # === FLEXT-MELTANO DBT RE-EXPORTS ===
    "FlextDbtHub",
    "FlextDbtPackageManager",
    "FlextDbtModelRegistry",
    "FlextDbtInMemoryExecutor",
    "create_dbt_hub",
    
    # === FLEXT-CORE RE-EXPORTS ===
    "FlextResult",
    "get_logger",
    
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
    "process_ldap_entries_for_dbt",
    "validate_ldap_data_quality",
]
