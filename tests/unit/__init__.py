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
    from flext_core.constants import FlextConstants as c
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.models import FlextModels as m
    from flext_core.protocols import FlextProtocols as p
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
    from flext_core.typings import FlextTypes as t
    from flext_core.utilities import FlextUtilities as u
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
    "c": ("flext_core.constants", "FlextConstants"),
    "d": ("flext_core.decorators", "FlextDecorators"),
    "e": ("flext_core.exceptions", "FlextExceptions"),
    "h": ("flext_core.handlers", "FlextHandlers"),
    "m": ("flext_core.models", "FlextModels"),
    "p": ("flext_core.protocols", "FlextProtocols"),
    "r": ("flext_core.result", "FlextResult"),
    "s": ("flext_core.service", "FlextService"),
    "t": ("flext_core.typings", "FlextTypes"),
    "test_dbt_services_sync": "tests.unit.test_dbt_services_sync",
    "test_dunder_alignment": "tests.unit.test_version",
    "test_incremental_groups_sync_applies_bookmark_filter": "tests.unit.test_version",
    "test_incremental_users_sync_applies_bookmark_filter": "tests.unit.test_version",
    "test_sync_users_uses_incremental_bookmark_and_persists_state": "tests.unit.test_dbt_services_sync",
    "test_version": "tests.unit.test_version",
    "test_version_metadata_integrity": "tests.unit.test_version",
    "test_version_properties": "tests.unit.test_version",
    "u": ("flext_core.utilities", "FlextUtilities"),
    "x": ("flext_core.mixins", "FlextMixins"),
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
