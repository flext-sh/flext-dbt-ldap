"""FLEXT DBT LDAP Utilities — LDAP integration for DBT.

Absorbed from ldap_integration.py into u.DbtLdap namespace.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_ldap import FlextLdapUtilities as ul
from flext_meltano import u

from flext_dbt_ldap import c, m, t
from flext_dbt_ldap._utilities.entry import FlextDbtLdapUtilitiesEntry

if TYPE_CHECKING:
    from collections.abc import Callable


class FlextDbtLdapUtilitiesIntegration(FlextDbtLdapUtilitiesEntry):
    """Typed LDAP-to-DBT transformation helpers."""

    _log = u.fetch_logger(__name__)

    @classmethod
    def transform_groups(
        cls,
        entries: t.SequenceOf[m.Ldif.Entry],
    ) -> t.SequenceOf[m.DbtLdap.GroupDimension]:
        """Transform LDAP entries into typed group dimensions.

        Returns:
            The resulting ``t.SequenceOf[m.DbtLdap.GroupDimension]``.
        """
        groups = [entry for entry in entries if cls.group_entry(entry)]
        build = m.DbtLdap.GroupDimension.from_ldap_entry
        return cls._transform_entries_to_dimensions(groups, build, "group")

    @classmethod
    def transform_memberships(
        cls,
        entries: t.SequenceOf[m.Ldif.Entry],
    ) -> t.SequenceOf[m.DbtLdap.MembershipFact]:
        """Transform LDAP entries into membership facts.

        Returns:
            The resulting ``t.SequenceOf[m.DbtLdap.MembershipFact]``.
        """
        cls._log.info("Transforming %d LDAP entries to membership facts", len(entries))
        memberships: list[m.DbtLdap.MembershipFact] = []
        for entry in entries:
            try:
                if cls.group_entry(entry):
                    memberships.extend(cls._extract_group_memberships(entry))
                    continue
                if cls.user_entry(entry):
                    memberships.extend(cls._extract_user_memberships(entry))
            except c.Meltano.SINGER_SAFE_EXCEPTIONS:
                entry_dn = (
                    str(entry.dn) if entry.dn is not None else c.DEFAULT_EMPTY_STRING
                )
                cls._log.exception(
                    "Failed to transform memberships for entry: %s",
                    entry_dn,
                )
        cls._log.info("Transformed %d membership facts", len(memberships))
        return memberships

    @classmethod
    def transform_users(
        cls,
        entries: t.SequenceOf[m.Ldif.Entry],
    ) -> t.SequenceOf[m.DbtLdap.UserDimension]:
        """Transform LDAP entries into typed user dimensions.

        Returns:
            The resulting ``t.SequenceOf[m.DbtLdap.UserDimension]``.
        """
        users = [entry for entry in entries if cls.user_entry(entry)]
        build = m.DbtLdap.UserDimension.from_ldap_entry
        return cls._transform_entries_to_dimensions(users, build, "user")

    @classmethod
    def _extract_group_memberships(
        cls,
        entry: m.Ldif.Entry,
    ) -> t.SequenceOf[m.DbtLdap.MembershipFact]:
        """Build membership facts from group membership attributes.

        Returns:
            The resulting ``t.SequenceOf[m.DbtLdap.MembershipFact]``.
        """
        memberships: list[m.DbtLdap.MembershipFact] = []
        attrs = ul.Ldap.extract_entry_attributes(entry)
        group_dn = str(entry.dn) if entry.dn is not None else c.DEFAULT_EMPTY_STRING
        for attribute in c.DbtLdap.MEMBERSHIP_ATTRIBUTES:
            members = attrs.get(attribute)
            if not members:
                continue
            memberships.extend(
                m.DbtLdap.MembershipFact(
                    user_dn=member_dn,
                    group_dn=group_dn,
                    membership_type=c.DbtLdap.DIRECT,
                )
                for member_dn in members
            )
        return memberships

    @classmethod
    def _extract_user_memberships(
        cls,
        entry: m.Ldif.Entry,
    ) -> t.SequenceOf[m.DbtLdap.MembershipFact]:
        """Build membership facts from a user entry.

        Returns:
            The resulting ``t.SequenceOf[m.DbtLdap.MembershipFact]``.
        """
        attrs = ul.Ldap.extract_entry_attributes(entry)
        group_dns = attrs.get(c.DbtLdap.MEMBER_OF, [])
        if not group_dns:
            empty: list[m.DbtLdap.MembershipFact] = []
            return empty
        user_dn = str(entry.dn) if entry.dn is not None else c.DEFAULT_EMPTY_STRING
        return [
            m.DbtLdap.MembershipFact(
                user_dn=user_dn,
                group_dn=group_dn,
                membership_type=c.DbtLdap.DIRECT,
            )
            for group_dn in group_dns
        ]

    @classmethod
    def _transform_entries_to_dimensions[DimensionT](
        cls,
        entries: t.SequenceOf[m.Ldif.Entry],
        build_dimension: Callable[[m.Ldif.Entry], DimensionT],
        kind: str,
        /,
    ) -> t.SequenceOf[DimensionT]:
        """Shared entry-to-dimension transformation flow.

        Returns:
            The resulting ``t.SequenceOf[DimensionT]``.
        """
        cls._log.info(
            "Transforming %d LDAP %s entries to dimensions",
            len(entries),
            kind,
        )
        dimensions: list[DimensionT] = []
        for entry in entries:
            try:
                dimensions.append(build_dimension(entry))
            except c.Meltano.SINGER_SAFE_EXCEPTIONS:
                entry_dn = (
                    str(entry.dn) if entry.dn is not None else c.DEFAULT_EMPTY_STRING
                )
                cls._log.exception(
                    "Failed to transform %s entry: %s",
                    kind,
                    entry_dn,
                )
        cls._log.info("Transformed %d %s dimensions", len(dimensions), kind)
        return dimensions


__all__: t.StrSequence = ("FlextDbtLdapUtilitiesIntegration",)
