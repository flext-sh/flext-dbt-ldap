"""Shared service foundation for flext-dbt-ldap components.

Inherits from s which provides dbt command
execution (run_models, run_tests, compile, docs, manifest, CLI).
This base adds typed settings access for dbt-ldap domain.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Annotated, override

from flext_core import FlextSettings
from flext_dbt_ldap import FlextDbtLdapSettings, t
from flext_meltano import FlextMeltanoDbtServiceBase, u


class FlextDbtLdapServiceBase(FlextMeltanoDbtServiceBase):
    """Base class for flext-dbt-ldap services.

    Inherits dbt execution infrastructure from s.
    Adds typed settings for the dbt-ldap domain.
    """

    settings_type: Annotated[
        type | None,
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
        """Return the typed dbt-ldap settings namespace."""
        return FlextSettings.fetch_global().fetch_namespace(
            "dbt-ldap", FlextDbtLdapSettings
        )

    @property
    @override
    def connection_profile(self) -> t.JsonMapping:
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

__all__: t.MutableSequenceOf[str] = ["FlextDbtLdapServiceBase"]
