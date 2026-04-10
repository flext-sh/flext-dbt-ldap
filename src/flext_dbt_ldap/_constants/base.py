"""FlextDbtLdapConstantsBase - DBT LDAP foundational constants.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Final


class FlextDbtLdapConstantsBase:
    """Base constants for DBT LDAP domain."""

    DEFAULT_QUALITY_THRESHOLD: Final[float] = 0.8
    DBT_SCHEMA_VERSION: Final[str] = "2"
    DEFAULT_REPORT_TYPE: Final[str] = "summary"
    DEFAULT_DBT_ADAPTER: Final[str] = "postgres"
    DEFAULT_DBT_USER: Final[str] = "dbt_user"
    DEFAULT_DBT_DATABASE: Final[str] = "ldap_db"
    DEFAULT_DBT_SCHEMA: Final[str] = "public"
    DEFAULT_DBT_THREADS: Final[int] = 4
