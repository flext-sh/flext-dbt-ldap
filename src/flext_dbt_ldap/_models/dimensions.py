"""Dimension and fact models for dbt-ldap."""

from __future__ import annotations

from typing import Annotated, Self

from flext_ldif import m, u

from flext_dbt_ldap import FlextDbtLdapModelsShared, FlextDbtLdapUtilitiesEntry, c
from flext_ldap import FlextLdapUtilities as ul


class FlextDbtLdapModelsDimensions(FlextDbtLdapModelsShared):
    """Directory-backed dimensions and facts for dbt-ldap."""

    class UserDimension(FlextDbtLdapModelsShared.DbtDimensionBase):
        """Canonical user dimension."""

        user_id: Annotated[str, u.Field(description="Canonical user identifier")]
        email: Annotated[str | None, u.Field(description="Primary user email")] = None
        display_name: Annotated[
            str | None, u.Field(description="Display name shown to users")
        ] = None
        department: Annotated[
            str | None, u.Field(description="User department name")
        ] = None
        manager_dn: Annotated[
            str | None, u.Field(description="Distinguished name of the manager")
        ] = None
        employee_number: Annotated[
            str | None, u.Field(description="Employee number from LDAP")
        ] = None
        phone: Annotated[str | None, u.Field(description="Primary phone number")] = None

        @u.model_validator(mode="after")
        def validate_required_fields(self) -> Self:
            """Validate required business fields."""
            if not self.user_id or not self.common_name:
                msg = "User ID and common name are required"
                raise ValueError(msg)
            return self

        @classmethod
        def from_ldap_entry(cls, entry: m.Ldif.Entry) -> Self:
            """Build a user dimension from a LDIF entry."""
            attrs = ul.Ldap.extract_entry_attributes(entry)
            return cls(
                user_id=ul.Ldap.get_first_attribute_value(attrs, c.DbtLdap.UID)
                or c.DEFAULT_EMPTY_STRING,
                common_name=ul.Ldap.get_first_attribute_value(attrs, c.DbtLdap.CN)
                or c.DEFAULT_EMPTY_STRING,
                email=ul.Ldap.get_first_attribute_value(attrs, c.DbtLdap.MAIL),
                display_name=ul.Ldap.get_first_attribute_value(
                    attrs,
                    c.DbtLdap.DISPLAY_NAME,
                ),
                department=ul.Ldap.get_first_attribute_value(
                    attrs,
                    c.DbtLdap.DEPARTMENT,
                ),
                manager_dn=ul.Ldap.get_first_attribute_value(
                    attrs,
                    c.DbtLdap.MANAGER,
                ),
                employee_number=ul.Ldap.get_first_attribute_value(
                    attrs,
                    c.DbtLdap.EMPLOYEE_NUMBER,
                ),
                phone=ul.Ldap.get_first_attribute_value(
                    attrs,
                    c.DbtLdap.TELEPHONE_NUMBER,
                ),
                is_active=FlextDbtLdapUtilitiesEntry.is_active_entry(attrs),
                created_date=ul.Ldap.get_first_attribute_value(
                    attrs,
                    c.DbtLdap.CREATE_TIMESTAMP,
                ),
                modified_date=ul.Ldap.get_first_attribute_value(
                    attrs,
                    c.DbtLdap.MODIFY_TIMESTAMP,
                ),
            )

    class GroupDimension(FlextDbtLdapModelsShared.DbtDimensionBase):
        """Canonical group dimension."""

        group_id: Annotated[str, u.Field(description="Canonical group identifier")]
        description: Annotated[
            str | None, u.Field(description="Group description from LDAP")
        ] = None
        group_type: Annotated[
            str | None, u.Field(description="Group type classification")
        ] = None
        member_count: Annotated[
            int, u.Field(description="Number of direct group members")
        ] = 0

        @u.model_validator(mode="after")
        def validate_required_fields(self) -> Self:
            """Validate required business fields."""
            if not self.group_id or not self.common_name:
                msg = "Group ID and common name are required"
                raise ValueError(msg)
            if self.member_count < 0:
                msg = "Member count cannot be negative"
                raise ValueError(msg)
            return self

        @classmethod
        def from_ldap_entry(cls, entry: m.Ldif.Entry) -> Self:
            """Build a group dimension from a LDIF entry."""
            attrs = ul.Ldap.extract_entry_attributes(entry)
            member_count = len(attrs.get(c.DbtLdap.MEMBER, [])) + len(
                attrs.get(c.DbtLdap.UNIQUE_MEMBER, []),
            )
            common_name = (
                ul.Ldap.get_first_attribute_value(attrs, c.DbtLdap.CN)
                or c.DEFAULT_EMPTY_STRING
            )
            return cls(
                group_id=common_name,
                common_name=common_name,
                description=ul.Ldap.get_first_attribute_value(
                    attrs,
                    c.DbtLdap.DESCRIPTION,
                ),
                group_type=ul.Ldap.get_first_attribute_value(
                    attrs,
                    c.DbtLdap.GROUP_TYPE,
                ),
                member_count=member_count,
                is_active=True,
                created_date=ul.Ldap.get_first_attribute_value(
                    attrs,
                    c.DbtLdap.CREATE_TIMESTAMP,
                ),
                modified_date=ul.Ldap.get_first_attribute_value(
                    attrs,
                    c.DbtLdap.MODIFY_TIMESTAMP,
                ),
            )

    class MembershipFact(FlextDbtLdapModelsShared.DbtSerializable):
        """Canonical membership fact."""

        user_dn: Annotated[str, u.Field(description="Member distinguished name")]
        group_dn: Annotated[str, u.Field(description="Group distinguished name")]
        membership_type: Annotated[
            str, u.Field(description="Membership relationship type")
        ] = c.DbtLdap.DIRECT
        is_primary: Annotated[
            bool,
            u.Field(description="Whether the membership is the primary assignment"),
        ] = False
        effective_date: Annotated[
            str | None, u.Field(description="Membership effective timestamp")
        ] = None
        expiry_date: Annotated[
            str | None, u.Field(description="Membership expiry timestamp")
        ] = None

        @u.model_validator(mode="after")
        def validate_required_fields(self) -> Self:
            """Validate required business fields."""
            if not self.user_dn or not self.group_dn:
                msg = "User DN and Group DN are required"
                raise ValueError(msg)
            return self
