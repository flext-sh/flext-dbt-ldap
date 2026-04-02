# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Unit package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if _TYPE_CHECKING:
    from flext_core import FlextTypes
    from tests.unit import test_dbt_services_sync, test_version
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

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = {
    "test_dbt_services_sync": "tests.unit.test_dbt_services_sync",
    "test_dunder_alignment": "tests.unit.test_version",
    "test_incremental_groups_sync_applies_bookmark_filter": "tests.unit.test_version",
    "test_incremental_users_sync_applies_bookmark_filter": "tests.unit.test_version",
    "test_sync_users_uses_incremental_bookmark_and_persists_state": "tests.unit.test_dbt_services_sync",
    "test_version": "tests.unit.test_version",
    "test_version_metadata_integrity": "tests.unit.test_version",
    "test_version_properties": "tests.unit.test_version",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
