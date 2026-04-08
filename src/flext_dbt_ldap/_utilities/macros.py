"""FLEXT DBT LDAP Utilities — macro helpers.

Absorbed from macros.py into u.DbtLdap namespace.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_core import FlextLogger
from flext_dbt_ldap import c, t

logger = FlextLogger(__name__)


class FlextDbtLdapUtilitiesMacros:
    """Unified DBT LDAP macros collection."""

    @staticmethod
    def extract_date_from_timestamp(timestamp: str) -> str | None:
        """Extract date part from LDAP timestamp.

        Args:
        timestamp: LDAP timestamp string (ISO or GeneralizedTime)

        Returns:
        Date string (YYYY-MM-DD) or None if extraction fails

        """
        try:
            return (
                timestamp.split("T", maxsplit=1)[0]
                if "T" in timestamp
                else timestamp[:10]
            )
        except c.Meltano.SINGER_SAFE_EXCEPTIONS:
            logger.exception("Error extracting date from timestamp: %s", timestamp)
            return None

    @staticmethod
    def extract_group_name_from_dn(dn: str) -> str | None:
        """Extract group name (cn) from DN."""
        return FlextDbtLdapUtilitiesMacros.parse_dn_component(dn, c.DbtLdap.CN)

    @staticmethod
    def extract_user_id_from_dn(dn: str) -> str | None:
        """Extract user ID from DN (tries uid, cn, samaccountname)."""
        for attr in c.DbtLdap.USER_ID_ATTRIBUTES:
            user_id = FlextDbtLdapUtilitiesMacros.parse_dn_component(dn, attr)
            if user_id:
                return user_id
        return None

    @staticmethod
    def get_parent_dn(dn: str) -> str | None:
        """Get parent DN from a distinguished name."""
        try:
            parts = [p.strip() for p in dn.split(",") if p.strip()]
            if len(parts) > 1:
                return ",".join(parts[1:])
            return None
        except c.Meltano.SINGER_SAFE_EXCEPTIONS:
            logger.exception("Failed to get parent DN: %s", dn)
            return None

    @staticmethod
    def is_user_active(user_account_control: int | None) -> bool:
        """Check if user account is active based on userAccountControl."""
        if user_account_control is None:
            return True
        return not bool(user_account_control & 2)

    @staticmethod
    def normalize_ldap_attribute(value: str | t.StrSequence | None) -> str:
        """Normalize LDAP attribute value for DBT processing."""
        if value is None:
            return ""
        if isinstance(value, str):
            return value
        return str(value[0]) if value else ""

    @staticmethod
    def parse_dn_component(dn: str, component: str) -> str | None:
        """Parse specific component from DN."""
        try:
            parts = [p.strip() for p in dn.split(",") if "=" in p]
            for part in parts:
                key, value = part.split("=", 1)
                if key.lower() == component.lower():
                    return value
            return None
        except c.Meltano.SINGER_SAFE_EXCEPTIONS:
            logger.exception("Failed to parse DN component: %s", dn)
            return None


__all__: t.StrSequence = ["FlextDbtLdapUtilitiesMacros"]
