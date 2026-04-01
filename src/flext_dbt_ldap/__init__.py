# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""FLEXT DBT LDAP - Enterprise LDAP integration for DBT workflows.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports, merge_lazy_imports

from flext_dbt_ldap.__version__ import (
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
    from flext_ldap import d, e, h, r, s, x

    from flext_dbt_ldap._utilities import *
    from flext_dbt_ldap.constants import *
    from flext_dbt_ldap.errors import *
    from flext_dbt_ldap.models import *
    from flext_dbt_ldap.protocols import *
    from flext_dbt_ldap.settings import *
    from flext_dbt_ldap.simple_api import *
    from flext_dbt_ldap.typings import *
    from flext_dbt_ldap.utilities import *
    from flext_dbt_ldap.version_info import *

_LAZY_IMPORTS: Mapping[str, str | Sequence[str]] = merge_lazy_imports(
    ("flext_dbt_ldap._utilities",),
    {
        "FlextDbtLdap": "flext_dbt_ldap.simple_api",
        "FlextDbtLdapAuthenticationError": "flext_dbt_ldap.errors",
        "FlextDbtLdapConfigurationError": "flext_dbt_ldap.errors",
        "FlextDbtLdapConnectionError": "flext_dbt_ldap.errors",
        "FlextDbtLdapConstants": "flext_dbt_ldap.constants",
        "FlextDbtLdapError": "flext_dbt_ldap.errors",
        "FlextDbtLdapMacroError": "flext_dbt_ldap.errors",
        "FlextDbtLdapModelError": "flext_dbt_ldap.errors",
        "FlextDbtLdapModels": "flext_dbt_ldap.models",
        "FlextDbtLdapProcessingError": "flext_dbt_ldap.errors",
        "FlextDbtLdapProtocols": "flext_dbt_ldap.protocols",
        "FlextDbtLdapSettings": "flext_dbt_ldap.settings",
        "FlextDbtLdapTestError": "flext_dbt_ldap.errors",
        "FlextDbtLdapTimeoutError": "flext_dbt_ldap.errors",
        "FlextDbtLdapTypes": "flext_dbt_ldap.typings",
        "FlextDbtLdapUtilities": "flext_dbt_ldap.utilities",
        "FlextDbtLdapValidationError": "flext_dbt_ldap.errors",
        "__version__": "flext_dbt_ldap.version_info",
        "__version_info__": "flext_dbt_ldap.version_info",
        "_utilities": "flext_dbt_ldap._utilities",
        "c": ("flext_dbt_ldap.constants", "FlextDbtLdapConstants"),
        "constants": "flext_dbt_ldap.constants",
        "d": "flext_ldap",
        "e": "flext_ldap",
        "errors": "flext_dbt_ldap.errors",
        "h": "flext_ldap",
        "logger": "flext_dbt_ldap.settings",
        "m": ("flext_dbt_ldap.models", "FlextDbtLdapModels"),
        "models": "flext_dbt_ldap.models",
        "p": ("flext_dbt_ldap.protocols", "FlextDbtLdapProtocols"),
        "protocols": "flext_dbt_ldap.protocols",
        "r": "flext_ldap",
        "s": "flext_ldap",
        "settings": "flext_dbt_ldap.settings",
        "simple_api": "flext_dbt_ldap.simple_api",
        "t": ("flext_dbt_ldap.typings", "FlextDbtLdapTypes"),
        "typings": "flext_dbt_ldap.typings",
        "u": ("flext_dbt_ldap.utilities", "FlextDbtLdapUtilities"),
        "utilities": "flext_dbt_ldap.utilities",
        "version_info": "flext_dbt_ldap.version_info",
        "x": "flext_ldap",
    },
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    [
        "__author__",
        "__author_email__",
        "__description__",
        "__license__",
        "__title__",
        "__url__",
    ],
)
