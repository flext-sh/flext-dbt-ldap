"""FLEXT DBT LDAP - Version information with Flextpatterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from importlib.metadata import metadata
from typing import Final

from flext_core import FlextResult


class FlextDbtLdapVersion:
    """Version information for flext-dbt-ldap package."""

    def __init__(self) -> None:
        """Initialize version from package metadata."""
        try:
            self._metadata = metadata("flext-dbt-ldap")
        except Exception:
            # Fallback for development/testing
            self._metadata = {
                "Version": "0.1.0",
                "Name": "flext-dbt-ldap",
                "Summary": "FLEXT DBT LDAP integration",
                "Author": "FLEXT Team",
                "Author-Email": "team@flext.dev",
                "License": "MIT",
                "Home-Page": "https://github.com/flext/flext-dbt-ldap",
            }

    @property
    def version(self) -> str:
        """Get version string."""
        return self._metadata.get("Version", "0.1.0")

    @property
    def version_info(self) -> tuple[int | str, ...]:
        """Get version info tuple."""
        version_str = self.version
        return tuple(
            int(part) if part.isdigit() else part for part in version_str.split(".")
        )

    @property
    def version_tuple(self) -> tuple[int | str, ...]:
        """Alias for version_info."""
        return self.version_info

    @property
    def author_name(self) -> str | None:
        """Get author name."""
        return self._metadata.get("Author")

    @property
    def maintainer_name(self) -> str | None:
        """Get maintainer name."""
        return self._metadata.get("Author")  # Same as author for now

    @property
    def description(self) -> str | None:
        """Get package description."""
        return self._metadata.get("Summary")

    @property
    def license(self) -> str | None:
        """Get package license."""
        return self._metadata.get("License")

    @property
    def url(self) -> str | None:
        """Get package URL."""
        return self._metadata.get("Home-Page")


def _create_version() -> FlextResult[FlextDbtLdapVersion]:
    """Create version instance from package metadata.

    Returns:
        FlextResult[FlextDbtLdapVersion]: Version instance or error

    """
    try:
        version = FlextDbtLdapVersion()
        return FlextResult[FlextDbtLdapVersion].ok(version)
    except Exception as e:
        return FlextResult[FlextDbtLdapVersion].fail(f"Version creation failed: {e}")


# Global version instance
_version_result = _create_version()
if _version_result.is_failure:
    error_msg = f"Failed to initialize version: {_version_result.error}"
    raise RuntimeError(error_msg)

VERSION: Final[FlextDbtLdapVersion] = _version_result.unwrap()

__all__ = [
    "VERSION",
    "FlextDbtLdapVersion",
]
