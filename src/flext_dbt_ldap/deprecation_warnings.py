"""FLEXT DBT LDAP - Deprecation warning system.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import warnings


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


# Configure warnings for clean output
warnings.filterwarnings("ignore", category=UserWarning)


__all__ = [
    "FlextDbtLdapDeprecationWarning",
    "_show_deprecation_warning",
]
