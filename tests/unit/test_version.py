"""Version metadata tests for flext-dbt-ldap."""

from __future__ import annotations

from collections.abc import Mapping

from flext_core.metadata import FlextProjectMetadata, FlextProjectPerson

from flext_dbt_ldap import __version__, __version_info__
from flext_dbt_ldap.version import VERSION, FlextDbtLdapVersion


def test_dunder_alignment() -> None:
    """Ensure dunder exports come from VERSION."""
    assert __version__ == VERSION.version
    assert __version_info__ == VERSION.version_info


def test_version_metadata_integrity() -> None:
    """VERSION should expose normalized metadata."""
    assert isinstance(VERSION, FlextDbtLdapVersion)
    assert isinstance(VERSION.metadata, FlextProjectMetadata)
    assert isinstance(VERSION.urls, Mapping)
    assert VERSION.version_tuple == VERSION.version_info


def test_contacts() -> None:
    """Primary author and maintainer info is accessible."""
    assert isinstance(VERSION.author, FlextProjectPerson)
    assert isinstance(VERSION.maintainer, FlextProjectPerson)
    assert VERSION.author_name
    assert VERSION.maintainer_name


def test_metadata_passthrough() -> None:
    """Author and maintainer collections mirror metadata."""
    assert VERSION.authors == VERSION.metadata.authors
    assert VERSION.maintainers == VERSION.metadata.maintainers
