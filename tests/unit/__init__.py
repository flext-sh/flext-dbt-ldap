# AUTO-GENERATED FILE — Regenerate with: make gen
"""Unit package."""

from __future__ import annotations

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".test_constants_flat_api": ("TestsFlextDbtLdapConstantsFlatApi",),
        ".test_dbt_services_sync": ("TestsFlextDbtLdapServicesSync",),
        ".test_version": ("TestsFlextDbtLdapVersion",),
    },
)


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, publish_all=False)
