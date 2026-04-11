"""Dimension and fact models for dbt-ldap."""

from __future__ import annotations

from typing import Annotated, Self

from flext_ldif import m as lm
from pydantic import Field, model_validator

from flext_dbt_ldap._models.shared import FlextDbtLdapModelsShared
from flext_dbt_ldap._utilities.entry import FlextDbtLdapUtilitiesEntry
from flext_dbt_ldap.constants import c


class FlextDbtLdapModelsDimensions(FlextDbtLdapModelsShared):
    """Directory-backed dimensions and facts for dbt-ldap."""

    class UserDimension(FlextDbtLdapModelsShared.DbtDimensionBase):
        """Canonical user dimension."""

        user_id: Annotated[str, Field(description="Canonical user identifier")]
        email: Annotated[
            str | None, Field(default=None, description="Primary user email")
        ] = None
        display_name: Annotated[
            str | None, Field(default=None, description="Display name shown to users")
        ] = None
        department: Annotated[
            str | None, Field(default=None, description="User department name")
        ] = None
        manager_dn: Annotated[
            str | None,
            Field(default=None, description="Distinguished name of the manager"),
        ] = None
        employee_number: Annotated[
            str | None, Field(default=None, description="Employee number from LDAP")
        ] = None
        phone: Annotated[
            str | None, Field(default=None, description="Primary phone number")
        ] = None

        @model_validator(mode="after")
        def validate_required_fields(self) -> Self:
            """Validate required business fields."""
            if not self.user_id or not self.common_name:
                msg = "User ID and common name are required"
                raise ValueError(msg)
            return self

        @classmethod
        def from_ldap_entry(cls, entry: lm.Ldif.Entry) -> Self:
            """Build a user dimension from a LDIF entry."""
            attrs = FlextDbtLdapUtilitiesEntry.ldap_entry_mapping(entry)
            return cls(
                user_id=FlextDbtLdapUtilitiesEntry.ldap_first_attribute(
                    attrs, c.DbtLdap.UID, c.DEFAULT_EMPTY_STRING
                )
                or c.DEFAULT_EMPTY_STRING,
                common_name=FlextDbtLdapUtilitiesEntry.ldap_first_attribute(
                    attrs, c.DbtLdap.CN, c.DEFAULT_EMPTY_STRING
                )
                or c.DEFAULT_EMPTY_STRING,
                email=FlextDbtLdapUtilitiesEntry.ldap_first_attribute(
                    attrs, c.DbtLdap.MAIL
                ),
                display_name=FlextDbtLdapUtilitiesEntry.ldap_first_attribute(
                    attrs, c.DbtLdap.DISPLAY_NAME
                ),
                department=FlextDbtLdapUtilitiesEntry.ldap_first_attribute(
                    attrs, c.DbtLdap.DEPARTMENT
                ),
                manager_dn=FlextDbtLdapUtilitiesEntry.ldap_first_attribute(
                    attrs, c.DbtLdap.MANAGER
                ),
                employee_number=FlextDbtLdapUtilitiesEntry.ldap_first_attribute(
                    attrs, c.DbtLdap.EMPLOYEE_NUMBER
                ),
                phone=FlextDbtLdapUtilitiesEntry.ldap_first_attribute(
                    attrs, c.DbtLdap.TELEPHONE_NUMBER
                ),
                is_active=FlextDbtLdapUtilitiesEntry.is_active_entry(attrs),
                created_date=FlextDbtLdapUtilitiesEntry.ldap_first_attribute(
                    attrs, c.DbtLdap.CREATE_TIMESTAMP
                ),
                modified_date=FlextDbtLdapUtilitiesEntry.ldap_first_attribute(
                    attrs, c.DbtLdap.MODIFY_TIMESTAMP
                ),
            )

    class GroupDimension(FlextDbtLdapModelsShared.DbtDimensionBase):
        """Canonical group dimension."""

        group_id: Annotated[str, Field(description="Canonical group identifier")]
        description: Annotated[
            str | None, Field(default=None, description="Group description from LDAP")
        ] = None
        group_type: Annotated[
            str | None, Field(default=None, description="Group type classification")
        ] = None
        member_count: Annotated[
            int, Field(description="Number of direct group members")
        ] = 0

        @model_validator(mode="after")
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
        def from_ldap_entry(cls, entry: lm.Ldif.Entry) -> Self:
            """Build a group dimension from a LDIF entry."""
            attrs = FlextDbtLdapUtilitiesEntry.ldap_entry_mapping(entry)
            member_count = len(attrs.get(c.DbtLdap.MEMBER, [])) + len(
                attrs.get(c.DbtLdap.UNIQUE_MEMBER, []),
            )
            common_name = (
                FlextDbtLdapUtilitiesEntry.ldap_first_attribute(
                    attrs,
                    c.DbtLdap.CN,
                    c.DEFAULT_EMPTY_STRING,
                )
                or c.DEFAULT_EMPTY_STRING
            )
            return cls(
                group_id=common_name,
                common_name=common_name,
                description=FlextDbtLdapUtilitiesEntry.ldap_first_attribute(
                    attrs, c.DbtLdap.DESCRIPTION
                ),
                group_type=FlextDbtLdapUtilitiesEntry.ldap_first_attribute(
                    attrs, c.DbtLdap.GROUP_TYPE
                ),
                member_count=member_count,
                is_active=True,
                created_date=FlextDbtLdapUtilitiesEntry.ldap_first_attribute(
                    attrs, c.DbtLdap.CREATE_TIMESTAMP
                ),
                modified_date=FlextDbtLdapUtilitiesEntry.ldap_first_attribute(
                    attrs, c.DbtLdap.MODIFY_TIMESTAMP
                ),
            )

    class MembershipFact(FlextDbtLdapModelsShared.DbtSerializable):
        """Canonical membership fact."""

        user_dn: Annotated[str, Field(description="Member distinguished name")]
        group_dn: Annotated[str, Field(description="Group distinguished name")]
        membership_type: Annotated[
            str, Field(description="Membership relationship type")
        ] = c.DbtLdap.DIRECT
        is_primary: Annotated[
            bool, Field(description="Whether the membership is the primary assignment")
        ] = False
        effective_date: Annotated[
            str | None,
            Field(default=None, description="Membership effective timestamp"),
        ] = None
        expiry_date: Annotated[
            str | None, Field(default=None, description="Membership expiry timestamp")
        ] = None

        @model_validator(mode="after")
        def validate_required_fields(self) -> Self:
            """Validate required business fields."""
            if not self.user_dn or not self.group_dn:
                msg = "User DN and Group DN are required"
                raise ValueError(msg)
            return self
