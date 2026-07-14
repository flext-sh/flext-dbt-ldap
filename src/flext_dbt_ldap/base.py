"""Shared service foundation for flext-dbt-ldap components.

Inherits from s which provides dbt command
execution (run_models, run_tests, compile, docs, manifest, CLI).
This base adds typed settings access for dbt-ldap domain.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Annotated, override

from flext_dbt_ldap import FlextDbtLdapSettings, m, t
from flext_meltano import FlextMeltanoDbtServiceBase, p, u


class FlextDbtLdapServiceBase(FlextMeltanoDbtServiceBase):
    """Base class for flext-dbt-ldap services.

    Inherits dbt execution infrastructure from s.
    Adds typed settings for the dbt-ldap domain.
    """

    dbt_project_name: Annotated[
        t.NonEmptyStr,
        u.Field(
            description="Canonical dbt project name for the DBT LDAP service",
        ),
    ] = "dbt-ldap"

    @classmethod
    def _runtime_bootstrap_options(cls) -> m.RuntimeBootstrapOptions:
        """Return runtime bootstrap options for DBT LDAP services."""
        return m.RuntimeBootstrapOptions(settings_type=FlextDbtLdapSettings)

    @property
    @override
    def connection_profile(self) -> p.Meltano.DbtConnectionProfile:
        """Dbt connection profile for LDAP-backed workflows."""
        # NOTE (multi-agent): mro-rn88 — read INJECTED settings via settings (runtime,
        # not the global singleton); connection scalars from Ldap.*, base_dn from DbtLdap.
        return m.DbtLdap.DbtConnectionProfile(
            host=settings.Ldap.host,
            port=settings.Ldap.port,
            use_tls=settings.Ldap.use_tls,
            base_dn=settings.DbtLdap.ldap_base_dn,
            project=self.dbt_project_name,
        )


s = FlextDbtLdapServiceBase

__all__: t.MutableSequenceOf[str] = ["FlextDbtLdapServiceBase", "s"]
