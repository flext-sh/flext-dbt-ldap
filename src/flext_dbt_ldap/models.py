"""FLEXT dbt LDAP Models - DBT LDAP data transformation models.

All structured data uses Pydantic models. No dict type aliases.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Callable, Mapping, MutableMapping, Sequence
from typing import Annotated, override

from flext_core import FlextLogger, FlextModels, r
from flext_ldap import FlextLdapModels
from flext_meltano import FlextMeltanoModels
from pydantic import Field, TypeAdapter, ValidationError

from flext_dbt_ldap import t

_MAPPING_ADAPTER: TypeAdapter[Mapping[str, t.Serializable]] = TypeAdapter(
    Mapping[str, t.Serializable]
)
_STRING_LIST_ADAPTER = TypeAdapter(Sequence[str])


def _entry_attrs_mapping(
    entry: FlextLdapModels.Ldif.Entry,
) -> Mapping[str, Sequence[str]]:
    """Get Mapping[str, Sequence[str]] from entry.attributes (Attributes or Mapping)."""
    raw = entry.attributes
    if raw is None:
        return {}
    mapping = raw.attributes if hasattr(raw, "attributes") else raw
    try:
        validated_mapping = _MAPPING_ADAPTER.validate_python(mapping)
    except ValidationError:
        return {}
    out: MutableMapping[str, Sequence[str]] = {}
    for k, v in validated_mapping.items():
        try:
            out[k] = _STRING_LIST_ADAPTER.validate_python(v)
        except ValidationError:
            out[k] = [] if v is None else [str(v)]
    return out


class FlextDbtLdapModels(FlextMeltanoModels, FlextLdapModels):
    """Unified DBT LDAP models collection with nested model classes.

    Hierarchy:
        FlextModels (flext-core)
        ├── FlextMeltanoModels (flext-meltano) - Singer/Meltano patterns
        └── FlextLdifModels (flext-ldif)
            └── FlextLdapModels (flext-ldap)
                └── FlextDbtLdapModels (this module)
    """

    # =========================================================================
    # RESULT MODELS
    # =========================================================================

    class ValidationMetrics(FlextModels.Value):
        """Validation metrics for LDAP data quality."""

        total_entries: int = 0
        valid_dns: int = 0
        valid_entries: int = 0
        quality_score: float = 0.0
        validation_passed: bool = False

    class DbtRunStatus(FlextModels.Value):
        """Status of a DBT transformation run."""

        status: str = "pending"
        models_run: Annotated[Sequence[str], Field(default_factory=list)]
        entries_processed: int = 0

    class DbtLdapPipelineResult(FlextModels.Value):
        """Result of a complete LDAP-to-DBT pipeline run."""

        extracted_entries: int = 0

    class SyncResult(FlextModels.Value):
        """Result of full data warehouse sync."""

        overall_success: bool = False
        successful_components: int = 0
        total_components: int = 0

    class PerformanceAnalysis(FlextModels.Value):
        """Performance analysis metrics."""

        execution_time: float = 0.0
        rows_processed: int = 0
        memory_usage: float = 0.0
        recommendations: Annotated[Sequence[str], Field(default_factory=list)]

    class ServiceStatus(FlextModels.Value):
        """Service status and capabilities."""

        status: str = "operational"
        service: str = ""
        capabilities: Annotated[Sequence[str], Field(default_factory=list)]

    class AnalyticsReport(FlextModels.Value):
        """Analytics report data."""

        report_type: str = "summary"
        generated_at: str = ""

    # =========================================================================
    # DBT CONFIGURATION MODELS
    # =========================================================================

    class DbtProjectConfig(FlextModels.Value):
        """DBT project configuration (dbt_project.yml)."""

        name: str
        version: str = "1.0.0"
        profile: str = ""
        model_paths: Annotated[Sequence[str], Field(default_factory=lambda: ["models"])]
        analysis_paths: Annotated[
            Sequence[str], Field(default_factory=lambda: ["analyses"])
        ]
        test_paths: Annotated[Sequence[str], Field(default_factory=lambda: ["tests"])]
        seed_paths: Annotated[Sequence[str], Field(default_factory=lambda: ["seeds"])]
        macro_paths: Annotated[Sequence[str], Field(default_factory=lambda: ["macros"])]
        snapshot_paths: Annotated[
            Sequence[str], Field(default_factory=lambda: ["snapshots"])
        ]
        target_path: str = "target"
        clean_targets: Annotated[
            Sequence[str],
            Field(
                default_factory=lambda: ["target", "dbt_packages"],
            ),
        ]
        target_schema: str = "public"
        tags: Annotated[Sequence[str], Field(default_factory=list)]
        materialized: str = "table"

    class DbtProfileConfig(FlextModels.Value):
        """DBT profile connection configuration."""

        type: str = "postgres"
        host: str = "localhost"
        user: str = "dbt_user"
        password: str = ""
        port: int = 5432
        dbname: str = "ldap_db"
        schema_name: str = "public"
        threads: int = 4

    class DbtSourceTable(FlextModels.Value):
        """DBT source table definition."""

        name: str
        description: str = ""

    class DbtSourceSchema(FlextModels.Value):
        """DBT source schema definition."""

        version: str = "2"
        sources: Annotated[
            Sequence[Mapping[str, t.Serializable]],
            Field(default_factory=list),
        ]

    class DbtModelDefinition(FlextModels.Value):
        """DBT model definition (schema.yml)."""

        version: str = "2"
        models: Annotated[
            Sequence[Mapping[str, t.Serializable]],
            Field(default_factory=list),
        ]

    class DbtTestConfig(FlextModels.Value):
        """DBT test configuration."""

        version: str = "2"
        models: Annotated[
            Sequence[Mapping[str, t.Serializable]],
            Field(default_factory=list),
        ]
        columns: Annotated[Mapping[str, Sequence[str]], Field(default_factory=dict)]

    class DbtSourceFreshness(FlextModels.Value):
        """DBT source freshness configuration."""

        warn_after: Annotated[Mapping[str, int], Field(default_factory=dict)]
        error_after: Annotated[Mapping[str, int], Field(default_factory=dict)]

    class DbtSourceDefinition(FlextModels.Value):
        """Complete DBT source definition."""

        name: str
        description: str = ""
        tables: Annotated[
            Sequence[Mapping[str, t.Serializable]],
            Field(default_factory=list),
        ]

    class DbtConfig(FlextModels.Value):
        """General DBT execution configuration."""

        target: str = "dev"
        profiles_dir: str = ""
        project_dir: str = ""

    class ProjectStructureValidation(FlextModels.Value):
        """DBT project structure validation result."""

        results: Annotated[Mapping[str, bool], Field(default_factory=dict)]

    class OptimizationHints(FlextModels.Value):
        """Query optimization hints."""

        add_indexes: bool = False
        index_columns: Annotated[Sequence[str], Field(default_factory=list)]
        partition_by: str = ""
        filter_early: bool = False

    # =========================================================================
    # TRANSFORMATION MODELS
    # =========================================================================

    class TransformationConfig(FlextModels.Value):
        """Transformation configuration."""

        source_table: str = ""
        transformations: Annotated[Mapping[str, str], Field(default_factory=dict)]
        filters: Annotated[Sequence[str], Field(default_factory=list)]

    class TransformationRule(FlextModels.Value):
        """Transformation rule definition."""

        name: str = ""
        rules: Annotated[Mapping[str, str], Field(default_factory=dict)]

    class DataValidationConfig(FlextModels.Value):
        """Data validation configuration."""

        min_quality_threshold: str = "0.8"
        required_attributes: Annotated[Sequence[str], Field(default_factory=list)]
        validate_dns: bool = True
        columns: Annotated[Mapping[str, Sequence[str]], Field(default_factory=dict)]

    # =========================================================================
    # LDAP MODELS
    # =========================================================================

    class LdapSchema(FlextModels.Value):
        """LDAP schema configuration."""

        object_classes: Annotated[Sequence[str], Field(default_factory=list)]
        required_attributes: Annotated[Sequence[str], Field(default_factory=list)]

    class LdapQuery(FlextModels.Value):
        """LDAP query configuration."""

        base_dn: str = ""
        filter_str: str = "(objectClass=*)"
        attributes: Annotated[Sequence[str], Field(default_factory=list)]
        scope: str = "SUBTREE"

    # =========================================================================
    # DOMAIN MODELS - LDAP data transformation entities
    # =========================================================================

    class UserDimension(FlextModels.Entity):
        """User dimension model for DBT LDAP transformations."""

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
            entry: FlextLdapModels.Ldif.Entry,
        ) -> FlextDbtLdapModels.UserDimension:
            """Create user dimension from LDAP entry."""
            attrs = FlextDbtLdapModels.DbtLdap.normalize_attributes(entry)
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

        def to_dbt_dict(self) -> Mapping[str, t.Scalar]:
            """Convert to dictionary suitable for DBT processing."""
            return {
                "user_id": self.user_id,
                "common_name": self.common_name,
                "email": self.email or "",
                "display_name": self.display_name or "",
                "department": self.department or "",
                "manager_dn": self.manager_dn or "",
                "employee_number": self.employee_number or "",
                "phone": self.phone or "",
                "is_active": self.is_active,
                "created_date": self.created_date or "",
                "modified_date": self.modified_date or "",
            }

        def validate_business_rules(self) -> r[bool]:
            """Validate user dimension business rules."""
            if not self.user_id or not self.common_name:
                return r[bool].fail("User ID and common name are required")
            return r[bool].ok(value=True)

    class GroupDimension(FlextModels.Entity):
        """Group dimension model for DBT LDAP transformations."""

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
            entry: FlextLdapModels.Ldif.Entry,
        ) -> FlextDbtLdapModels.GroupDimension:
            """Create group dimension from LDAP entry."""
            attrs = FlextDbtLdapModels.DbtLdap.normalize_attributes(entry)
            member_count = len(attrs.get("member", [])) + len(
                attrs.get("uniqueMember", []),
            )
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
                is_active=True,
                created_date=attrs.get("createTimestamp", [None])[0]
                if "createTimestamp" in attrs
                else None,
                modified_date=attrs.get("modifyTimestamp", [None])[0]
                if "modifyTimestamp" in attrs
                else None,
            )

        def to_dbt_dict(self) -> Mapping[str, t.Scalar]:
            """Convert to dictionary suitable for DBT processing."""
            return {
                "group_id": self.group_id,
                "common_name": self.common_name,
                "description": self.description or "",
                "group_type": self.group_type or "",
                "member_count": self.member_count,
                "is_active": self.is_active,
                "created_date": self.created_date or "",
                "modified_date": self.modified_date or "",
            }

        def validate_business_rules(self) -> r[bool]:
            """Validate group dimension business rules."""
            if not self.group_id or not self.common_name:
                return r[bool].fail("Group ID and common name are required")
            if self.member_count < 0:
                return r[bool].fail("Member count cannot be negative")
            return r[bool].ok(value=True)

    class MembershipFact(FlextModels.Entity):
        """Membership fact model for DBT LDAP transformations."""

        user_dn: str
        group_dn: str
        membership_type: str = "direct"
        is_primary: bool = False
        effective_date: str | None = None
        expiry_date: str | None = None

        def to_dbt_dict(self) -> Mapping[str, t.Scalar]:
            """Convert to dictionary suitable for DBT processing."""
            return {
                "user_dn": self.user_dn,
                "group_dn": self.group_dn,
                "membership_type": self.membership_type,
                "is_primary": self.is_primary,
                "effective_date": self.effective_date or "",
                "expiry_date": self.expiry_date or "",
            }

        def validate_business_rules(self) -> r[bool]:
            """Validate membership fact business rules."""
            if not self.user_dn or not self.group_dn:
                return r[bool].fail("User DN and Group DN are required")
            return r[bool].ok(value=True)

    # =========================================================================
    # TRANSFORMER - LDAP to DBT data transformation
    # =========================================================================

    class DbtLdap:
        """LDAP data transformer for DBT operations."""

        @override
        def __init__(self) -> None:
            """Initialize LDAP transformer."""
            super().__init__()
            self._logger_instance: FlextLogger | None = None

        @property
        def logger(self) -> FlextLogger:
            """Lazy logger via FlextLogger."""
            if self._logger_instance is None:
                self._logger_instance = FlextLogger(__name__)
            return self._logger_instance

        @staticmethod
        def _get_object_classes(entry: FlextLdapModels.Ldif.Entry) -> Sequence[str]:
            """Extract t.NormalizedValue classes from entry attributes."""
            raw = _entry_attrs_mapping(entry)
            oc_val = raw.get("objectClass", [])
            try:
                return _STRING_LIST_ADAPTER.validate_python(oc_val)
            except ValidationError:
                return [str(oc_val)]

        @staticmethod
        def normalize_attributes(
            entry: FlextLdapModels.Ldif.Entry,
        ) -> Mapping[str, Sequence[str]]:
            """Normalize entry attributes to Mapping[str, Sequence[str]]."""
            return _entry_attrs_mapping(entry)

        def transform_groups(
            self,
            entries: Sequence[FlextLdapModels.Ldif.Entry],
        ) -> Sequence[FlextDbtLdapModels.GroupDimension]:
            """Transform LDAP entries to group dimensions."""
            return self._transform_entries_to_dimensions(
                entries=entries,
                is_entry_target=self._is_group_entry,
                build_dimension=FlextDbtLdapModels.GroupDimension.from_ldap_entry,
                transform_label="group dimensions",
                failure_label="group entry",
            )

        def transform_memberships(
            self,
            entries: Sequence[FlextLdapModels.Ldif.Entry],
        ) -> Sequence[FlextDbtLdapModels.MembershipFact]:
            """Transform LDAP entries to membership facts."""
            self.logger.info(
                f"Transforming {len(entries)} LDAP entries to membership facts"
            )
            membership_facts: list[FlextDbtLdapModels.MembershipFact] = []
            for entry in entries:
                try:
                    if self._is_group_entry(entry):
                        membership_facts.extend(
                            self._extract_group_memberships(entry),
                        )
                    elif self._is_user_entry(entry):
                        membership_facts.extend(
                            self._extract_user_memberships(entry),
                        )
                except (
                    ValueError,
                    TypeError,
                    KeyError,
                    AttributeError,
                    OSError,
                    RuntimeError,
                    ImportError,
                ):
                    self.logger.exception(
                        "Failed to transform memberships for entry: "
                        f"{str(entry.dn) if entry.dn is not None else ''}"
                    )
            self.logger.info(f"Transformed {len(membership_facts)} membership facts")
            return membership_facts

        def transform_users(
            self,
            entries: Sequence[FlextLdapModels.Ldif.Entry],
        ) -> Sequence[FlextDbtLdapModels.UserDimension]:
            """Transform LDAP entries to user dimensions."""
            return self._transform_entries_to_dimensions(
                entries=entries,
                is_entry_target=self._is_user_entry,
                build_dimension=FlextDbtLdapModels.UserDimension.from_ldap_entry,
                transform_label="user dimensions",
                failure_label="user entry",
            )

        def _transform_entries_to_dimensions[TDimension](
            self,
            *,
            entries: Sequence[FlextLdapModels.Ldif.Entry],
            is_entry_target: Callable[[FlextLdapModels.Ldif.Entry], bool],
            build_dimension: Callable[[FlextLdapModels.Ldif.Entry], TDimension],
            transform_label: str,
            failure_label: str,
        ) -> Sequence[TDimension]:
            self.logger.info(
                f"Transforming {len(entries)} LDAP entries to {transform_label}"
            )
            dimensions: list[TDimension] = []
            for entry in entries:
                if not is_entry_target(entry):
                    continue
                try:
                    dimensions.append(build_dimension(entry))
                except (
                    ValueError,
                    TypeError,
                    KeyError,
                    AttributeError,
                    OSError,
                    RuntimeError,
                    ImportError,
                ):
                    entry_dn = str(entry.dn) if entry.dn is not None else ""
                    self.logger.exception(
                        f"Failed to transform {failure_label}: {entry_dn}"
                    )
            self.logger.info(f"Transformed {len(dimensions)} {transform_label}")
            return dimensions

        def _extract_group_memberships(
            self,
            group_entry: FlextLdapModels.Ldif.Entry,
        ) -> Sequence[FlextDbtLdapModels.MembershipFact]:
            """Extract memberships from a group entry."""
            memberships: list[FlextDbtLdapModels.MembershipFact] = []
            attrs = self.normalize_attributes(group_entry)
            group_dn = str(group_entry.dn) if group_entry.dn is not None else ""
            for attr in ("member", "uniqueMember", "memberUid"):
                if attr in attrs:
                    memberships.extend(
                        FlextDbtLdapModels.MembershipFact(
                            user_dn=member_dn,
                            group_dn=group_dn,
                            membership_type="direct",
                        )
                        for member_dn in attrs[attr]
                    )
            return memberships

        def _extract_user_memberships(
            self,
            user_entry: FlextLdapModels.Ldif.Entry,
        ) -> Sequence[FlextDbtLdapModels.MembershipFact]:
            """Extract memberships from a user entry."""
            memberships: list[FlextDbtLdapModels.MembershipFact] = []
            attrs = self.normalize_attributes(user_entry)
            user_dn = str(user_entry.dn) if user_entry.dn is not None else ""
            if "memberOf" in attrs:
                memberships.extend(
                    FlextDbtLdapModels.MembershipFact(
                        user_dn=user_dn,
                        group_dn=group_dn,
                        membership_type="direct",
                    )
                    for group_dn in attrs["memberOf"]
                )
            return memberships

        def _is_group_entry(self, entry: FlextLdapModels.Ldif.Entry) -> bool:
            """Check if entry is a group entry."""
            object_classes = self._get_object_classes(entry)
            group_classes = [
                "group",
                "groupOfNames",
                "groupOfUniqueNames",
                "posixGroup",
            ]
            return any(cls in object_classes for cls in group_classes)

        def _is_user_entry(self, entry: FlextLdapModels.Ldif.Entry) -> bool:
            """Check if entry is a user entry."""
            object_classes = self._get_object_classes(entry)
            user_classes = [
                "person",
                "user",
                "inetOrgPerson",
                "organizationalPerson",
            ]
            return any(cls in object_classes for cls in user_classes)

        def _post_init_log(self) -> None:
            self.logger.info("Initialized LDAP DBT transformer")


# Short aliases

__all__: Sequence[str] = [
    "FlextDbtLdapModels",
    "m",
]

m = FlextDbtLdapModels
