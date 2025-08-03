"""FLEXT DBT LDAP Simple API - Placeholder module for MyPy compatibility.

This module exists to satisfy MyPy import checking.
All actual simple API functionality is imported from flext-ldap library.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_ldap import (
    FlextLdapClient,
    FlextLdapConfig,
    FlextLdapResult,
)


# Placeholder functions for missing imports
def create_flext_group_dimension() -> object:
    """Placeholder for create_flext_group_dimension."""
    return None


def create_flext_ldap_transformer() -> object:
    """Placeholder for create_flext_ldap_transformer."""
    return None


def create_flext_user_dimension() -> object:
    """Placeholder for create_flext_user_dimension."""
    return None


# Re-export for backwards compatibility
__all__ = [
    "FlextLdapClient",
    "FlextLdapConfig",
    "FlextLdapResult",
    "create_flext_group_dimension",
    "create_flext_ldap_transformer",
    "create_flext_user_dimension",
]
