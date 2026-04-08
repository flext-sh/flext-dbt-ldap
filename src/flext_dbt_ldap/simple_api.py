"""FLEXT DBT LDAP — unified facade via MRO composition.

All service methods available directly on FlextDbtLdap via MRO.
No internal delegation, no factory wrappers.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import override

from flext_core import r
from flext_dbt_ldap import (
    FlextDbtLdapSettings,
    FlextDbtLdapUtilitiesSync,
    m,
    t,
)


class FlextDbtLdap(FlextDbtLdapUtilitiesSync):
    """Unified DBT LDAP facade — MRO-composed from service mixins.

    All extraction, transformation, sync, and validation methods
    are directly available via MRO. No wrappers, no delegation.
    """

    def __init__(self, config: FlextDbtLdapSettings | None = None) -> None:
        """Wire all mixin state."""
        super().__init__(
            config_overrides=(
                config.model_dump(exclude_none=True) if config is not None else None
            ),
            config_type=FlextDbtLdapSettings,
        )
        object.__setattr__(self, "_ldap_api", self.create_ldap_api(self.config))
        object.__setattr__(self, "transformer", m.DbtLdap())
        object.__setattr__(self, "_sync_state_file", self._resolve_sync_state_file())
        object.__setattr__(self, "_sync_bookmarks", self._load_sync_state())

    @override
    def execute(self) -> r[t.ContainerMapping]:
        """Execute DBT LDAP service — verify readiness."""
        return r[t.ContainerMapping].ok(self.config.model_dump(exclude_none=True))


__all__ = ["FlextDbtLdap"]
