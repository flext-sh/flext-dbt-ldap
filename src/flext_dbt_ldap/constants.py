"""FLEXT DBT LDAP Constants - LDAP DBT transformation constants.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import ClassVar

from flext_core import FlextConstants


class FlextDbtLdapConstants(FlextConstants):
    """LDAP DBT transformation-specific constants following flext-core patterns."""

    # LDAP Configuration
    DEFAULT_LDAP_HOST = "localhost"
    DEFAULT_LDAP_PORT = 389
    DEFAULT_LDAPS_PORT = 636
    DEFAULT_LDAP_TIMEOUT = 30

    # DBT Configuration
    DEFAULT_DBT_PROFILES_DIR = "./profiles"
    DEFAULT_DBT_TARGET = "dev"
    DBT_ALLOWED_TARGETS: ClassVar[list[str]] = ["dev", "staging", "prod"]

    # LDAP DBT Model Configuration
    DEFAULT_BATCH_SIZE = 1000
    MAX_BATCH_SIZE = 10000
    DEFAULT_SCHEMA = "ldap_analytics"


__all__ = ["FlextDbtLdapConstants"]
