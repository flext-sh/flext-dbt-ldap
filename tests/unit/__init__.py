# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Unit package."""

from __future__ import annotations

from collections.abc import Mapping, MutableMapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core import FlextTypes

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

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "test_dunder_alignment": ["tests.unit.test_version", "test_dunder_alignment"],
    "test_incremental_groups_sync_applies_bookmark_filter": [
        "tests.unit.test_version",
        "test_incremental_groups_sync_applies_bookmark_filter",
    ],
    "test_incremental_users_sync_applies_bookmark_filter": [
        "tests.unit.test_version",
        "test_incremental_users_sync_applies_bookmark_filter",
    ],
    "test_sync_users_uses_incremental_bookmark_and_persists_state": [
        "tests.unit.test_dbt_services_sync",
        "test_sync_users_uses_incremental_bookmark_and_persists_state",
    ],
    "test_version_metadata_integrity": [
        "tests.unit.test_version",
        "test_version_metadata_integrity",
    ],
    "test_version_properties": ["tests.unit.test_version", "test_version_properties"],
}

__all__ = [
    "test_dunder_alignment",
    "test_incremental_groups_sync_applies_bookmark_filter",
    "test_incremental_users_sync_applies_bookmark_filter",
    "test_sync_users_uses_incremental_bookmark_and_persists_state",
    "test_version_metadata_integrity",
    "test_version_properties",
]


_LAZY_CACHE: MutableMapping[str, FlextTypes.ModuleExport] = {}


def __getattr__(name: str) -> FlextTypes.ModuleExport:
    """Lazy-load module attributes on first access (PEP 562).

    A local cache ``_LAZY_CACHE`` persists resolved objects across repeated
    accesses during process lifetime.

    Args:
        name: Attribute name requested by dir()/import.

    Returns:
        Lazy-loaded module export type.

    Raises:
        AttributeError: If attribute not registered.

    """
    if name in _LAZY_CACHE:
        return _LAZY_CACHE[name]

    value = lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)
    _LAZY_CACHE[name] = value
    return value


def __dir__() -> Sequence[str]:
    """Return list of available attributes for dir() and autocomplete.

    Returns:
        List of public names from module exports.

    """
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
