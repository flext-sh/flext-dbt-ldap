"""Compatibility alias for the stateful dbt-ldap client mixin."""

from __future__ import annotations

from flext_dbt_ldap.services.client import FlextDbtLdapClientMixin

FlextDbtLdapUtilitiesClient = FlextDbtLdapClientMixin

__all__: list[str] = ["FlextDbtLdapUtilitiesClient"]
