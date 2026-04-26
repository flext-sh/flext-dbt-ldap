"""Entry normalization helpers for dbt-ldap utilities and models."""

from __future__ import annotations

from collections.abc import (
    Mapping,
    MutableMapping,
)

from flext_ldif import m as lm

from flext_dbt_ldap import FlextDbtLdapUtilitiesMacros, c, t
from flext_meltano import u


class FlextDbtLdapUtilitiesEntry:
    """Low-level LDAP entry helpers reused by models and integrations."""

    _log = u.fetch_logger(__name__)

    @staticmethod
    def ldap_first_attribute(
        attrs: t.DbtLdap.LdapEntryMapping,
        key: str,
        default: str | None = None,
    ) -> str | None:
        """Return the first string value for a LDAP attribute key."""
        values = attrs.get(key)
        if not values:
            return default
        return str(values[0])

    @staticmethod
    def ldap_entry_mapping(entry: lm.Ldif.Entry) -> t.DbtLdap.LdapEntryMapping:
        """Normalize raw LDIF entry attributes into a typed LDAP mapping."""
        raw = entry.attributes
        if raw is None:
            empty: t.DbtLdap.MutableLdapEntryMapping = {}
            return empty
        mapping = raw.attributes if hasattr(raw, "attributes") else raw
        if not isinstance(mapping, Mapping):
            empty: t.DbtLdap.MutableLdapEntryMapping = {}
            return empty
        normalized: MutableMapping[str, t.DbtLdap.LdapAttributeValues] = {}
        for key, values in mapping.items():
            normalized[str(key)] = [str(item) for item in values] if values else []
        return normalized

    @classmethod
    def ldap_object_classes(cls, entry: lm.Ldif.Entry) -> t.StrSequence:
        """Return normalized LDAP object classes for an entry."""
        attrs = cls.ldap_entry_mapping(entry)
        return attrs.get(c.Ldap.LdapAttributeNames.OBJECT_CLASS, [])

    @classmethod
    def is_active_entry(cls, attrs: t.DbtLdap.LdapEntryMapping) -> bool:
        """Return whether the LDAP entry represents an active account."""
        raw_flag = cls.ldap_first_attribute(attrs, c.DbtLdap.USER_ACCOUNT_CONTROL)
        if raw_flag is None:
            return True
        try:
            return FlextDbtLdapUtilitiesMacros.is_user_active(int(raw_flag))
        except c.Meltano.SINGER_SAFE_EXCEPTIONS:
            cls._log.exception(
                "Failed to parse userAccountControl value: %s",
                raw_flag,
            )
            return True

    @classmethod
    def is_group_entry(cls, entry: lm.Ldif.Entry) -> bool:
        """Check whether an entry matches the configured group object classes."""
        object_classes = cls.ldap_object_classes(entry)
        return any(item in object_classes for item in c.DbtLdap.GROUPS_CLASSES)

    @classmethod
    def is_user_entry(cls, entry: lm.Ldif.Entry) -> bool:
        """Check whether an entry matches the configured user object classes."""
        object_classes = cls.ldap_object_classes(entry)
        return any(item in object_classes for item in c.DbtLdap.USERS_CLASSES)
