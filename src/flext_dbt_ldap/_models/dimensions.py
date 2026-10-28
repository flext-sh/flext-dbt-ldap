"""Dimension and fact models for dbt-ldap.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_ldap/_models/dimensions
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Annotated, Self

from flext_ldap import m, t, u

from flext_dbt_ldap import c
from flext_dbt_ldap._models.shared import FlextModelsDbtLdapShared
from flext_dbt_ldap._utilities import FlextDbtLdapUtilitiesEntry


class FlextModelsDbtLdapDimensions(FlextModelsDbtLdapShared):
    """Directory-backed dimensions and facts for dbt-ldap."""

    class UserDimension(FlextModelsDbtLdapShared.DbtDimensionBase):
        """Canonical user dimension."""

        user_id: Annotated[str, m.Field(description="Canonical user identifier")]
        email: Annotated[str | None, m.Field(description="Primary user email")] = None
        display_name: Annotated[
            str | None,
            m.Field(description="Display name shown to users"),
        ] = None
        department: Annotated[
            str | None,
            m.Field(description="User department name"),
        ] = None
        manager_dn: Annotated[
            str | None,
            m.Field(description="Distinguished name of the manager"),
        ] = None
        employee_number: Annotated[
            str | None,
            m.Field(description="Employee number from LDAP"),
        ] = None
        phone: Annotated[str | None, m.Field(description="Primary phone number")] = None

        @m.model_validator(mode="after")
        def validate_required_fields(self) -> Self:
            """Validate required business fields.

            Returns:
                The resulting ``Self``.

            Raises:
                ValueError: If User ID and common name are required.

            """
            if not self.user_id or not self.common_name:
                msg = "User ID and common name are required"
                raise ValueError(msg)
            return self

        @classmethod
        def from_ldap_entry(cls, entry: t.Ldif.EntryLike) -> Self:
            """Build a user dimension from a LDIF entry.

            Args:
                entry: LDIF entry carrying the user LDAP attributes.

            Returns:
                The resulting ``Self``.

            """
            attrs = u.Ldap.extract_entry_attributes(entry)
            return cls(
                user_id=u.Ldap.resolve_first_attribute_value(attrs, c.DbtLdap.UID)
                or c.DEFAULT_EMPTY_STRING,
                common_name=u.Ldap.resolve_first_attribute_value(attrs, c.DbtLdap.CN)
                or c.DEFAULT_EMPTY_STRING,
                email=u.Ldap.resolve_first_attribute_value(attrs, c.DbtLdap.MAIL),
                display_name=u.Ldap.resolve_first_attribute_value(
                    attrs,
                    c.DbtLdap.DISPLAY_NAME,
                ),
                department=u.Ldap.resolve_first_attribute_value(
                    attrs,
                    c.DbtLdap.DEPARTMENT,
                ),
                manager_dn=u.Ldap.resolve_first_attribute_value(
                    attrs,
                    c.DbtLdap.MANAGER,
                ),
                employee_number=u.Ldap.resolve_first_attribute_value(
                    attrs,
                    c.DbtLdap.EMPLOYEE_NUMBER,
                ),
                phone=u.Ldap.resolve_first_attribute_value(
                    attrs,
                    c.DbtLdap.TELEPHONE_NUMBER,
                ),
                is_active=FlextDbtLdapUtilitiesEntry.active_entry(attrs),
                created_date=u.Ldap.resolve_first_attribute_value(
                    attrs,
                    c.DbtLdap.CREATE_TIMESTAMP,
                ),
                modified_date=u.Ldap.resolve_first_attribute_value(
                    attrs,
                    c.DbtLdap.MODIFY_TIMESTAMP,
                ),
            )

    class GroupDimension(FlextModelsDbtLdapShared.DbtDimensionBase):
        """Canonical group dimension."""

        group_id: Annotated[str, m.Field(description="Canonical group identifier")]
        description: Annotated[
            str | None,
            m.Field(description="Group description from LDAP"),
        ] = None
        group_type: Annotated[
            str | None,
            m.Field(description="Group type classification"),
        ] = None
        member_count: Annotated[
            int,
            m.Field(description="Number of direct group members"),
        ] = 0

        @m.model_validator(mode="after")
        def validate_required_fields(self) -> Self:
            """Validate required business fields.

            Returns:
                The resulting ``Self``.

            Raises:
                ValueError: If Group ID and common name are required; or if Member count
                    cannot be negative.

            """
            if not self.group_id or not self.common_name:
                msg = "Group ID and common name are required"
                raise ValueError(msg)
            if self.member_count < 0:
                msg = "Member count cannot be negative"
                raise ValueError(msg)
            return self

        @classmethod
        def from_ldap_entry(cls, entry: t.Ldif.EntryLike) -> Self:
            """Build a group dimension from a LDIF entry.

            Args:
                entry: LDIF entry carrying the group LDAP attributes.

            Returns:
                The resulting ``Self``.

            """
            attrs = u.Ldap.extract_entry_attributes(entry)
            member_count = len(attrs.get(c.DbtLdap.MEMBER, [])) + len(
                attrs.get(c.DbtLdap.UNIQUE_MEMBER, []),
            )
            common_name = (
                u.Ldap.resolve_first_attribute_value(attrs, c.DbtLdap.CN)
                or c.DEFAULT_EMPTY_STRING
            )
            return cls(
                group_id=common_name,
                common_name=common_name,
                description=u.Ldap.resolve_first_attribute_value(
                    attrs,
                    c.DbtLdap.DESCRIPTION,
                ),
                group_type=u.Ldap.resolve_first_attribute_value(
                    attrs,
                    c.DbtLdap.GROUP_TYPE,
                ),
                member_count=member_count,
                is_active=True,
                created_date=u.Ldap.resolve_first_attribute_value(
                    attrs,
                    c.DbtLdap.CREATE_TIMESTAMP,
                ),
                modified_date=u.Ldap.resolve_first_attribute_value(
                    attrs,
                    c.DbtLdap.MODIFY_TIMESTAMP,
                ),
            )

    class MembershipFact(FlextModelsDbtLdapShared.DbtSerializable):
        """Canonical membership fact."""

        user_dn: Annotated[str, m.Field(description="Member distinguished name")]
        group_dn: Annotated[str, m.Field(description="Group distinguished name")]
        membership_type: Annotated[
            str,
            m.Field(description="Membership relationship type"),
        ] = c.DbtLdap.DIRECT
        is_primary: Annotated[
            bool,
            m.Field(description="Whether the membership is the primary assignment"),
        ] = False
        effective_date: Annotated[
            str | None,
            m.Field(description="Membership effective timestamp"),
        ] = None
        expiry_date: Annotated[
            str | None,
            m.Field(description="Membership expiry timestamp"),
        ] = None

        @m.model_validator(mode="after")
        def validate_required_fields(self) -> Self:
            """Validate required business fields.

            Returns:
                The resulting ``Self``.

            Raises:
                ValueError: If User DN and Group DN are required.

            """
            if not self.user_dn or not self.group_dn:
                msg = "User DN and Group DN are required"
                raise ValueError(msg)
            return self


__all__: list[str] = ["FlextModelsDbtLdapDimensions"]
