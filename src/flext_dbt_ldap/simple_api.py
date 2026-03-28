"""Re-export shim — canonical implementation lives in _utilities.simple_api."""

from __future__ import annotations

from flext_dbt_ldap._utilities.simple_api import FlextDbtLdap

__all__ = ["FlextDbtLdap"]
