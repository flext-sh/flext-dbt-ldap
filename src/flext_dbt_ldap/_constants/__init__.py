# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Ldap. Constants package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_dbt_ldap._constants.attributes import FlextDbtLdapConstantsAttributes
    from flext_dbt_ldap._constants.base import FlextDbtLdapConstantsBase
    from flext_dbt_ldap._constants.search import FlextDbtLdapConstantsSearch
    from flext_dbt_ldap._constants.transformation import (
        FlextDbtLdapConstantsTransformation,
    )


__all__: tuple[str, ...] = (
    "FlextDbtLdapConstantsAttributes",
    "FlextDbtLdapConstantsBase",
    "FlextDbtLdapConstantsSearch",
    "FlextDbtLdapConstantsTransformation",
)

install_lazy_exports(
    __name__,
    globals(),
    {
        "FlextDbtLdapConstantsAttributes": ".attributes",
        "FlextDbtLdapConstantsBase": ".base",
        "FlextDbtLdapConstantsSearch": ".search",
        "FlextDbtLdapConstantsTransformation": ".transformation",
    },
    public_exports=__all__,
    deferred_members={
        "FlextDbtLdapConstantsAttributes": (
            "UID",
            "CN",
            "MAIL",
            "DISPLAY_NAME",
            "DEPARTMENT",
            "MANAGER",
            "DESCRIPTION",
            "MEMBER",
            "GROUP_TYPE",
            "MEMBER_OF",
            "UNIQUE_MEMBER",
            "SAM_ACCOUNT_NAME",
            "EMPLOYEE_NUMBER",
            "TELEPHONE_NUMBER",
            "USER_ACCOUNT_CONTROL",
            "CREATE_TIMESTAMP",
            "MODIFY_TIMESTAMP",
            "MEMBER_UID",
            "MEMBERSHIP_ATTRIBUTES",
            "USERS_CLASSES",
            "GROUPS_CLASSES",
            "ORG_UNITS_CLASSES",
            "USERS",
            "GROUPS",
            "ORG_UNITS",
        ),
        "FlextDbtLdapConstantsBase": (
            "DEFAULT_QUALITY_THRESHOLD",
            "DBT_SCHEMA_VERSION",
            "DEFAULT_REPORT_TYPE",
            "DEFAULT_DBT_SCHEMA",
        ),
        "FlextDbtLdapConstantsSearch": (
            "FILTER_USER",
            "FILTER_GROUP",
            "FILTER_MEMBERSHIP",
            "SEARCH_GROUP",
            "SEARCH_MEMBERSHIP",
            "LDAPS_DEFAULT_PORT",
        ),
        "FlextDbtLdapConstantsTransformation": (
            "STG_USERS",
            "DIM_USERS",
            "STG_GROUPS",
            "DIM_GROUPS",
            "FACT_MEMBERSHIPS",
            "TIMESTAMP",
            "INTEGER",
            "TEXT",
            "DIRECT",
            "OPERATIONAL",
            "DEFAULT_BATCH_SIZE",
            "MAX_BATCH_SIZE",
            "DEFAULT_PROFILES_DIR",
            "DEFAULT_TARGET",
            "DEFAULT_MODEL_PATHS",
            "DEFAULT_ANALYSIS_PATHS",
            "DEFAULT_TEST_PATHS",
            "DEFAULT_SEED_PATHS",
            "DEFAULT_MACRO_PATHS",
            "DEFAULT_SNAPSHOT_PATHS",
            "DEFAULT_CLEAN_TARGETS",
        ),
    },
)
