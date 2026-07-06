# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Ldap package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import (
    build_lazy_import_map,
    install_lazy_exports,
    merge_lazy_imports,
)
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

if TYPE_CHECKING:
    from flext_dbt_ldap.api import FlextDbtLdap as FlextDbtLdap, dbt_ldap as dbt_ldap
    from flext_dbt_ldap.base import (
        FlextDbtLdapServiceBase as FlextDbtLdapServiceBase,
        s as s,
    )
    from flext_dbt_ldap.constants import (
        FlextDbtLdapConstants as FlextDbtLdapConstants,
        c as c,
    )
    from flext_dbt_ldap.models import FlextDbtLdapModels as FlextDbtLdapModels, m as m
    from flext_dbt_ldap.protocols import (
        FlextDbtLdapProtocols as FlextDbtLdapProtocols,
        p as p,
    )
    from flext_dbt_ldap.services.client import (
        FlextDbtLdapClientMixin as FlextDbtLdapClientMixin,
    )
    from flext_dbt_ldap.services.sync import (
        FlextDbtLdapSyncMixin as FlextDbtLdapSyncMixin,
    )
    from flext_dbt_ldap.settings import FlextDbtLdapSettings as FlextDbtLdapSettings
    from flext_dbt_ldap.typings import FlextDbtLdapTypes as FlextDbtLdapTypes, t as t
    from flext_dbt_ldap.utilities import (
        FlextDbtLdapUtilities as FlextDbtLdapUtilities,
        u as u,
    )
    from flext_ldap import d as d, e as e, h as h, r as r, x as x
_LAZY_IMPORTS = merge_lazy_imports(
    (".services",),
    build_lazy_import_map(
        {
            ".api": (
                "FlextDbtLdap",
                "dbt_ldap",
            ),
            ".base": (
                "FlextDbtLdapServiceBase",
                "s",
            ),
            ".constants": (
                "FlextDbtLdapConstants",
                "c",
            ),
            ".models": (
                "FlextDbtLdapModels",
                "m",
            ),
            ".protocols": (
                "FlextDbtLdapProtocols",
                "p",
            ),
            ".services.client": ("FlextDbtLdapClientMixin",),
            ".services.sync": ("FlextDbtLdapSyncMixin",),
            ".settings": ("FlextDbtLdapSettings",),
            ".typings": (
                "FlextDbtLdapTypes",
                "t",
            ),
            ".utilities": (
                "FlextDbtLdapUtilities",
                "u",
            ),
            "flext_ldap": (
                "d",
                "e",
                "h",
                "r",
                "x",
            ),
        },
    ),
    exclude_names=(
        "cleanup_submodule_namespace",
        "install_lazy_exports",
        "lazy_getattr",
        "logger",
        "merge_lazy_imports",
        "output",
        "output_reporting",
        "pytest_addoption",
        "pytest_collect_file",
        "pytest_collection_modifyitems",
        "pytest_configure",
        "pytest_runtest_setup",
        "pytest_runtest_teardown",
        "pytest_sessionfinish",
        "pytest_sessionstart",
        "pytest_terminal_summary",
        "pytest_warning_recorded",
    ),
    module_name=__name__,
)


__all__: tuple[str, ...] = (
    "FlextDbtLdap",
    "FlextDbtLdapClientMixin",
    "FlextDbtLdapConstants",
    "FlextDbtLdapModels",
    "FlextDbtLdapProtocols",
    "FlextDbtLdapServiceBase",
    "FlextDbtLdapSettings",
    "FlextDbtLdapSyncMixin",
    "FlextDbtLdapTypes",
    "FlextDbtLdapUtilities",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "c",
    "d",
    "dbt_ldap",
    "e",
    "h",
    "m",
    "p",
    "r",
    "s",
    "t",
    "u",
    "x",
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    public_exports=__all__,
)
