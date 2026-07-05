"""Behavior contract for the flattened DbtLdap constants and UserDimension APIs.

Every assertion here exercises an OBSERVABLE public contract: the flat constant
surface exposed by ``c.DbtLdap`` and the public model behaviour of
``m.DbtLdap.UserDimension`` (fields, ``from_ldap_entry`` mapping, validation, and
``to_dbt_dict`` serialization). No private attribute, internal collaborator, or
implementation-layout detail is touched.
"""

from __future__ import annotations

import pytest
from flext_tests import tm
from pydantic import ValidationError

from tests.constants import c
from tests.models import m

type LdifEntry = m.Ldif.Entry


class TestsFlextDbtLdapConstantsFlatApi:
    """Behavior contract for c.DbtLdap flat surface and UserDimension integration."""

    # --- Flat constants surface (public contract) --------------------------

    @pytest.mark.parametrize(
        ("actual", "expected"),
        [
            (c.DbtLdap.CN, c.Ldap.AttributeName.COMMON_NAME),
            (c.DbtLdap.UID, "uid"),
            (c.DbtLdap.MAIL, "mail"),
            (c.DbtLdap.DISPLAY_NAME, "displayName"),
            (c.DbtLdap.DEPARTMENT, "department"),
            (c.DbtLdap.EMPLOYEE_NUMBER, "employeeNumber"),
            (c.DbtLdap.TELEPHONE_NUMBER, "telephoneNumber"),
            (c.DbtLdap.FILTER_USER, "(objectClass=person)"),
            (c.DbtLdap.FILTER_GROUP, "(objectClass=group)"),
            (c.DbtLdap.STG_USERS, "stg_users"),
            (c.DbtLdap.DIM_USERS, "dim_users"),
            (c.DbtLdap.DEFAULT_BATCH_SIZE, c.DEFAULT_SIZE),
            (c.DbtLdap.MAX_BATCH_SIZE, c.MAX_ITEMS),
        ],
    )
    def test_flat_constant_exposes_expected_public_value(
        self,
        actual: str | int,
        expected: str | int,
    ) -> None:
        tm.that(actual, eq=expected)

    def test_common_name_constant_reuses_parent_ldap_attribute_name(self) -> None:
        # The domain CN constant must stay welded to the inherited protocol value,
        # not shadow it with a private copy.
        tm.that(c.DbtLdap.CN, eq=c.Ldap.AttributeName.COMMON_NAME)

    # --- UserDimension.from_ldap_entry mapping -----------------------------

    @staticmethod
    def _entry(attributes: dict[str, list[str]]) -> LdifEntry:
        return m.Ldif.Entry(
            dn=m.Ldif.DN(value="uid=jdoe,ou=people,dc=example,dc=com"),
            attributes=m.Ldif.Attributes.model_validate({"attributes": attributes}),
        )

    def test_from_ldap_entry_maps_canonical_attributes(self) -> None:
        entry = self._entry({
            "uid": ["jdoe"],
            "cn": ["John Doe"],
            "mail": ["john.doe@example.com"],
            "displayName": ["John D."],
            "department": ["Engineering"],
            "manager": ["uid=manager,ou=people,dc=example,dc=com"],
            "employeeNumber": ["123"],
            "telephoneNumber": ["+1-555-0100"],
            "createTimestamp": ["20250101000000Z"],
            "modifyTimestamp": ["20250102000000Z"],
            "objectClass": ["inetOrgPerson", "person"],
        })

        dimension = m.DbtLdap.UserDimension.from_ldap_entry(entry)

        tm.that(dimension.user_id, eq="jdoe")
        tm.that(dimension.common_name, eq="John Doe")
        tm.that(dimension.email, eq="john.doe@example.com")
        tm.that(dimension.display_name, eq="John D.")
        tm.that(dimension.department, eq="Engineering")
        tm.that(dimension.manager_dn, eq="uid=manager,ou=people,dc=example,dc=com")
        tm.that(dimension.employee_number, eq="123")
        tm.that(dimension.phone, eq="+1-555-0100")
        tm.that(dimension.created_date, eq="20250101000000Z")
        tm.that(dimension.modified_date, eq="20250102000000Z")
        tm.that(dimension.is_active, eq=True)

    def test_from_ldap_entry_leaves_optional_attributes_none_when_absent(self) -> None:
        entry = self._entry({
            "uid": ["mnimal"],
            "cn": ["Minimal User"],
            "objectClass": ["inetOrgPerson"],
        })

        dimension = m.DbtLdap.UserDimension.from_ldap_entry(entry)

        tm.that(dimension.user_id, eq="mnimal")
        tm.that(dimension.common_name, eq="Minimal User")
        tm.that(dimension.email, eq=None)
        tm.that(dimension.display_name, eq=None)
        tm.that(dimension.department, eq=None)
        tm.that(dimension.manager_dn, eq=None)
        tm.that(dimension.employee_number, eq=None)
        tm.that(dimension.phone, eq=None)
        tm.that(dimension.created_date, eq=None)
        tm.that(dimension.modified_date, eq=None)
        # Absent userAccountControl means the account is treated as active.
        tm.that(dimension.is_active, eq=True)

    def test_from_ldap_entry_is_idempotent_for_same_input(self) -> None:
        entry = self._entry({
            "uid": ["jdoe"],
            "cn": ["John Doe"],
            "mail": ["john.doe@example.com"],
        })

        fields = ("user_id", "common_name", "email", "is_active")
        first = m.DbtLdap.UserDimension.from_ldap_entry(entry)
        second = m.DbtLdap.UserDimension.from_ldap_entry(entry)

        tm.that(
            first.model_dump(include=set(fields)),
            eq=second.model_dump(include=set(fields)),
        )

    # --- UserDimension validation contract ---------------------------------

    def test_construction_rejects_blank_identity_fields(self) -> None:
        with pytest.raises(ValidationError):
            m.DbtLdap.UserDimension(user_id="", common_name="")

    def test_construction_requires_common_name(self) -> None:
        with pytest.raises(ValidationError):
            m.DbtLdap.UserDimension.model_validate({"user_id": "jdoe"})

    # --- UserDimension public serialization --------------------------------

    def test_to_dbt_dict_replaces_missing_optionals_with_empty_string(self) -> None:
        dimension = m.DbtLdap.UserDimension(user_id="jdoe", common_name="John Doe")

        dumped = dimension.to_dbt_dict()

        tm.that(dumped["user_id"], eq="jdoe")
        tm.that(dumped["common_name"], eq="John Doe")
        tm.that(dumped["email"], eq="")
        tm.that(dumped["phone"], eq="")
        tm.that(dumped["is_active"], eq=True)


__all__: list[str] = ["TestsFlextDbtLdapConstantsFlatApi"]
