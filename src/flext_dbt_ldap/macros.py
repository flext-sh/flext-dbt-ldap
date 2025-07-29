"""FLEXT DBT LDAP Macros - Placeholder module for MyPy compatibility.

This module exists to satisfy MyPy import checking.
All actual macros are imported from flext-ldap library.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_ldap import (
    format_ldap_timestamp,
    parse_dn,
    validate_dn,
)


# Placeholder classes for missing imports
class DNParser:
    """Placeholder for DNParser."""


class LDAPMacros:
    """Placeholder for LDAPMacros."""


class TimestampConverter:
    """Placeholder for TimestampConverter."""


# Re-export for backwards compatibility
__all__ = [
    "DNParser",
    "LDAPMacros",
    "TimestampConverter",
    "format_ldap_timestamp",
    "parse_dn",
    "validate_dn",
]
