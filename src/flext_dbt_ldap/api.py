"""FLEXT DBT LDAP — unified facade via MRO composition.

All service methods available directly on FlextDbtLdap via MRO.
No internal delegation, no factory wrappers.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import override

from flext_dbt_ldap import (
    FlextDbtLdapSettings,
    p,
    r,
    settings,
    t,
    u,
)
from flext_dbt_ldap.services.sync import FlextDbtLdapSyncMixin
from flext_meltano import FlextMeltanoDbtServiceBase


class FlextDbtLdap(FlextDbtLdapSyncMixin):
    """Unified DBT LDAP facade — MRO-composed from service mixins.

    All extraction, transformation, sync, and validation methods
    are directly available via MRO. No wrappers, no delegation.
    """

    def __init__(self, settings: FlextDbtLdapSettings | None = None) -> None:
        """Wire all mixin state."""
        # NOTE (multi-agent): mro-rn88 — resolve to the global settings singleton when no
        # override is supplied so create_ldap_api always receives a concrete settings.
        effective_settings = settings or FlextDbtLdapSettings.fetch_global()
        FlextMeltanoDbtServiceBase.__init__(self, settings=effective_settings)
        object.__setattr__(self, "_ldap_api", self.create_ldap_api(effective_settings))
        object.__setattr__(self, "transformer", u.DbtLdap())
        object.__setattr__(self, "_sync_state_file", self._resolve_sync_state_file())
        object.__setattr__(self, "_sync_bookmarks", self._load_sync_state())

    @override
    def execute(self) -> p.Result[t.JsonMapping]:
        """Execute DBT LDAP service — verify readiness."""
        return r[t.JsonMapping].ok(settings.model_dump(exclude_none=True))


dbt_ldap = FlextDbtLdap

__all__: list[str] = ["FlextDbtLdap", "dbt_ldap"]
