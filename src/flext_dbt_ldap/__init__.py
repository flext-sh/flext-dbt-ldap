# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Flext dbt ldap package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports, merge_lazy_imports
from flext_dbt_ldap.__version__ import (
    __all__,
    __author__,
    __author_email__,
    __description__,
    __license__,
    __title__,
    __url__,
    __version__,
    __version_info__,
)

if _TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
    from flext_dbt_ldap import (
        _utilities,
        base,
        client,
        constants,
        errors,
        integration,
        macros,
        models,
        protocols,
        settings,
        simple_api,
        sync,
        typings,
        utilities,
        version_info,
    )
    from flext_dbt_ldap._utilities import (
        FlextDbtLdapUtilitiesClient,
        FlextDbtLdapUtilitiesIntegration,
        FlextDbtLdapUtilitiesMacros,
        FlextDbtLdapUtilitiesSync,
    )
    from flext_dbt_ldap.base import FlextDbtLdapServiceBase
    from flext_dbt_ldap.constants import (
        FlextDbtLdapConstants,
        FlextDbtLdapConstants as c,
    )
    from flext_dbt_ldap.errors import FlextDbtLdapError
    from flext_dbt_ldap.models import (
        FlextDbtLdapModels,
        FlextDbtLdapModels as m,
        logger,
    )
    from flext_dbt_ldap.protocols import (
        FlextDbtLdapProtocols,
        FlextDbtLdapProtocols as p,
    )
    from flext_dbt_ldap.settings import FlextDbtLdapSettings
    from flext_dbt_ldap.simple_api import FlextDbtLdap
    from flext_dbt_ldap.typings import FlextDbtLdapTypes, FlextDbtLdapTypes as t
    from flext_dbt_ldap.utilities import (
        FlextDbtLdapUtilities,
        FlextDbtLdapUtilities as u,
    )
    from flext_dbt_ldap.version_info import __version__, __version_info__

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = merge_lazy_imports(
    ("flext_dbt_ldap._utilities",),
    {
        "FlextDbtLdap": "flext_dbt_ldap.simple_api",
        "FlextDbtLdapConstants": "flext_dbt_ldap.constants",
        "FlextDbtLdapError": "flext_dbt_ldap.errors",
        "FlextDbtLdapModels": "flext_dbt_ldap.models",
        "FlextDbtLdapProtocols": "flext_dbt_ldap.protocols",
        "FlextDbtLdapServiceBase": "flext_dbt_ldap.base",
        "FlextDbtLdapSettings": "flext_dbt_ldap.settings",
        "FlextDbtLdapTypes": "flext_dbt_ldap.typings",
        "FlextDbtLdapUtilities": "flext_dbt_ldap.utilities",
        "__version__": "flext_dbt_ldap.version_info",
        "__version_info__": "flext_dbt_ldap.version_info",
        "_utilities": "flext_dbt_ldap._utilities",
        "base": "flext_dbt_ldap.base",
        "c": ("flext_dbt_ldap.constants", "FlextDbtLdapConstants"),
        "client": "flext_dbt_ldap.client",
        "constants": "flext_dbt_ldap.constants",
        "d": ("flext_core.decorators", "FlextDecorators"),
        "e": ("flext_core.exceptions", "FlextExceptions"),
        "errors": "flext_dbt_ldap.errors",
        "h": ("flext_core.handlers", "FlextHandlers"),
        "integration": "flext_dbt_ldap.integration",
        "logger": "flext_dbt_ldap.models",
        "m": ("flext_dbt_ldap.models", "FlextDbtLdapModels"),
        "macros": "flext_dbt_ldap.macros",
        "models": "flext_dbt_ldap.models",
        "p": ("flext_dbt_ldap.protocols", "FlextDbtLdapProtocols"),
        "protocols": "flext_dbt_ldap.protocols",
        "r": ("flext_core.result", "FlextResult"),
        "s": ("flext_core.service", "FlextService"),
        "settings": "flext_dbt_ldap.settings",
        "simple_api": "flext_dbt_ldap.simple_api",
        "sync": "flext_dbt_ldap.sync",
        "t": ("flext_dbt_ldap.typings", "FlextDbtLdapTypes"),
        "typings": "flext_dbt_ldap.typings",
        "u": ("flext_dbt_ldap.utilities", "FlextDbtLdapUtilities"),
        "utilities": "flext_dbt_ldap.utilities",
        "version_info": "flext_dbt_ldap.version_info",
        "x": ("flext_core.mixins", "FlextMixins"),
    },
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    [
        "__all__",
        "__author__",
        "__author_email__",
        "__description__",
        "__license__",
        "__title__",
        "__url__",
    ],
)
