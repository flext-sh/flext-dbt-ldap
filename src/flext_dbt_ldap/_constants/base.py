"""FlextDbtLdapConstantsBase - DBT LDAP foundational constants.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Final


class FlextDbtLdapConstantsBase:
    """Base constants for DBT LDAP domain."""

    DEFAULT_QUALITY_THRESHOLD: Final[float] = 0.8
    DBT_SCHEMA_VERSION: Final[str] = "2"
    DEFAULT_REPORT_TYPE: Final[str] = c.MetricType.SUMMARY
    DEFAULT_DBT_SCHEMA: Final[str] = "public"


__all__: list[str] = ["FlextDbtLdapConstantsBase"]
