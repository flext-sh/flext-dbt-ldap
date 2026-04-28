"""Compatibility alias for the stateful dbt-ldap sync mixin."""

from __future__ import annotations

from flext_dbt_ldap.services.sync import FlextDbtLdapSyncMixin

FlextDbtLdapUtilitiesSync = FlextDbtLdapSyncMixin

__all__: list[str] = ["FlextDbtLdapUtilitiesSync"]
