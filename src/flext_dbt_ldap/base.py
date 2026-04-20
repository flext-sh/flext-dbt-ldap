"""Shared service foundation for flext-dbt-ldap components.

Inherits from s which provides dbt command
execution (run_models, run_tests, compile, docs, manifest, CLI).
This base adds typed settings access for dbt-ldap domain.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import (
    Mapping,
)
from typing import Annotated, override

from flext_dbt_ldap import FlextDbtLdapSettings, t
from flext_meltano import FlextMeltanoDbtServiceBase, u


class FlextDbtLdapServiceBase(FlextMeltanoDbtServiceBase):
    """Base class for flext-dbt-ldap services.

    Inherits dbt execution infrastructure from s.
    Adds typed settings for the dbt-ldap domain.
    """

    settings_type: Annotated[
        type[FlextDbtLdapSettings] | None,
        u.Field(
            description="Settings class for DBT LDAP service initialization",
        ),
    ] = FlextDbtLdapSettings
    dbt_project_name: Annotated[
        t.NonEmptyStr,
        u.Field(
            description="Canonical dbt project name for the DBT LDAP service",
        ),
    ] = "dbt-ldap"

    @property
    @override
    def settings(self) -> FlextDbtLdapSettings:
        """Return the typed dbt-ldap settings for this service instance."""
        settings = super().settings
        if not isinstance(settings, FlextDbtLdapSettings):
            msg = "DBT LDAP service runtime settings must be FlextDbtLdapSettings"
            raise TypeError(msg)
        return settings

    @property
    @override
    def connection_profile(self) -> Mapping[str, t.Container]:
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


s = FlextDbtLdapServiceBase

__all__: list[str] = ["FlextDbtLdapServiceBase"]
