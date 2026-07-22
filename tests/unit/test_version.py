"""Behavior contract for flext_dbt_ldap version metadata."""

from __future__ import annotations

import pytest
from packaging.version import Version

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
from flext_tests import tm

__all__: list[str] = ["TestsFlextDbtLdapVersion"]


class TestsFlextDbtLdapVersion:
    """Behavior contract for flext_dbt_ldap version metadata exports."""

    def test_version_string_is_non_empty_str(self) -> None:
        tm.that(__version__, is_=str)
        tm.that(__version__.strip(), ne="")

    def test_version_info_is_three_integer_release_tuple(self) -> None:
        tm.that(__version_info__, is_=tuple)
        tm.that(len(__version_info__), eq=3)
        assert all(isinstance(part, int) for part in __version_info__)

    def test_version_string_and_tuple_are_aligned(self) -> None:
        tm.that(__version_info__, eq=Version(__version__).release)

    @pytest.mark.parametrize(
        "field_value",
        [
            __title__,
            __description__,
            __author__,
            __author_email__,
            __license__,
            __url__,
        ],
    )
    def test_metadata_field_is_non_empty_str(self, field_value: str) -> None:
        tm.that(field_value, is_=str)
        tm.that(field_value.strip(), ne="")

    def test_title_identifies_this_distribution(self) -> None:
        tm.that(__title__.lower(), contains="flext")

    def test_author_email_is_well_formed(self) -> None:
        tm.that(__author_email__, contains="@")
