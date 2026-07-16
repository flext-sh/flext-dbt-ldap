"""FLEXT DBT LDAP Utilities — LDAP integration for DBT.

Absorbed from ldap_integration.py into u.DbtLdap namespace.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import (
    Callable,
)

from flext_dbt_ldap import c, m, p, t
from flext_dbt_ldap._utilities.entry import FlextDbtLdapUtilitiesEntry
from flext_ldap import FlextLdapUtilities as ul
from flext_meltano import u


class FlextDbtLdapUtilitiesIntegration(FlextDbtLdapUtilitiesEntry):
    """Typed LDAP-to-DBT transformation helpers."""

    _log = u.fetch_logger(__name__)

    def transform_groups(
        self,
        entries: t.SequenceOf[p.Ldif.Entry],
    ) -> t.SequenceOf[p.DbtLdap.GroupDimension]:
        """Transform LDAP entries into typed group dimensions."""
        return self._transform_entries_to_dimensions(
            entries=entries,
            is_entry_target=self.is_group_entry,
            build_dimension=m.DbtLdap.GroupDimension.from_ldap_entry,
            transform_label="group dimensions",
            failure_label="group entry",
        )

    def transform_memberships(
        self,
        entries: t.SequenceOf[p.Ldif.Entry],
    ) -> t.SequenceOf[p.DbtLdap.MembershipFact]:
        """Transform LDAP entries into membership facts."""
        self._log.info(
            "Transforming %d LDAP entries to membership facts",
            len(entries),
        )
        memberships: list[p.DbtLdap.MembershipFact] = []
        for entry in entries:
            try:
                if self.is_group_entry(entry):
                    memberships.extend(self._extract_group_memberships(entry))
                    continue
                if self.is_user_entry(entry):
                    memberships.extend(self._extract_user_memberships(entry))
            except c.Meltano.SINGER_SAFE_EXCEPTIONS:
                entry_dn = (
                    str(entry.dn) if entry.dn is not None else c.DEFAULT_EMPTY_STRING
                )
                self._log.exception(
                    "Failed to transform memberships for entry: %s",
                    entry_dn,
                )
        self._log.info("Transformed %d membership facts", len(memberships))
        return memberships

    def transform_users(
        self,
        entries: t.SequenceOf[p.Ldif.Entry],
    ) -> t.SequenceOf[p.DbtLdap.UserDimension]:
        """Transform LDAP entries into typed user dimensions."""
        return self._transform_entries_to_dimensions(
            entries=entries,
            is_entry_target=self.is_user_entry,
            build_dimension=m.DbtLdap.UserDimension.from_ldap_entry,
            transform_label="user dimensions",
            failure_label="user entry",
        )

    def _extract_group_memberships(
        self,
        entry: p.Ldif.Entry,
    ) -> t.SequenceOf[p.DbtLdap.MembershipFact]:
        """Build membership facts from group membership attributes."""
        memberships: list[p.DbtLdap.MembershipFact] = []
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

    def _extract_user_memberships(
        self,
        entry: p.Ldif.Entry,
    ) -> t.SequenceOf[p.DbtLdap.MembershipFact]:
        """Build membership facts from a user entry."""
        attrs = ul.Ldap.extract_entry_attributes(entry)
        group_dns = attrs.get(c.DbtLdap.MEMBER_OF, [])
        if not group_dns:
            empty: list[p.DbtLdap.MembershipFact] = []
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

    def _transform_entries_to_dimensions[DimensionT](
        self,
        *,
        entries: t.SequenceOf[p.Ldif.Entry],
        is_entry_target: Callable[[p.Ldif.Entry], bool],
        build_dimension: Callable[[p.Ldif.Entry], DimensionT],
        transform_label: str,
        failure_label: str,
    ) -> t.SequenceOf[DimensionT]:
        """Shared entry-to-dimension transformation flow."""
        self._log.info(
            "Transforming %d LDAP entries to %s",
            len(entries),
            transform_label,
        )
        dimensions: list[DimensionT] = []
        for entry in entries:
            if not is_entry_target(entry):
                continue
            try:
                dimensions.append(build_dimension(entry))
            except c.Meltano.SINGER_SAFE_EXCEPTIONS:
                entry_dn = (
                    str(entry.dn) if entry.dn is not None else c.DEFAULT_EMPTY_STRING
                )
                self._log.exception(
                    "Failed to transform %s: %s",
                    failure_label,
                    entry_dn,
                )
        self._log.info("Transformed %d %s", len(dimensions), transform_label)
        return dimensions


__all__: t.StrSequence = ("FlextDbtLdapUtilitiesIntegration",)
