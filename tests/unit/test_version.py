"""Version metadata tests for flext-dbt-ldap."""

from __future__ import annotations

from flext_dbt_ldap import __version__, __version_info__
from flext_dbt_ldap.version import VERSION, FlextDbtLdapVersion


def test_dunder_alignment() -> None:
    """Ensure dunder exports come from VERSION."""
    assert __version__ == VERSION.version
    assert __version_info__ == VERSION.version_info


def test_version_metadata_integrity() -> None:
    """VERSION should expose normalized metadata."""
    assert isinstance(VERSION, FlextDbtLdapVersion)
    assert VERSION.version_tuple == VERSION.version_info


def test_version_properties() -> None:
    """Version properties should be accessible."""
    assert isinstance(VERSION.version, str)
    assert isinstance(VERSION.version_info, tuple)
    assert isinstance(VERSION.version_tuple, tuple)
    assert VERSION.author_name is None or isinstance(VERSION.author_name, str)
    assert VERSION.maintainer_name is None or isinstance(VERSION.maintainer_name, str)
    assert VERSION.description is None or isinstance(VERSION.description, str)
    assert VERSION.license is None or isinstance(VERSION.license, str)
    assert VERSION.url is None or isinstance(VERSION.url, str)
