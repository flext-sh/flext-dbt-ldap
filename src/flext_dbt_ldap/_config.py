"""FlextDbtLdapConfig — frozen config singleton for flext-dbt-ldap (ADR-005 §7).

Model-less: business rules live in ``config/*.yaml`` under the ``DbtLdap:`` key and
are exposed through the open ``config.DbtLdap`` namespace (``extra="allow"``), with
no per-domain model. Access is ``config.DbtLdap.<domain>[<key>...]``.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from flext_meltano import FlextMeltanoConfig


class _DbtLdapNamespace(BaseModel):
    """Open, frozen namespace exposing every ``config/*.yaml`` domain model-less."""

    model_config = ConfigDict(extra="allow", frozen=True)


class FlextDbtLdapConfig(FlextMeltanoConfig):
    """DbtLdap config auto-loaded model-less from ``config/*.yaml``."""

    DbtLdap: _DbtLdapNamespace = _DbtLdapNamespace()


config: FlextDbtLdapConfig = FlextDbtLdapConfig.fetch_global()
"""Pre-instantiated frozen config singleton — ``from flext_dbt_ldap import config``."""

__all__: list[str] = ["FlextDbtLdapConfig", "config"]
