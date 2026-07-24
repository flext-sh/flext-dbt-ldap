# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import (
    build_lazy_import_map,
    install_lazy_exports,
    merge_lazy_imports,
)

if TYPE_CHECKING:
    from flext_tests import (
        d as d,
        e as e,
        h as h,
        r as r,
        td as td,
        tf as tf,
        tk as tk,
        tm as tm,
        tv as tv,
        x as x,
    )

    from tests.base import (
        TestsFlextDbtLdapServiceBase as TestsFlextDbtLdapServiceBase,
        s as s,
    )
    from tests.constants import (
        TestsFlextDbtLdapConstants as TestsFlextDbtLdapConstants,
        c as c,
    )
    from tests.models import TestsFlextDbtLdapModels as TestsFlextDbtLdapModels, m as m
    from tests.protocols import (
        TestsFlextDbtLdapProtocols as TestsFlextDbtLdapProtocols,
        p as p,
    )
    from tests.settings import TestsFlextDbtLdapSettings as TestsFlextDbtLdapSettings
    from tests.typings import TestsFlextDbtLdapTypes as TestsFlextDbtLdapTypes, t as t
    from tests.unit.test_constants_flat_api import (
        TestsFlextDbtLdapConstantsFlatApi as TestsFlextDbtLdapConstantsFlatApi,
    )
    from tests.unit.test_dbt_services_sync import (
        TestsFlextDbtLdapServicesSync as TestsFlextDbtLdapServicesSync,
    )
    from tests.unit.test_version import (
        TestsFlextDbtLdapVersion as TestsFlextDbtLdapVersion,
    )
    from tests.utilities import (
        TestsFlextDbtLdapUtilities as TestsFlextDbtLdapUtilities,
        u as u,
    )
_LAZY_IMPORTS = merge_lazy_imports(
    (".e2e", ".unit"),
    build_lazy_import_map({
        ".base": ("TestsFlextDbtLdapServiceBase", "s"),
        ".conftest": ("conftest",),
        ".constants": ("TestsFlextDbtLdapConstants", "c"),
        ".e2e": ("e2e",),
        ".models": ("TestsFlextDbtLdapModels", "m"),
        ".protocols": ("TestsFlextDbtLdapProtocols", "p"),
        ".settings": ("TestsFlextDbtLdapSettings",),
        ".typings": ("TestsFlextDbtLdapTypes", "t"),
        ".unit": ("unit",),
        ".unit.test_constants_flat_api": ("TestsFlextDbtLdapConstantsFlatApi",),
        ".unit.test_dbt_services_sync": ("TestsFlextDbtLdapServicesSync",),
        ".unit.test_version": ("TestsFlextDbtLdapVersion",),
        ".utilities": ("TestsFlextDbtLdapUtilities", "u"),
        "flext_tests": ("d", "e", "h", "r", "td", "tf", "tk", "tm", "tv", "x"),
    }),
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


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, publish_all=False)
