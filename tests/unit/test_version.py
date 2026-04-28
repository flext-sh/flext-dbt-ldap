"""Behavior contract for flext_dbt_ldap version metadata."""

from __future__ import annotations

from flext_tests import tm

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


class TestsFlextDbtLdapVersion:
    """Behavior contract for flext_dbt_ldap version metadata exports."""

    def test_version_string_and_tuple_are_aligned(self) -> None:
        tm.that(__version__, is_=str)
        tm.that(__version_info__, is_=tuple)
        parts = tuple(
            int(part) if part.isdigit() else part for part in __version__.split(".")
        )
        tm.that(parts, eq=__version_info__)

    def test_metadata_exports_have_expected_types(self) -> None:
        tm.that(__title__, is_=str)
        tm.that(__description__, is_=str)
        tm.that(__author_email__, is_=str)
        tm.that(__license__, is_=str)
        tm.that(__author__, is_=str)
        tm.that(__url__, is_=str)

    def test_version_fields_are_non_empty(self) -> None:
        tm.that(__version__.strip(), ne="")
        tm.that(len(__version_info__), gte=1)
