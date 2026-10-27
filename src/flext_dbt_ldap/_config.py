"""FlextDbtLdapConfig — frozen config singleton for flext-dbt-ldap (ADR-005 §7).

Model-less: business rules live in ``config/*.yaml`` under the ``DbtLdap:`` key and
are exposed through the open ``config.DbtLdap`` namespace (``extra="allow"``), with
no per-domain model. Access is ``config.DbtLdap.<domain>[<key>...]``.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Annotated

from flext_meltano import FlextMeltanoConfig
from pydantic import BaseModel, ConfigDict, Field

from flext_dbt_ldap.config_models import FlextDbtLdapModelsConfig


class FlextDbtLdapConfig(FlextMeltanoConfig):
    """DbtLdap config auto-loaded model-less from ``config/*.yaml``."""

    class Namespace(BaseModel):
        """Open, frozen payload for the owned configuration domain."""

        model_config = ConfigDict(extra="allow", frozen=True)

    DbtLdap: Annotated[
        FlextDbtLdapModelsConfig.DbtLdapNamespace,
        Field(
            description="Open namespace exposing ``config/*.yaml`` under ``DbtLdap``.",
        ),
    ] = FlextDbtLdapModelsConfig.DbtLdapNamespace()


config: FlextDbtLdapConfig = FlextDbtLdapConfig.fetch_global()
"""Pre-instantiated frozen config singleton — ``from flext_dbt_ldap import config``."""

__all__: list[str] = ["FlextDbtLdapConfig", "config"]
