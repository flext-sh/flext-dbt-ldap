"""FLEXT DBT LDAP Macros - DBT macro utilities for LDAP transformations.

Provides DBT macro utilities and helper functions for LDAP data transformations.
Integrates with flext-ldap functions for DN parsing and timestamp formatting.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_core import get_logger
from flext_ldap.utils import (
    flext_ldap_format_timestamp,
    flext_ldap_parse_dn,
    flext_ldap_validate_dn,
)

logger = get_logger(__name__)


class FlextDbtLdapDNParser:
    """DN parser utilities for DBT LDAP macros."""

    @staticmethod
    def parse_dn_component(dn: str, component: str) -> str | None:
        """Parse specific component from DN.

        Args:
            dn: Distinguished name to parse
            component: Component to extract (cn, ou, dc, etc.)

        Returns:
            Component value or None if not found

        """
        try:
            parsed = flext_ldap_parse_dn(dn)
            if parsed:
                # Extract component from parsed DN components
                for component_dict in parsed:
                    if component.lower() in component_dict:
                        return component_dict[component.lower()]
            return None
        except Exception:
            logger.exception("Failed to parse DN component: %s", dn)
            return None

    @staticmethod
    def get_parent_dn(dn: str) -> str | None:
        """Get parent DN from a distinguished name.

        Args:
            dn: Distinguished name

        Returns:
            Parent DN or None if error

        """
        try:
            parsed = flext_ldap_parse_dn(dn)
            if parsed and len(parsed) > 1:
                # Return DN without first component
                parent_components = parsed[1:]
                # Reconstruct DN from remaining components
                parent_parts = []
                for comp_dict in parent_components:
                    for attr, value in comp_dict.items():
                        parent_parts.append(f"{attr}={value}")
                return ",".join(parent_parts)
            return None
        except Exception:
            logger.exception("Failed to get parent DN: %s", dn)
            return None


class FlextDbtLdapMacros:
    """Main DBT LDAP macros collection."""

    @staticmethod
    def extract_user_id_from_dn(dn: str) -> str | None:
        """Extract user ID from DN.

        Looks for uid, cn, or sam attributes in the DN.

        Args:
            dn: Distinguished name

        Returns:
            User ID or None if not found

        """
        parser = FlextDbtLdapDNParser()

        # Try different common user ID attributes
        for attr in ["uid", "cn", "samaccountname"]:
            user_id = parser.parse_dn_component(dn, attr)
            if user_id:
                return user_id

        return None

    @staticmethod
    def extract_group_name_from_dn(dn: str) -> str | None:
        """Extract group name from DN.

        Looks for cn attribute in the DN.

        Args:
            dn: Distinguished name

        Returns:
            Group name or None if not found

        """
        parser = FlextDbtLdapDNParser()
        return parser.parse_dn_component(dn, "cn")

    @staticmethod
    def normalize_ldap_attribute(value: object) -> str:
        """Normalize LDAP attribute value for DBT processing.

        Args:
            value: LDAP attribute value (can be list or single value)

        Returns:
            Normalized string value

        """
        if value is None:
            return ""

        if isinstance(value, list):
            # Take first value from list
            return str(value[0]) if value else ""

        return str(value)

    @staticmethod
    def is_user_active(user_account_control: int | None) -> bool:
        """Check if user account is active based on userAccountControl.

        Args:
            user_account_control: AD userAccountControl value

        Returns:
            True if user is active, False otherwise

        """
        if user_account_control is None:
            return True  # Assume active if not specified

        # Check if account is disabled (bit 1)
        return not bool(user_account_control & 0x0002)


class FlextDbtLdapTimestampConverter:
    """Timestamp conversion utilities for DBT LDAP macros."""

    @staticmethod
    def convert_ldap_timestamp(timestamp: str) -> str | None:
        """Convert LDAP timestamp to standard format.

        Args:
            timestamp: LDAP timestamp string

        Returns:
            ISO format timestamp or None if conversion fails

        """
        try:
            return flext_ldap_format_timestamp(timestamp)
        except Exception:
            logger.exception("Error converting timestamp: %s", timestamp)
            return None

    @staticmethod
    def extract_date_from_timestamp(timestamp: str) -> str | None:
        """Extract date part from LDAP timestamp.

        Args:
            timestamp: LDAP timestamp string

        Returns:
            Date string (YYYY-MM-DD) or None if extraction fails

        """
        converted = FlextDbtLdapTimestampConverter.convert_ldap_timestamp(timestamp)
        if converted:
            # Extract date part (assuming ISO format)
            return converted.split("T")[0] if "T" in converted else converted[:10]
        return None


# Backward compatibility aliases
DNParser = FlextDbtLdapDNParser
LDAPMacros = FlextDbtLdapMacros
TimestampConverter = FlextDbtLdapTimestampConverter


# Re-export for backwards compatibility
__all__: list[str] = [
    "DNParser",
    "FlextDbtLdapDNParser",
    "FlextDbtLdapMacros",
    "FlextDbtLdapTimestampConverter",
    "LDAPMacros",
    "TimestampConverter",
    "flext_ldap_format_timestamp",
    "flext_ldap_parse_dn",
    "flext_ldap_validate_dn",
]
