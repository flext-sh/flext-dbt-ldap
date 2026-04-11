"""Shared service foundation for flext-dbt-ldap components.

Inherits from FlextMeltanoDbtServiceBase which provides dbt command
execution (run_models, run_tests, compile, docs, manifest, CLI).
This base adds typed settings access for dbt-ldap domain.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import override

from pydantic import Field

from flext_dbt_ldap import FlextDbtLdapSettings, t
from flext_meltano import FlextMeltanoDbtServiceBase


class FlextDbtLdapServiceBase(FlextMeltanoDbtServiceBase):
    """Base class for flext-dbt-ldap services.

    Inherits dbt execution infrastructure from FlextMeltanoDbtServiceBase.
    Adds typed settings for the dbt-ldap domain.
    """

    config_type: type | None = Field(
        default=FlextDbtLdapSettings,
        description="Configuration class for DBT LDAP service initialization",
    )
    dbt_project_name: t.NonEmptyStr = Field(
        default="dbt-ldap",
        description="Canonical dbt project name for the DBT LDAP service",
    )

    @property
    @override
    def settings(self) -> FlextDbtLdapSettings:
        """Return the typed dbt-ldap configuration for this service instance."""
        settings = super().settings
        if isinstance(settings, FlextDbtLdapSettings):
            return settings
        return FlextDbtLdapSettings.model_validate(self.config_overrides or {})

    @override
    @property
    @override
    def connection_profile(self) -> t.ContainerMapping:
        """Dbt connection profile for LDAP."""
        s = self.settings
        return {
            "type": "ldap",
            "host": s.ldap_host,
            "port": s.ldap_port,
            "use_tls": s.ldap_use_tls,
            "base_dn": s.ldap_base_dn,
            "project": self.dbt_project_name,
        }


__all__ = ["FlextDbtLdapServiceBase"]
