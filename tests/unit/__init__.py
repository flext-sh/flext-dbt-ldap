# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make codegen
#
"""Unit package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from tests.unit.test_dbt_services_sync import (
        test_sync_users_uses_incremental_bookmark_and_persists_state,
    )
    from tests.unit.test_version import (
        test_dunder_alignment,
        test_incremental_groups_sync_applies_bookmark_filter,
        test_incremental_users_sync_applies_bookmark_filter,
        test_version_metadata_integrity,
        test_version_properties,
    )

# Lazy import mapping: export_name -> (module_path, attr_name)
_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "test_dunder_alignment": ("tests.unit.test_version", "test_dunder_alignment"),
    "test_incremental_groups_sync_applies_bookmark_filter": (
        "tests.unit.test_version",
        "test_incremental_groups_sync_applies_bookmark_filter",
    ),
    "test_incremental_users_sync_applies_bookmark_filter": (
        "tests.unit.test_version",
        "test_incremental_users_sync_applies_bookmark_filter",
    ),
    "test_sync_users_uses_incremental_bookmark_and_persists_state": (
        "tests.unit.test_dbt_services_sync",
        "test_sync_users_uses_incremental_bookmark_and_persists_state",
    ),
    "test_version_metadata_integrity": (
        "tests.unit.test_version",
        "test_version_metadata_integrity",
    ),
    "test_version_properties": ("tests.unit.test_version", "test_version_properties"),
}

__all__ = [
    "test_dunder_alignment",
    "test_incremental_groups_sync_applies_bookmark_filter",
    "test_incremental_users_sync_applies_bookmark_filter",
    "test_sync_users_uses_incremental_bookmark_and_persists_state",
    "test_version_metadata_integrity",
    "test_version_properties",
]


def __getattr__(name: str) -> t.ModuleExport:
    """Lazy-load module attributes on first access (PEP 562)."""
    return lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete."""
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
