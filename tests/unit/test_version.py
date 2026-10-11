"""Behavior contract for flext_dbt_ldap version metadata.

Copyright (c) 2026 FLEXT Team. All rights reserved.
tests/unit/test_version
SPDX-License-Identifier: MIT
"""

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
from tests import tm


class TestsFlextDbtLdapVersion:
    """Behavior contract for flext_dbt_ldap version metadata exports."""

    @staticmethod
    def test_version_string_is_non_empty_str() -> None:
        """Test version string is non empty str."""
        tm.that(__version__, is_=str)
        tm.that(__version__.strip(), ne="")

    @staticmethod
    def test_version_info_is_three_integer_release_tuple() -> None:
        """Test version info is three integer release tuple."""
        tm.that(__version_info__, is_=tuple)
        tm.that(len(__version_info__), eq=3)
        assert all(isinstance(part, int) for part in __version_info__)

    @staticmethod
    def test_version_string_and_tuple_are_aligned() -> None:
        """Test version string and tuple are aligned."""
        tm.that(__version_info__, eq=Version(__version__).release)

    @staticmethod
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
    def test_metadata_field_is_non_empty_str(field_value: str) -> None:
        """Test metadata field is non empty str."""
        tm.that(field_value, is_=str)
        tm.that(field_value.strip(), ne="")

    @staticmethod
    def test_title_identifies_this_distribution() -> None:
        """Test title identifies this distribution."""
        tm.that(__title__.lower(), contains="flext")

    @staticmethod
    def test_author_email_is_well_formed() -> None:
        """Test author email is well formed."""
        tm.that(__author_email__, contains="@")
