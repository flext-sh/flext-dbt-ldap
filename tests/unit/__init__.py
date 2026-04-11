# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Ldap package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if _t.TYPE_CHECKING:
    from flext_dbt_ldap.test_constants_flat_api import (
        test_dbt_ldap_constants_surface_is_flat,
        test_user_dimension_from_ldap_entry_uses_flat_constants_surface,
    )
    from flext_dbt_ldap.test_dbt_services_sync import (
        test_run_dbt_models_propagates_run_models_failure,
        test_service_init_fails_fast_when_sync_state_is_invalid,
        test_sync_groups_uses_incremental_bookmark_and_persists_state,
        test_sync_users_fails_when_sync_state_persistence_fails,
        test_sync_users_uses_incremental_bookmark_and_persists_state,
    )
    from flext_dbt_ldap.test_version import (
        test_dunder_alignment,
        test_version_metadata_integrity,
        test_version_properties,
    )
_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".test_constants_flat_api": (
            "test_dbt_ldap_constants_surface_is_flat",
            "test_user_dimension_from_ldap_entry_uses_flat_constants_surface",
        ),
        ".test_dbt_services_sync": (
            "test_run_dbt_models_propagates_run_models_failure",
            "test_service_init_fails_fast_when_sync_state_is_invalid",
            "test_sync_groups_uses_incremental_bookmark_and_persists_state",
            "test_sync_users_fails_when_sync_state_persistence_fails",
            "test_sync_users_uses_incremental_bookmark_and_persists_state",
        ),
        ".test_version": (
            "test_dunder_alignment",
            "test_version_metadata_integrity",
            "test_version_properties",
        ),
    },
)


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)

__all__ = [
    "test_dbt_ldap_constants_surface_is_flat",
    "test_dunder_alignment",
    "test_run_dbt_models_propagates_run_models_failure",
    "test_service_init_fails_fast_when_sync_state_is_invalid",
    "test_sync_groups_uses_incremental_bookmark_and_persists_state",
    "test_sync_users_fails_when_sync_state_persistence_fails",
    "test_sync_users_uses_incremental_bookmark_and_persists_state",
    "test_user_dimension_from_ldap_entry_uses_flat_constants_surface",
    "test_version_metadata_integrity",
    "test_version_properties",
]
