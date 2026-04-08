"""Regression tests for the flattened DbtLdap constants surface."""

from __future__ import annotations

from tests import c, m


def test_dbt_ldap_constants_surface_is_flat() -> None:
    """The local namespace stays flat and reuses parent LDAP constants."""
    assert c.DbtLdap.CN == c.Ldap.LdapAttributeNames.COMMON_NAME
    assert c.DbtLdap.FILTER_GROUP == "(objectClass=group)"
    assert c.DbtLdap.STG_USERS == "stg_users"
    assert c.DbtLdap.DEFAULT_BATCH_SIZE == c.DEFAULT_SIZE
    assert not hasattr(c.DbtLdap, "LdapAttributes")
    assert not hasattr(c.DbtLdap, "DbtModels")
    assert not hasattr(c.DbtLdap, "DataTypes")


def test_user_dimension_from_ldap_entry_uses_flat_constants_surface() -> None:
    """Public model construction uses the flattened DbtLdap constants surface."""
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

    assert dimension.user_id == "jdoe"
    assert dimension.common_name == "John Doe"
    assert dimension.email == "john.doe@example.com"
    assert dimension.department == "Engineering"
    assert dimension.employee_number == "123"
    assert dimension.created_date == "20250101000000Z"
    assert dimension.modified_date == "20250102000000Z"
    assert dimension.is_active is True
