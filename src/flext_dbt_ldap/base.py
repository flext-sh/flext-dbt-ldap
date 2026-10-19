"""Shared service foundation for flext-dbt-ldap components.

Inherits from s which provides dbt command
execution (run_models, run_tests, compile, docs, manifest, CLI).
This base adds typed settings access for dbt-ldap domain.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Annotated, override

from flext_meltano import FlextMeltanoDbtServiceBase

from flext_dbt_ldap import FlextDbtLdapSettings, m, p, t


class FlextDbtLdapServiceBase(FlextMeltanoDbtServiceBase):
    """Base class for flext-dbt-ldap services.

    Inherits dbt execution infrastructure from s.
    Adds typed settings for the dbt-ldap domain.
    """

    dbt_project_name: Annotated[
        t.NonEmptyStr,
        m.Field(description="Canonical dbt project name for the DBT LDAP service"),
    ] = "dbt-ldap"

    @classmethod
    def runtime_bootstrap_options(cls) -> m.RuntimeBootstrapOptions:
        """Return runtime bootstrap options for DBT LDAP services.

        Returns:
            The resulting ``m.RuntimeBootstrapOptions``.

        """
        return m.RuntimeBootstrapOptions(settings_type=FlextDbtLdapSettings)

    @property
    @override
    def settings(self) -> FlextDbtLdapSettings:
        """The typed dbt-ldap settings from the INJECTED runtime (not the global).

        Returns:
            The resulting ``FlextDbtLdapSettings``.

        """
        # NOTE (multi-agent): mro-rn88 — narrow the runtime-injected settings so test
        # overrides (e.g. dbt_project_dir) are honored; fall back to the typed global.
        runtime_settings = super().settings
        if isinstance(runtime_settings, FlextDbtLdapSettings):
            return runtime_settings
        return FlextDbtLdapSettings.fetch_global()

    @property
    @override
    def connection_profile(self) -> p.Meltano.DbtConnectionProfile:
        """The dbt connection profile for LDAP-backed workflows.

        Returns:
            The resulting ``p.Meltano.DbtConnectionProfile``.

        """
        # NOTE (multi-agent): mro-rn88 — read INJECTED settings via self.settings
        # (runtime, not the global singleton); connection scalars from Ldap.*,
        # base_dn from DbtLdap.
        return m.DbtLdap.DbtConnectionProfile(
            host=self.settings.Ldap.host,
            port=self.settings.Ldap.port,
            use_tls=self.settings.Ldap.use_tls,
            base_dn=self.settings.DbtLdap.ldap_base_dn,
            project=self.dbt_project_name,
        )


s = FlextDbtLdapServiceBase

__all__: t.MutableSequenceOf[str] = ["FlextDbtLdapServiceBase", "s"]
