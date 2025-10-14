"""FLEXT DBT LDAP - Type aliases and compatibility definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_core import FlextCore

# ================================
# TYPE ALIASES AND COMPATIBILITY
# ================================

# FlextDbtLdap-specific aliases (following FlextXxx pattern)
FlextDbtLdap: type | None = None  # Will be set to platform when available
FlextDbtLdapResult = FlextCore.Result  # FlextDbtLdap result pattern

# Legacy compatibility - use FlextCore.Models directly
DomainBaseModel = FlextCore.Models.ArbitraryTypesModel  # Domain base model

__all__ = [
    "DomainBaseModel",
    "FlextDbtLdap",
    "FlextDbtLdapResult",
]
