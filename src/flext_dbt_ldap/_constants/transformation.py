"""FlextDbtLdapConstantsTransformation - DBT transformation constants.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import ClassVar, Final

from flext_meltano import FlextMeltanoConstants

from flext_dbt_ldap import t


class FlextDbtLdapConstantsTransformation:
    """DBT-specific transformation configuration constants."""

    STG_USERS: Final[str] = "stg_users"
    DIM_USERS: Final[str] = "dim_users"
    STG_GROUPS: Final[str] = "stg_groups"
    DIM_GROUPS: Final[str] = "dim_groups"
    FACT_MEMBERSHIPS: Final[str] = "fact_memberships"

    TIMESTAMP: Final[str] = "timestamp"
    TEXT_ARRAY: Final[str] = "text[]"
    INTEGER: Final[str] = "integer"
    TEXT: Final[str] = "text"
    TIMESTAMP_ATTRS: ClassVar[t.VariadicTuple[str]] = (
        "createtimestamp",
        "modifytimestamp",
    )
    ARRAY_ATTRS: ClassVar[t.VariadicTuple[str]] = ("memberof", "objectclass")
    INTEGER_ATTRS: ClassVar[t.VariadicTuple[str]] = ("uidnumber", "gidnumber")

    DIRECT: Final[str] = "direct"
    OPERATIONAL: Final[str] = "operational"

    PERFORMANCE_EXECUTION_TIME_THRESHOLD: Final[float] = 30.0
    PERFORMANCE_MEMORY_USAGE_THRESHOLD: Final[float] = 1024.0
    PERFORMANCE_ROWS_PROCESSED_THRESHOLD: Final[int] = 100000

    DEFAULT_BATCH_SIZE: Final[int] = FlextMeltanoConstants.DEFAULT_SIZE
    MAX_BATCH_SIZE: Final[int] = FlextMeltanoConstants.MAX_ITEMS

    DEFAULT_PROFILES_DIR: Final[str] = "./profiles"
    DEFAULT_TARGET: Final[str] = "dev"
    DEFAULT_MODEL_PATHS: ClassVar[t.VariadicTuple[str]] = ("models",)
    DEFAULT_ANALYSIS_PATHS: ClassVar[t.VariadicTuple[str]] = ("analyses",)
    DEFAULT_TEST_PATHS: ClassVar[t.VariadicTuple[str]] = ("tests",)
    DEFAULT_SEED_PATHS: ClassVar[t.VariadicTuple[str]] = ("seeds",)
    DEFAULT_MACRO_PATHS: ClassVar[t.VariadicTuple[str]] = ("macros",)
    DEFAULT_SNAPSHOT_PATHS: ClassVar[t.VariadicTuple[str]] = ("snapshots",)
    DEFAULT_CLEAN_TARGETS: ClassVar[t.VariadicTuple[str]] = (
        FlextMeltanoConstants.Meltano.PREFIX_TARGET,
        "dbt_packages",
    )
    ALLOWED_TARGETS: ClassVar[t.VariadicTuple[str]] = ("dev", "staging", "prod")
