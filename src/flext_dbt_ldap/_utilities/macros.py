"""FLEXT DBT LDAP Utilities — macro helpers.

DN parsing is owned by flext-ldif ``u.Ldif.DN``; only dbt-specific helpers live here.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_dbt_ldap import t


class FlextDbtLdapUtilitiesMacros:
    """Unified DBT LDAP macros collection."""

    @staticmethod
    def user_active(user_account_control: int | None) -> bool:
        """Check if user account is active based on userAccountControl."""
        if user_account_control is None:
            return True
        return not bool(user_account_control & 2)


__all__: t.StrSequence = ("FlextDbtLdapUtilitiesMacros",)
