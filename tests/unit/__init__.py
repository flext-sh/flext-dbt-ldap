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
    from flext_dbt_ldap import test_dbt_services_sync, test_version
    from flext_dbt_ldap.test_dbt_services_sync import (
        call_kwargs,
        mock_pipeline,
        persisted,
        result,
        return_value,
        service,
        state_file,
        test_sync_users_uses_incremental_bookmark_and_persists_state,
    )
    from flext_dbt_ldap.test_version import test_dunder_alignment

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = {
    "c": ("flext_core.constants", "FlextConstants"),
    "call_kwargs": "flext_dbt_ldap.test_dbt_services_sync",
    "d": ("flext_core.decorators", "FlextDecorators"),
    "e": ("flext_core.exceptions", "FlextExceptions"),
    "h": ("flext_core.handlers", "FlextHandlers"),
    "m": ("flext_core.models", "FlextModels"),
    "mock_pipeline": "flext_dbt_ldap.test_dbt_services_sync",
    "p": ("flext_core.protocols", "FlextProtocols"),
    "persisted": "flext_dbt_ldap.test_dbt_services_sync",
    "r": ("flext_core.result", "FlextResult"),
    "result": "flext_dbt_ldap.test_dbt_services_sync",
    "return_value": "flext_dbt_ldap.test_dbt_services_sync",
    "s": ("flext_core.service", "FlextService"),
    "service": "flext_dbt_ldap.test_dbt_services_sync",
    "state_file": "flext_dbt_ldap.test_dbt_services_sync",
    "t": ("flext_core.typings", "FlextTypes"),
    "test_dbt_services_sync": "flext_dbt_ldap.test_dbt_services_sync",
    "test_dunder_alignment": "flext_dbt_ldap.test_version",
    "test_sync_users_uses_incremental_bookmark_and_persists_state": "flext_dbt_ldap.test_dbt_services_sync",
    "test_version": "flext_dbt_ldap.test_version",
    "u": ("flext_core.utilities", "FlextUtilities"),
    "x": ("flext_core.mixins", "FlextMixins"),
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
