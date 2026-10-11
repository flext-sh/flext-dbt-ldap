"""FLEXT DBT LDAP settings — namespaced under ``settings.DbtLdap``.

Universal fields via MRO; project fields in the ``DbtLdap`` group with simple
scalar types (env-settable).

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Annotated

# NOTE (multi-agent): mro-rn88 — inherit FlextLdapSettings so LDAP connection scalars
# come from settings.Ldap.* (SSOT); FlextMeltanoSettings adds the dbt/meltano surface.
from flext_ldap import FlextLdapSettings
from flext_meltano import FlextMeltanoSettings, m


def _empty_list_str() -> list[str]:
    return []


def _empty_dict_str_str() -> dict[str, str]:
    return {}


class FlextDbtLdapSettings(FlextLdapSettings, FlextMeltanoSettings):
    """DBT LDAP settings; connection via ``Ldap.*``, dbt knobs via ``DbtLdap.*``."""

    model_config = m.SettingsConfigDict(
        env_prefix="FLEXT_DBT_LDAP_",
        env_nested_delimiter="__",
        extra="ignore",
    )

    class _DbtLdap(m.BaseModel):
        """dbt-LDAP knobs only (LDAP connection lives in ``Ldap``)."""

        ldap_base_dn: Annotated[str, m.Field(description="LDAP base DN")] = (
            "dc=example,dc=com"
        )
        dbt_project_dir: Annotated[
            str, m.Field(description="Path to DBT project directory")
        ] = "."
        min_quality_threshold: Annotated[
            float,
            m.Field(
                ge=0.0,
                le=1.0,
                description="Minimum data quality score threshold",
            ),
        ] = 0.8
        required_attributes: Annotated[
            list[str],
            m.Field(
                description="Required LDAP attributes for validation",
            ),
        ] = m.Field(default_factory=_empty_list_str)
        ldap_attribute_mapping: Annotated[
            dict[str, str],
            m.Field(
                description="Mapping of LDAP attributes to DBT model attributes",
            ),
        ] = m.Field(default_factory=_empty_dict_str_str)
        ldap_schema_mapping: Annotated[
            dict[str, str],
            m.Field(
                description="Mapping of LDAP schemas to DBT tables",
            ),
        ] = m.Field(default_factory=_empty_dict_str_str)

    if TYPE_CHECKING:
        DbtLdap: _DbtLdap
    else:
        DbtLdap: _DbtLdap = m.Field(
            default_factory=_DbtLdap,
            description="Namespaced dbt-LDAP settings.",
        )


settings: FlextDbtLdapSettings = FlextDbtLdapSettings.fetch_global()
"""Pre-instantiated settings singleton — ``from flext_dbt_ldap import settings``."""

__all__: list[str] = ["FlextDbtLdapSettings", "settings"]
