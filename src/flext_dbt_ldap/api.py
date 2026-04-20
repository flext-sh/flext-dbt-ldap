"""FLEXT DBT LDAP — unified facade via MRO composition.

All service methods available directly on FlextDbtLdap via MRO.
No internal delegation, no factory wrappers.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import (
    Mapping,
)
from typing import override

from flext_dbt_ldap import (
    FlextDbtLdapSettings,
    FlextDbtLdapUtilitiesSync,
    p,
    r,
    t,
    u,
)
from flext_meltano import FlextMeltanoDbtServiceBase


class FlextDbtLdap(FlextDbtLdapUtilitiesSync):
    """Unified DBT LDAP facade — MRO-composed from service mixins.

    All extraction, transformation, sync, and validation methods
    are directly available via MRO. No wrappers, no delegation.
    """

    def __init__(self, settings: FlextDbtLdapSettings | None = None) -> None:
        """Wire all mixin state."""
        FlextMeltanoDbtServiceBase.__init__(self, settings=settings)
        object.__setattr__(self, "_ldap_api", self.create_ldap_api(self.settings))
        object.__setattr__(self, "transformer", u.DbtLdap())
        object.__setattr__(self, "_sync_state_file", self._resolve_sync_state_file())
        object.__setattr__(self, "_sync_bookmarks", self._load_sync_state())

    @override
    def execute(self) -> p.Result[Mapping[str, t.Container]]:
        """Execute DBT LDAP service — verify readiness."""
        return r[Mapping[str, t.Container]].ok(
            self.settings.model_dump(exclude_none=True)
        )


dbt_ldap = FlextDbtLdap

__all__: list[str] = ["FlextDbtLdap", "dbt_ldap"]
