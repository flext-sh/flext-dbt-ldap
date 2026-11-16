# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Ldap. Models package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import defer_lazy_bases, install_lazy_exports

if TYPE_CHECKING:
    from flext_dbt_ldap._models.config import FlextDbtLdapModelsConfig
    from flext_dbt_ldap._models.dbt import FlextDbtLdapModelsDbt
    from flext_dbt_ldap._models.dimensions import FlextDbtLdapModelsDimensions
    from flext_dbt_ldap._models.results import FlextDbtLdapModelsResults
    from flext_dbt_ldap._models.schema import FlextDbtLdapModelsSchema
    from flext_dbt_ldap._models.shared import FlextDbtLdapModelsShared


__all__: tuple[str, ...] = (
    "FlextDbtLdapModelsConfig",
    "FlextDbtLdapModelsDbt",
    "FlextDbtLdapModelsDimensions",
    "FlextDbtLdapModelsResults",
    "FlextDbtLdapModelsSchema",
    "FlextDbtLdapModelsShared",
)

install_lazy_exports(
    __name__,
    globals(),
    {
        "FlextDbtLdapModelsConfig": ".config",
        "FlextDbtLdapModelsDbt": ".dbt",
        "FlextDbtLdapModelsDimensions": ".dimensions",
        "FlextDbtLdapModelsResults": ".results",
        "FlextDbtLdapModelsSchema": ".schema",
        "FlextDbtLdapModelsShared": ".shared",
    },
    public_exports=__all__,
    deferred_members={
        "FlextDbtLdapModelsConfig": (),
        "FlextDbtLdapModelsDbt": (
            "DbtConnectionProfile",
            "DbtProjectConfig",
            "DbtSourceFreshness",
            "DbtSourceDefinition",
            "DbtConfig",
        ),
        "FlextDbtLdapModelsDimensions": (
            "UserDimension",
            "GroupDimension",
            "MembershipFact",
        ),
        "FlextDbtLdapModelsResults": (
            "ValidationMetrics",
            "DbtRunStatus",
            "DbtLdapPipelineResult",
            "SyncResult",
            "PerformanceAnalysis",
            "ServiceStatus",
            "AnalyticsReport",
        ),
        "FlextDbtLdapModelsSchema": (
            "DbtModelDefinition",
            "DbtTestConfig",
            "TransformationConfig",
            "TransformationRule",
            "DataValidationConfig",
            "LdapSchema",
            "LdapQuery",
        ),
        "FlextDbtLdapModelsShared": (
            "DbtSerializable",
            "DbtDimensionBase",
        ),
    },
)

defer_lazy_bases(
    __name__,
    {
        "FlextDbtLdapModelsConfig": (
            ("flext_dbt_ldap", "FlextDbtLdapModelsConfigNamespace"),
        ),
        "FlextDbtLdapModelsDimensions": ((".", "FlextDbtLdapModelsShared"),),
        "FlextDbtLdapModelsResults": ((".", "FlextDbtLdapModelsShared"),),
    },
)
