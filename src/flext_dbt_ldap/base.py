"""Shared service foundation for flext-dbt-ldap components.

Inherits from FlextMeltanoDbtServiceBase which provides dbt command
execution (run_models, run_tests, compile, docs, manifest, CLI).
This base adds typed settings access for dbt-ldap domain.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import override

from flext_core import FlextSettings
from flext_meltano import FlextMeltanoDbtServiceBase

from flext_dbt_ldap import FlextDbtLdapSettings, t


class FlextDbtLdapServiceBase(FlextMeltanoDbtServiceBase):
    """Base class for flext-dbt-ldap services.

    Inherits dbt execution infrastructure from FlextMeltanoDbtServiceBase.
    Adds typed settings for the dbt-ldap domain.
    """

    dbt_project_name: t.NonEmptyStr = "dbt-ldap"

    def _dbt_ldap_settings(self) -> FlextDbtLdapSettings:
        """Return the typed dbt-ldap settings namespace."""
        return FlextSettings.get_global().get_namespace(
            "dbt_ldap", FlextDbtLdapSettings
        )

    @override
    def get_connection_profile(self) -> t.ContainerMapping:
        """Return dbt connection profile for LDAP."""
        s = self._dbt_ldap_settings()
        return {
            "type": "ldap",
            "host": s.ldap_host,
            "port": s.ldap_port,
            "use_tls": s.ldap_use_tls,
            "base_dn": s.ldap_base_dn,
            "project": self.dbt_project_name,
        }


__all__ = ["FlextDbtLdapServiceBase"]
