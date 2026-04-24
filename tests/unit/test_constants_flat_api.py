"""Behavior contract for flattened DbtLdap constants surface."""

from __future__ import annotations

from flext_tests import tm

from tests import c, m


class TestsFlextDbtLdapConstantsFlatApi:
    """Behavior contract for c.DbtLdap flat surface and UserDimension integration."""

    def test_flat_constants_surface_reuses_parent_ldap(self) -> None:
        tm.that(c.DbtLdap.CN, eq=c.Ldap.LdapAttributeNames.COMMON_NAME)
        tm.that(c.DbtLdap.FILTER_GROUP, eq="(objectClass=group)")
        tm.that(c.DbtLdap.STG_USERS, eq="stg_users")
        tm.that(c.DbtLdap.DEFAULT_BATCH_SIZE, eq=c.DEFAULT_SIZE)
        tm.that(hasattr(c.DbtLdap, "LdapAttributes"), eq=False)
        tm.that(hasattr(c.DbtLdap, "DbtModels"), eq=False)
        tm.that(hasattr(c.DbtLdap, "DataTypes"), eq=False)

    def test_user_dimension_from_ldap_entry_maps_canonical_attributes(self) -> None:
        entry = m.Ldif.Entry(
            dn=m.Ldif.DN(value="uid=jdoe,ou=people,dc=example,dc=com"),
            attributes=m.Ldif.Attributes.model_validate({
                "attributes": {
                    "uid": ["jdoe"],
                    "cn": ["John Doe"],
                    "mail": ["john.doe@example.com"],
                    "displayName": ["John Doe"],
                    "department": ["Engineering"],
                    "manager": ["uid=manager,ou=people,dc=example,dc=com"],
                    "employeeNumber": ["123"],
                    "telephoneNumber": ["+1-555-0100"],
                    "createTimestamp": ["20250101000000Z"],
                    "modifyTimestamp": ["20250102000000Z"],
                    "objectClass": ["inetOrgPerson", "person"],
                },
            }),
        )

        dimension = m.DbtLdap.UserDimension.from_ldap_entry(entry)

        tm.that(dimension.user_id, eq="jdoe")
        tm.that(dimension.common_name, eq="John Doe")
        tm.that(dimension.email, eq="john.doe@example.com")
        tm.that(dimension.department, eq="Engineering")
        tm.that(dimension.employee_number, eq="123")
        tm.that(dimension.created_date, eq="20250101000000Z")
        tm.that(dimension.modified_date, eq="20250102000000Z")
        tm.that(dimension.is_active, eq=True)
