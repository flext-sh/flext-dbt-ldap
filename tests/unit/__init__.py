# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Unit package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from tests.unit import test_dbt_services_sync, test_version
    from tests.unit.test_dbt_services_sync import *
    from tests.unit.test_version import *

_LAZY_IMPORTS: Mapping[str, str | Sequence[str]] = {
    "test_dbt_services_sync": "tests.unit.test_dbt_services_sync",
    "test_dunder_alignment": "tests.unit.test_version",
    "test_incremental_groups_sync_applies_bookmark_filter": "tests.unit.test_version",
    "test_incremental_users_sync_applies_bookmark_filter": "tests.unit.test_version",
    "test_sync_users_uses_incremental_bookmark_and_persists_state": "tests.unit.test_dbt_services_sync",
    "test_version": "tests.unit.test_version",
    "test_version_metadata_integrity": "tests.unit.test_version",
    "test_version_properties": "tests.unit.test_version",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, sorted(_LAZY_IMPORTS))
