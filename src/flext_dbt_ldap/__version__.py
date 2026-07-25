# AUTO-GENERATED FILE — Regenerate with: make gen
"""Package version and metadata for flext-dbt-ldap.

Subclass of ``FlextVersion`` — overrides only ``_metadata``.
All derived attributes (``__version__``, ``__title__``, etc.) are
computed automatically via ``FlextVersion.__init_subclass__``.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from importlib.metadata import PackageMetadata, metadata

from flext_core.__version__ import FlextVersion


class FlextDbtLdapVersion(FlextVersion):
    """flext-dbt-ldap version — MRO-derived from FlextVersion."""

    _metadata: PackageMetadata = metadata("flext-dbt-ldap")


__version__ = FlextDbtLdapVersion.__version__
__version_info__ = FlextDbtLdapVersion.__version_info__
__title__ = FlextDbtLdapVersion.__title__
__description__ = FlextDbtLdapVersion.__description__
__author__ = FlextDbtLdapVersion.__author__
__author_email__ = FlextDbtLdapVersion.__author_email__
__license__ = FlextDbtLdapVersion.__license__
__url__ = FlextDbtLdapVersion.__url__
__all__: list[str] = [
    "FlextDbtLdapVersion",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
]
