"""FLEXT DBT LDAP Models.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import override

from flext_core import FlextLogger, FlextModels, FlextResult, FlextTypes
from flext_ldap import FlextLDAPEntities, FlextLDAPModels

from flext_dbt_ldap.typings import FlextDbtLdapTypes

logger = FlextLogger(__name__)


class FlextDbtLdapModels(FlextModels):
    """Unified DBT LDAP models collection with nested model classes."""

    class UserDimension(FlextModels.Entity):
        """User dimension model for DBT LDAP transformations.

        Represents a user dimension table structure optimized for analytics.
        """

        user_id: str
        common_name: str
        email: str | None = None
        display_name: str | None = None
        department: str | None = None
        manager_dn: str | None = None
        employee_number: str | None = None
        phone: str | None = None
        is_active: bool = True
        created_date: str | None = None
        modified_date: str | None = None

        @classmethod
        def from_ldap_entry(
            cls,
            entry: FlextLDAPEntities.Entry,
        ) -> FlextDbtLdapModels.UserDimension:
            """Create user dimension from LDAP entry."""
            # Normalize attributes to dict[str, FlextDbtLdapTypes.Core.StringList]
            raw = entry.attributes
            attrs: dict[str, FlextDbtLdapTypes.Core.StringList] = {}
            if isinstance(raw, dict):
                for k, v in raw.items():
                    if isinstance(v, list):
                        attrs[k] = [str(x) for x in v]
                    else:
                        attrs[k] = [str(v)] if v is not None else []

            return cls(
                user_id=attrs.get("uid", [""])[0] if "uid" in attrs else "",
                common_name=attrs.get("cn", [""])[0] if "cn" in attrs else "",
                email=attrs.get("mail", [None])[0] if "mail" in attrs else None,
                display_name=attrs.get("displayName", [None])[0]
                if "displayName" in attrs
                else None,
                department=attrs.get("department", [None])[0]
                if "department" in attrs
                else None,
                manager_dn=attrs.get("manager", [None])[0]
                if "manager" in attrs
                else None,
                employee_number=attrs.get("employeeNumber", [None])[0]
                if "employeeNumber" in attrs
                else None,
                phone=attrs.get("telephoneNumber", [None])[0]
                if "telephoneNumber" in attrs
                else None,
                is_active=not (
                    "userAccountControl" in attrs
                    and "2" in str(attrs["userAccountControl"][0])
                ),
                created_date=attrs.get("createTimestamp", [None])[0]
                if "createTimestamp" in attrs
                else None,
                modified_date=attrs.get("modifyTimestamp", [None])[0]
                if "modifyTimestamp" in attrs
                else None,
            )

        def validate_business_rules(self: object) -> FlextResult[None]:
            """Validate user dimension business rules."""
            if not self.user_id or not self.common_name:
                return FlextResult[None].fail("User ID and common name are required")
            return FlextResult[None].ok(None)

        def to_dbt_dict(self: object) -> FlextTypes.Dict:
            """Convert to dictionary suitable for DBT processing."""
            return {
                "user_id": self.user_id,
                "common_name": self.common_name,
                "email": self.email,
                "display_name": self.display_name,
                "department": self.department,
                "manager_dn": self.manager_dn,
                "employee_number": self.employee_number,
                "phone": self.phone,
                "is_active": self.is_active,
                "created_date": self.created_date,
                "modified_date": self.modified_date,
            }

    class GroupDimension(FlextModels.Entity):
        """Group dimension model for DBT LDAP transformations.

        Represents a group dimension table structure optimized for analytics.
        """

        group_id: str
        common_name: str
        description: str | None = None
        group_type: str | None = None
        member_count: int = 0
        is_active: bool = True
        created_date: str | None = None
        modified_date: str | None = None

        @classmethod
        def from_ldap_entry(
            cls,
            entry: FlextLDAPEntities.Entry,
        ) -> FlextDbtLdapModels.GroupDimension:
            """Create group dimension from LDAP entry."""
            raw = entry.attributes
            attrs: dict[str, FlextDbtLdapTypes.Core.StringList] = {}
            if isinstance(raw, dict):
                for k, v in raw.items():
                    if isinstance(v, list):
                        attrs[k] = [str(x) for x in v]
                    else:
                        attrs[k] = [str(v)] if v is not None else []

            # Count members
            member_count = 0
            if "member" in attrs:
                member_count = len(attrs["member"])
            elif "uniqueMember" in attrs:
                member_count = len(attrs["uniqueMember"])

            return cls(
                group_id=attrs.get("cn", [""])[0] if "cn" in attrs else "",
                common_name=attrs.get("cn", [""])[0] if "cn" in attrs else "",
                description=attrs.get("description", [None])[0]
                if "description" in attrs
                else None,
                group_type=attrs.get("groupType", [None])[0]
                if "groupType" in attrs
                else None,
                member_count=member_count,
                is_active=True,  # Groups are typically active by default
                created_date=attrs.get("createTimestamp", [None])[0]
                if "createTimestamp" in attrs
                else None,
                modified_date=attrs.get("modifyTimestamp", [None])[0]
                if "modifyTimestamp" in attrs
                else None,
            )

        def validate_business_rules(self: object) -> FlextResult[None]:
            """Validate group dimension business rules."""
            if not self.group_id or not self.common_name:
                return FlextResult[None].fail("Group ID and common name are required")
            if self.member_count < 0:
                return FlextResult[None].fail("Member count cannot be negative")
            return FlextResult[None].ok(None)

        def to_dbt_dict(self: object) -> FlextTypes.Dict:
            """Convert to dictionary suitable for DBT processing."""
            return {
                "group_id": self.group_id,
                "common_name": self.common_name,
                "description": self.description,
                "group_type": self.group_type,
                "member_count": self.member_count,
                "is_active": self.is_active,
                "created_date": self.created_date,
                "modified_date": self.modified_date,
            }

    class MembershipFact(FlextModels.Entity):
        """Membership fact model for DBT LDAP transformations.

        Represents user-group membership relationships as fact table.
        """

        user_dn: str
        group_dn: str
        membership_type: str = "direct"  # direct, nested, computed
        is_primary: bool = False
        effective_date: str | None = None
        expiry_date: str | None = None

        def validate_business_rules(self: object) -> FlextResult[None]:
            """Validate membership fact business rules."""
            if not self.user_dn or not self.group_dn:
                return FlextResult[None].fail("User DN and Group DN are required")
            return FlextResult[None].ok(None)

        def to_dbt_dict(self: object) -> FlextTypes.Dict:
            """Convert to dictionary suitable for DBT processing."""
            return {
                "user_dn": self.user_dn,
                "group_dn": self.group_dn,
                "membership_type": self.membership_type,
                "is_primary": self.is_primary,
                "effective_date": self.effective_date,
                "expiry_date": self.expiry_date,
            }

    class Transformer:
        """LDAP data transformer for DBT operations.

        Transforms LDAP entries into DBT-compatible data models.
        """

        @override
        def __init__(self: object) -> None:
            """Initialize LDAP transformer."""
            logger.info("Initialized LDAP DBT transformer")

        def transform_users(
            self,
            entries: list[FlextLDAPEntities.Entry],
        ) -> list[FlextDbtLdapModels.UserDimension]:
            """Transform LDAP entries to user dimensions.

            Args:
                entries: List of LDAP entries

            Returns:
                List of user dimension models

            """
            logger.info("Transforming %d LDAP entries to user dimensions", len(entries))

            user_dims = []

            for entry in entries:
                # Filter user entries
                if self._is_user_entry(entry):
                    try:
                        user_dim = FlextDbtLdapModels.UserDimension.from_ldap_entry(
                            entry,
                        )
                        user_dims.append(user_dim)
                    except Exception:
                        logger.exception("Failed to transform user entry: %s", entry.dn)
                        continue

            logger.info("Transformed %d user dimensions", len(user_dims))
            return user_dims

        def transform_groups(
            self,
            entries: list[FlextLDAPEntities.Entry],
        ) -> list[FlextDbtLdapModels.GroupDimension]:
            """Transform LDAP entries to group dimensions.

            Args:
                entries: List of LDAP entries

            Returns:
                List of group dimension models

            """
            logger.info(
                "Transforming %d LDAP entries to group dimensions",
                len(entries),
            )

            group_dims = []

            for entry in entries:
                # Filter group entries
                if self._is_group_entry(entry):
                    try:
                        group_dim = FlextDbtLdapModels.GroupDimension.from_ldap_entry(
                            entry,
                        )
                        group_dims.append(group_dim)
                    except Exception:
                        logger.exception(
                            "Failed to transform group entry: %s",
                            entry.dn,
                        )
                        continue

            logger.info("Transformed %d group dimensions", len(group_dims))
            return group_dims

        def transform_memberships(
            self,
            entries: list[FlextLDAPEntities.Entry],
        ) -> list[FlextDbtLdapModels.MembershipFact]:
            """Transform LDAP entries to membership facts.

            Args:
                entries: List of LDAP entries

            Returns:
                List of membership fact models

            """
            logger.info(
                "Transforming %d LDAP entries to membership facts",
                len(entries),
            )

            membership_facts = []

            for entry in entries:
                try:
                    # Extract memberships from group entries
                    if self._is_group_entry(entry):
                        memberships = self._extract_group_memberships(entry)
                        membership_facts.extend(memberships)

                    # Extract memberships from user entries
                    elif self._is_user_entry(entry):
                        memberships = self._extract_user_memberships(entry)
                        membership_facts.extend(memberships)

                except Exception:
                    logger.exception(
                        "Failed to transform memberships for entry: %s",
                        entry.dn,
                    )
                    continue

            logger.info("Transformed %d membership facts", len(membership_facts))
            return membership_facts

        def _is_user_entry(self, entry: FlextLDAPEntities.Entry) -> bool:
            """Check if entry is a user entry."""
            raw = entry.attributes
            object_classes: FlextDbtLdapTypes.Core.StringList = []
            if isinstance(raw, dict):
                oc_val: FlextTypes.List = raw.get("objectClass", [])
                if isinstance(oc_val, list):
                    object_classes = [str(x) for x in oc_val]
                elif oc_val is not None:
                    object_classes = [str(oc_val)]
            user_classes = ["person", "user", "inetOrgPerson", "organizationalPerson"]
            return any(cls in object_classes for cls in user_classes)

        def _is_group_entry(self, entry: FlextLDAPEntities.Entry) -> bool:
            """Check if entry is a group entry."""
            raw = entry.attributes
            object_classes: FlextDbtLdapTypes.Core.StringList = []
            if isinstance(raw, dict):
                oc_val: FlextTypes.List = raw.get("objectClass", [])
                if isinstance(oc_val, list):
                    object_classes = [str(x) for x in oc_val]
                elif oc_val is not None:
                    object_classes = [str(oc_val)]
            group_classes = [
                "group",
                "groupOfNames",
                "groupOfUniqueNames",
                "posixGroup",
            ]
            return any(cls in object_classes for cls in group_classes)

        def _extract_group_memberships(
            self,
            group_entry: FlextLDAPEntities.Entry,
        ) -> list[FlextDbtLdapModels.MembershipFact]:
            """Extract memberships from a group entry."""
            memberships: list[FlextDbtLdapModels.MembershipFact] = []
            raw = group_entry.attributes
            attrs: dict[str, FlextDbtLdapTypes.Core.StringList] = {}
            if isinstance(raw, dict):
                for k, v in raw.items():
                    if isinstance(v, list):
                        attrs[k] = [str(x) for x in v]
                    else:
                        attrs[k] = [str(v)] if v is not None else []

            # Handle different membership attribute types
            member_attrs = ["member", "uniqueMember", "memberUid"]

            for attr in member_attrs:
                if attr in attrs:
                    for member_dn in attrs[attr]:
                        membership = FlextDbtLdapModels.MembershipFact(
                            user_dn=member_dn,
                            group_dn=group_entry.dn,
                            membership_type="direct",
                        )
                        memberships.append(membership)

            return memberships

        def _extract_user_memberships(
            self,
            user_entry: FlextLDAPEntities.Entry,
        ) -> list[FlextDbtLdapModels.MembershipFact]:
            """Extract memberships from a user entry."""
            memberships: list[FlextDbtLdapModels.MembershipFact] = []
            raw = user_entry.attributes
            attrs: dict[str, FlextDbtLdapTypes.Core.StringList] = {}
            if isinstance(raw, dict):
                for k, v in raw.items():
                    if isinstance(v, list):
                        attrs[k] = [str(x) for x in v]
                    else:
                        attrs[k] = [str(v)] if v is not None else []

            # Handle memberOf attribute
            if "memberOf" in attrs:
                for group_dn in attrs["memberOf"]:
                    membership = FlextDbtLdapModels.MembershipFact(
                        user_dn=user_entry.dn,
                        group_dn=group_dn,
                        membership_type="direct",
                    )
                    memberships.append(membership)

            return memberships


# Unified class pattern - all access through FlextDbtLdapModels


__all__: FlextDbtLdapTypes.Core.StringList = [
    "FlextDbtLdapModels",
    # Re-exports from flext-ldap for convenience - unified class pattern
    "FlextLDAPEntities",
    "FlextLDAPModels",
]


__all__: FlextDbtLdapTypes.Core.StringList = [
    "FlextDbtLdapModels",
    # Re-exports from flext-ldap for convenience - use unified class pattern
    "FlextLDAPEntities",
    "FlextLDAPModels",
]
