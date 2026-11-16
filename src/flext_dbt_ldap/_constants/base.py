"""FlextDbtLdapConstantsBase - DBT LDAP foundational constants.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import ClassVar

from flext_meltano import c


class FlextDbtLdapConstantsBase:
    """Base constants for DBT LDAP domain."""

    DEFAULT_QUALITY_THRESHOLD: ClassVar[float] = 0.8
    DBT_SCHEMA_VERSION: ClassVar[str] = "2"
    DEFAULT_REPORT_TYPE: ClassVar[str] = c.MetricType.SUMMARY
    DEFAULT_DBT_SCHEMA: ClassVar[str] = "public"


__all__: list[str] = ["FlextDbtLdapConstantsBase"]
