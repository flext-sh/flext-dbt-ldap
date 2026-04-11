"""Shared dbt-ldap model mixins and internal base classes."""

from __future__ import annotations

from typing import Annotated

from pydantic import Field

from flext_dbt_ldap import c, t
from flext_meltano import FlextMeltanoModels


class FlextDbtLdapModelsShared:
    """Shared internal model bases reused across dbt-ldap model mixins."""

    class DbtSerializable(FlextMeltanoModels.Entity):
        """Base for DBT-serializable models."""

        def to_dbt_dict(self) -> t.ConfigurationMapping:
            """Dump models to DBT-friendly dictionaries."""
            dumped = self.model_dump()
            return {
                key: value if value is not None else c.DEFAULT_EMPTY_STRING
                for key, value in dumped.items()
            }

    class DbtDimensionBase(DbtSerializable):
        """Shared fields for directory-backed dimension models."""

        common_name: Annotated[str, Field(description="Canonical common name")]
        is_active: Annotated[
            bool,
            Field(description="Whether the directory record is active"),
        ] = True
        created_date: Annotated[
            str | None,
            Field(default=None, description="Source creation timestamp"),
        ] = None
        modified_date: Annotated[
            str | None,
            Field(default=None, description="Source modification timestamp"),
        ] = None
