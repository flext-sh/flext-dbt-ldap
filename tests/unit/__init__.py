# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Unit package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports

if _t.TYPE_CHECKING:
    import tests.unit.test_constants_flat_api as _tests_unit_test_constants_flat_api

    test_constants_flat_api = _tests_unit_test_constants_flat_api
    import tests.unit.test_dbt_services_sync as _tests_unit_test_dbt_services_sync
    from tests.unit.test_constants_flat_api import (
        test_dbt_ldap_constants_surface_is_flat,
        test_user_dimension_from_ldap_entry_uses_flat_constants_surface,
    )

    test_dbt_services_sync = _tests_unit_test_dbt_services_sync
    import tests.unit.test_version as _tests_unit_test_version
    from tests.unit.test_dbt_services_sync import (
        test_run_dbt_models_propagates_run_models_failure,
        test_sync_groups_uses_incremental_bookmark_and_persists_state,
        test_sync_users_uses_incremental_bookmark_and_persists_state,
    )

    test_version = _tests_unit_test_version
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
    from tests.unit.test_version import (
        test_dunder_alignment,
        test_version_metadata_integrity,
        test_version_properties,
    )
_LAZY_IMPORTS = {
    "c": ("flext_core.constants", "FlextConstants"),
    "d": ("flext_core.decorators", "FlextDecorators"),
    "e": ("flext_core.exceptions", "FlextExceptions"),
    "h": ("flext_core.handlers", "FlextHandlers"),
    "m": ("flext_core.models", "FlextModels"),
    "p": ("flext_core.protocols", "FlextProtocols"),
    "r": ("flext_core.result", "FlextResult"),
    "s": ("flext_core.service", "FlextService"),
    "t": ("flext_core.typings", "FlextTypes"),
    "test_constants_flat_api": "tests.unit.test_constants_flat_api",
    "test_dbt_ldap_constants_surface_is_flat": (
        "tests.unit.test_constants_flat_api",
        "test_dbt_ldap_constants_surface_is_flat",
    ),
    "test_dbt_services_sync": "tests.unit.test_dbt_services_sync",
    "test_dunder_alignment": ("tests.unit.test_version", "test_dunder_alignment"),
    "test_run_dbt_models_propagates_run_models_failure": (
        "tests.unit.test_dbt_services_sync",
        "test_run_dbt_models_propagates_run_models_failure",
    ),
    "test_sync_groups_uses_incremental_bookmark_and_persists_state": (
        "tests.unit.test_dbt_services_sync",
        "test_sync_groups_uses_incremental_bookmark_and_persists_state",
    ),
    "test_sync_users_uses_incremental_bookmark_and_persists_state": (
        "tests.unit.test_dbt_services_sync",
        "test_sync_users_uses_incremental_bookmark_and_persists_state",
    ),
    "test_user_dimension_from_ldap_entry_uses_flat_constants_surface": (
        "tests.unit.test_constants_flat_api",
        "test_user_dimension_from_ldap_entry_uses_flat_constants_surface",
    ),
    "test_version": "tests.unit.test_version",
    "test_version_metadata_integrity": (
        "tests.unit.test_version",
        "test_version_metadata_integrity",
    ),
    "test_version_properties": ("tests.unit.test_version", "test_version_properties"),
    "u": ("flext_core.utilities", "FlextUtilities"),
    "x": ("flext_core.mixins", "FlextMixins"),
}

__all__ = [
    "c",
    "d",
    "e",
    "h",
    "m",
    "p",
    "r",
    "s",
    "t",
    "test_constants_flat_api",
    "test_dbt_ldap_constants_surface_is_flat",
    "test_dbt_services_sync",
    "test_dunder_alignment",
    "test_run_dbt_models_propagates_run_models_failure",
    "test_sync_groups_uses_incremental_bookmark_and_persists_state",
    "test_sync_users_uses_incremental_bookmark_and_persists_state",
    "test_user_dimension_from_ldap_entry_uses_flat_constants_surface",
    "test_version",
    "test_version_metadata_integrity",
    "test_version_properties",
    "u",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
