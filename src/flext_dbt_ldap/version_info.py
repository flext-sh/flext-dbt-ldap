"""FLEXT DBT LDAP - Version information and metadata.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import importlib.metadata

# ================================
# MODULE CONFIGURATION
# ================================

__version__ = importlib.metadata.version("flext-dbt-ldap")
__version_info__ = tuple(int(x) for x in __version__.split(".") if x.isdigit())


__all__ = [
    "__version__",
    "__version_info__",
]
