# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Unit package."""

from __future__ import annotations

from flext_core.lazy import install_lazy_exports

_LAZY_IMPORTS = {
    "test_constants_flat_api": "tests.unit.test_constants_flat_api",
    "test_dbt_services_sync": "tests.unit.test_dbt_services_sync",
    "test_version": "tests.unit.test_version",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, publish_all=False)
