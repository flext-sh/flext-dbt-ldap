"""FLEXT DBT LDAP — unified facade via MRO composition.

All service methods available directly on FlextDbtLdap via MRO.
No internal delegation, no factory wrappers.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import override

from flext_core import FlextService, r

from flext_dbt_ldap import m
from flext_dbt_ldap._utilities.sync import FlextDbtLdapUtilitiesSync
from flext_dbt_ldap.settings import FlextDbtLdapSettings


class FlextDbtLdap(
    FlextDbtLdapUtilitiesSync,
    FlextService[FlextDbtLdapSettings],
):
    """Unified DBT LDAP facade — MRO-composed from service mixins.

    All extraction, transformation, sync, and validation methods
    are directly available via MRO. No wrappers, no delegation.
    """

    def __init__(self, config: FlextDbtLdapSettings | None = None) -> None:
        """Wire all mixin state."""
        self._dbt_ldap_config: FlextDbtLdapSettings = (
            config if config is not None else FlextDbtLdapSettings.model_validate({})
        )
        self._config = self._dbt_ldap_config
        super().__init__()
        self._ldap_api = self.create_ldap_api(self.config)
        self._dbt_manager = None
        # Sync mixin state
        self.transformer = m.DbtLdap()
        self._sync_state_file = self._resolve_sync_state_file()
        self._sync_bookmarks = self._load_sync_state()

    @property
    @override
    def config(self) -> FlextDbtLdapSettings:
        """Get the current configuration."""
        return self._dbt_ldap_config

    @classmethod
    def create(cls) -> FlextDbtLdap:
        """Factory method."""
        return cls()

    @override
    def execute(self) -> r[FlextDbtLdapSettings]:
        """Execute DBT LDAP service — verify readiness."""
        return r[FlextDbtLdapSettings].ok(self.config)


__all__ = ["FlextDbtLdap"]
