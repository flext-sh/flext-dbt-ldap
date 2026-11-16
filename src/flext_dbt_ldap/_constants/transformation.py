"""FlextDbtLdapConstantsTransformation - DBT transformation constants.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import ClassVar

from flext_meltano import c


class FlextDbtLdapConstantsTransformation:
    """DBT-specific transformation configuration constants."""

    STG_USERS: ClassVar[str] = "stg_users"
    DIM_USERS: ClassVar[str] = "dim_users"
    STG_GROUPS: ClassVar[str] = "stg_groups"
    DIM_GROUPS: ClassVar[str] = "dim_groups"
    FACT_MEMBERSHIPS: ClassVar[str] = "fact_memberships"

    TIMESTAMP: ClassVar[str] = "timestamp"
    INTEGER: ClassVar[str] = "integer"
    TEXT: ClassVar[str] = "text"

    DIRECT: ClassVar[str] = "direct"
    OPERATIONAL: ClassVar[str] = "operational"

    DEFAULT_BATCH_SIZE: ClassVar[int] = c.DEFAULT_SIZE
    MAX_BATCH_SIZE: ClassVar[int] = c.MAX_ITEMS

    DEFAULT_PROFILES_DIR: ClassVar[str] = "./profiles"
    DEFAULT_TARGET: ClassVar[str] = "dev"
    DEFAULT_MODEL_PATHS: ClassVar[tuple[str, ...]] = ("models",)
    DEFAULT_ANALYSIS_PATHS: ClassVar[tuple[str, ...]] = ("analyses",)
    DEFAULT_TEST_PATHS: ClassVar[tuple[str, ...]] = ("tests",)
    DEFAULT_SEED_PATHS: ClassVar[tuple[str, ...]] = ("seeds",)
    DEFAULT_MACRO_PATHS: ClassVar[tuple[str, ...]] = ("macros",)
    DEFAULT_SNAPSHOT_PATHS: ClassVar[tuple[str, ...]] = ("snapshots",)
    DEFAULT_CLEAN_TARGETS: ClassVar[tuple[str, ...]] = (
        c.Meltano.PREFIX_TARGET,
        "dbt_packages",
    )


__all__: list[str] = ["FlextDbtLdapConstantsTransformation"]
