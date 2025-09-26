"""FLEXT DBT LDAP Constants - LDAP DBT transformation constants.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import ClassVar

from flext_core import FlextConstants


class FlextDbtLdapConstants(FlextConstants):
    """LDAP DBT transformation-specific constants following FLEXT unified pattern with nested domains."""

    class Connection:
        """LDAP connection configuration constants."""

        class Ldap:
            """Standard LDAP connection settings."""

            DEFAULT_HOST = FlextConstants.Platform.DEFAULT_HOST
            DEFAULT_PORT = FlextConstants.Platform.LDAP_DEFAULT_PORT
            DEFAULT_TIMEOUT = FlextConstants.Network.DEFAULT_TIMEOUT

        class Ldaps:
            """Secure LDAP connection settings."""

            DEFAULT_PORT = FlextConstants.Platform.LDAPS_DEFAULT_PORT

    class Dbt:
        """DBT-specific configuration constants."""

        DEFAULT_PROFILES_DIR = "./profiles"
        DEFAULT_TARGET = "dev"
        ALLOWED_TARGETS: ClassVar[list[str]] = ["dev", "staging", "prod"]

    class Processing:
        """DBT LDAP transformation configuration."""

        DEFAULT_BATCH_SIZE = FlextConstants.Performance.BatchProcessing.DEFAULT_SIZE
        MAX_BATCH_SIZE = FlextConstants.Performance.BatchProcessing.MAX_ITEMS


__all__ = ["FlextDbtLdapConstants"]
