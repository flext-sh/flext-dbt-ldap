"""FLEXT Enterprise - dbt-ldap component."""

import importlib.metadata

try:
    __version__ = importlib.metadata.version("flext-dbt-ldap")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.0.0-dev"

__version_info__ = tuple(int(x) for x in __version__.split(".") if x.isdigit())

__all__ = ["__version__", "__version_info__"]
