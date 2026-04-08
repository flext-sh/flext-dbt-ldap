# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports

if _t.TYPE_CHECKING:
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
    from tests.constants import (
        TestsFlextDbtLdapConstants,
        TestsFlextDbtLdapConstants as c,
    )
    from tests.models import TestsFlextDbtLdapModels, TestsFlextDbtLdapModels as m
    from tests.protocols import (
        TestsFlextDbtLdapProtocols,
        TestsFlextDbtLdapProtocols as p,
    )
    from tests.typings import TestsFlextDbtLdapTypes, TestsFlextDbtLdapTypes as t
    from tests.utilities import (
        TestsFlextDbtLdapUtilities,
        TestsFlextDbtLdapUtilities as u,
    )
_LAZY_IMPORTS = {
    "TestsFlextDbtLdapConstants": ".constants",
    "TestsFlextDbtLdapModels": ".models",
    "TestsFlextDbtLdapProtocols": ".protocols",
    "TestsFlextDbtLdapTypes": ".typings",
    "TestsFlextDbtLdapUtilities": ".utilities",
    "c": (".constants", "TestsFlextDbtLdapConstants"),
    "d": ("flext_core.decorators", "FlextDecorators"),
    "e": ("flext_core.exceptions", "FlextExceptions"),
    "h": ("flext_core.handlers", "FlextHandlers"),
    "m": (".models", "TestsFlextDbtLdapModels"),
    "p": (".protocols", "TestsFlextDbtLdapProtocols"),
    "r": ("flext_core.result", "FlextResult"),
    "s": ("flext_core.service", "FlextService"),
    "t": (".typings", "TestsFlextDbtLdapTypes"),
    "u": (".utilities", "TestsFlextDbtLdapUtilities"),
    "x": ("flext_core.mixins", "FlextMixins"),
}

__all__ = [
    "TestsFlextDbtLdapConstants",
    "TestsFlextDbtLdapModels",
    "TestsFlextDbtLdapProtocols",
    "TestsFlextDbtLdapTypes",
    "TestsFlextDbtLdapUtilities",
    "c",
    "d",
    "e",
    "h",
    "m",
    "p",
    "r",
    "s",
    "t",
    "u",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
