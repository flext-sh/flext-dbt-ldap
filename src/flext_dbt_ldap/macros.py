"""FLEXT DBT LDAP Macros.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_core import FlextLogger
from pydantic import TypeAdapter, ValidationError

logger = FlextLogger(__name__)
_STRING_LIST_ADAPTER = TypeAdapter(list[str])


class FlextDbtLdapMacros:
    """Unified DBT LDAP macros collection with nested helpers."""

    class _DNParser:
        """DN parser utilities for DBT LDAP macros."""

        @staticmethod
        def get_parent_dn(dn: str) -> str | None:
            """Get parent DN from a distinguished name.

            Args:
            dn: Distinguished name

            Returns:
            Parent DN or None if error

            """
            try:
                parts = [p.strip() for p in dn.split(",") if p.strip()]
                if len(parts) > 1:
                    return ",".join(parts[1:])
                return None
            except (
                ValueError,
                TypeError,
                KeyError,
                AttributeError,
                OSError,
                RuntimeError,
                ImportError,
            ):
                logger.exception("Failed to get parent DN: %s", dn)
                return None

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
                # Very simple DN parsing: split by commas, then by '='
                parts = [p.strip() for p in dn.split(",") if "=" in p]
                for part in parts:
                    key, value = part.split("=", 1)
                    if key.lower() == component.lower():
                        return value
                return None
            except (
                ValueError,
                TypeError,
                KeyError,
                AttributeError,
                OSError,
                RuntimeError,
                ImportError,
            ):
                logger.exception("Failed to parse DN component: %s", dn)
                return None

    class _TimestampConverter:
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
                # Basic passthrough; customize if needed
                return timestamp
            except (
                ValueError,
                TypeError,
                KeyError,
                AttributeError,
                OSError,
                RuntimeError,
                ImportError,
            ):
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
            converted = FlextDbtLdapMacros._TimestampConverter.convert_ldap_timestamp(
                timestamp,
            )
            if converted:
                # Extract date part (assuming ISO format)
                return converted.split("T")[0] if "T" in converted else converted[:10]
            return None

    @staticmethod
    def convert_ldap_timestamp(timestamp: str) -> str | None:
        """Convert LDAP timestamp to standard format.

        Args:
        timestamp: LDAP timestamp string

        Returns:
        ISO format timestamp or None if conversion fails

        """
        return FlextDbtLdapMacros._TimestampConverter.convert_ldap_timestamp(timestamp)

    @staticmethod
    def extract_date_from_timestamp(timestamp: str) -> str | None:
        """Extract date part from LDAP timestamp.

        Args:
        timestamp: LDAP timestamp string

        Returns:
        Date string (YYYY-MM-DD) or None if extraction fails

        """
        return FlextDbtLdapMacros._TimestampConverter.extract_date_from_timestamp(
            timestamp,
        )

    @staticmethod
    def extract_group_name_from_dn(dn: str) -> str | None:
        """Extract group name from DN.

        Looks for cn attribute in the DN.

        Args:
        dn: Distinguished name

        Returns:
        Group name or None if not found

        """
        return FlextDbtLdapMacros._DNParser.parse_dn_component(dn, "cn")

    @staticmethod
    def extract_user_id_from_dn(dn: str) -> str | None:
        """Extract user ID from DN.

        Looks for uid, cn, or sam attributes in the DN.

        Args:
        dn: Distinguished name

        Returns:
        User ID or None if not found

        """
        # Try different common user ID attributes
        for attr in ["uid", "cn", "samaccountname"]:
            user_id = FlextDbtLdapMacros._DNParser.parse_dn_component(dn, attr)
            if user_id:
                return user_id

        return None

    @staticmethod
    def get_parent_dn(dn: str) -> str | None:
        """Get parent DN from a distinguished name.

        Args:
        dn: Distinguished name

        Returns:
        Parent DN or None if error

        """
        return FlextDbtLdapMacros._DNParser.get_parent_dn(dn)

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

    @staticmethod
    def normalize_ldap_attribute(value: str | list[str] | None) -> str:
        """Normalize LDAP attribute value for DBT processing.

        Args:
        value: LDAP attribute value (can be list or single value)

        Returns:
        Normalized string value

        """
        if value is None:
            return ""
        try:
            values = _STRING_LIST_ADAPTER.validate_python(value)
        except ValidationError:
            return str(value)
        return str(values[0]) if values else ""

    @staticmethod
    def parse_dn_component(dn: str, component: str) -> str | None:
        """Parse specific component from DN.

        Args:
        dn: Distinguished name to parse
        component: Component to extract (cn, ou, dc, etc.)

        Returns:
        Component value or None if not found

        """
        return FlextDbtLdapMacros._DNParser.parse_dn_component(dn, component)


__all__: list[str] = [
    "FlextDbtLdapMacros",
]
