"""Version metadata tests for flext-dbt-ldap."""

from __future__ import annotations

from flext_dbt_ldap import (
    __author__,
    __author_email__,
    __description__,
    __license__,
    __title__,
    __url__,
    __version__,
    __version_info__,
)


def test_dunder_alignment() -> None:
    """Ensure version exports are consistent."""
    assert isinstance(__version__, str)
    assert isinstance(__version_info__, tuple)
    assert (
        tuple(int(part) if part.isdigit() else part for part in __version__.split("."))
        == __version_info__
    )


def test_version_metadata_integrity() -> None:
    """Metadata exports should be strings or None (when missing from package metadata)."""
    assert isinstance(__title__, str)
    assert isinstance(__description__, str)
    assert isinstance(__author_email__, str)
    assert isinstance(__license__, str)
    # __author__ and __url__ may be None/empty depending on package metadata availability
    assert __author__ is None or isinstance(__author__, str)
    assert isinstance(__url__, str)


def test_version_properties() -> None:
    """Version fields should not be empty when package metadata is available."""
    assert __version__.strip() != ""
    assert len(__version_info__) >= 1
