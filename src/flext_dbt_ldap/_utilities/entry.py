"""Entry normalization helpers for dbt-ldap utilities and models."""

from __future__ import annotations

from flext_ldif import m as lm

from flext_dbt_ldap import FlextDbtLdapUtilitiesMacros, c, t
from flext_ldap import FlextLdapUtilities as ul
from flext_meltano import u


class FlextDbtLdapUtilitiesEntry:
    """Low-level LDAP entry helpers reused by models and integrations."""

    _log = u.fetch_logger(__name__)

    @classmethod
    def is_active_entry(cls, attrs: t.Ldap.OperationAttributes) -> bool:
        """Return whether the LDAP entry represents an active account."""
        raw_flag = ul.Ldap.get_first_attribute_value(
            attrs,
            c.DbtLdap.USER_ACCOUNT_CONTROL,
        )
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
        object_classes = ul.Ldap.extract_entry_attributes(entry).get(
            c.Ldap.AttributeName.OBJECT_CLASS,
            [],
        )
        return any(
            ul.Ldap.norm_in(item, object_classes) for item in c.DbtLdap.GROUPS_CLASSES
        )

    @classmethod
    def is_user_entry(cls, entry: lm.Ldif.Entry) -> bool:
        """Check whether an entry matches the configured user object classes."""
        object_classes = ul.Ldap.extract_entry_attributes(entry).get(
            c.Ldap.AttributeName.OBJECT_CLASS,
            [],
        )
        return any(
            ul.Ldap.norm_in(item, object_classes) for item in c.DbtLdap.USERS_CLASSES
        )
