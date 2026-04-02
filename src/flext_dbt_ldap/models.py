"""FLEXT dbt LDAP Models - DBT LDAP data transformation models.

All structured data uses Pydantic models. No dict type aliases.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Callable, Mapping, MutableMapping, MutableSequence, Sequence

from pydantic import Field, model_validator

from flext_core import FlextLogger
from flext_dbt_ldap import c, t
from flext_ldap import FlextLdapModels
from flext_meltano import FlextMeltanoModels

logger = FlextLogger(__name__)


class FlextDbtLdapModels(FlextMeltanoModels, FlextLdapModels):
    """Unified DBT LDAP models collection with nested model classes.

    Hierarchy:
        FlextModels (flext-core)
        ├── FlextMeltanoModels (flext-meltano) - Singer/Meltano patterns
        └── FlextLdifModels (flext-ldif)
            └── FlextLdapModels (flext-ldap)
                └── FlextDbtLdapModels (this module)
    """

    @staticmethod
    def _get_attr(
        attrs: t.DbtLdap.LdapEntryMapping,
        key: str,
        default: str | None = None,
    ) -> str | None:
        """Extract first value from multi-valued LDAP attribute.

        Single helper replaces the repetitive
        ``attrs.get("X", [None])[0] if "X" in attrs else None`` pattern.
        """
        values = attrs.get(key)
        if values:
            return str(values[0])
        return default

    @staticmethod
    def _entry_attrs_mapping(
        entry: m.Ldif.Entry,
    ) -> t.DbtLdap.LdapEntryMapping:
        """Get t.DbtLdap.LdapEntryMapping from entry.attributes."""
        raw = entry.attributes
        if raw is None:
            return {}
        mapping = raw.attributes if hasattr(raw, "attributes") else raw
        if not isinstance(mapping, Mapping):
            return {}
        out: MutableMapping[str, t.StrSequence] = {}
        for k, values in mapping.items():
            out[str(k)] = [str(item) for item in values] if values else []
        return out

    class DbtLdap:
        """LDAP data transformer for DBT operations."""

        # =========================================================================
        # RESULT MODELS
        # =========================================================================

        class ValidationMetrics(FlextMeltanoModels.Value):
            """Validation metrics for LDAP data quality."""

            total_entries: int = 0
            valid_dns: int = 0
            valid_entries: int = 0
            quality_score: float = 0.0
            validation_passed: bool = False

        class DbtRunStatus(FlextMeltanoModels.Value):
            """Status of a DBT transformation run."""

            status: str = c.DbtLdap.Statuses.PENDING
            models_run: t.StrSequence = Field(default_factory=list)
            entries_processed: int = 0

        class DbtLdapPipelineResult(FlextMeltanoModels.Value):
            """Result of a complete LDAP-to-DBT pipeline run."""

            extracted_entries: int = 0

        class SyncResult(FlextMeltanoModels.Value):
            """Result of full data warehouse sync."""

            overall_success: bool = False
            successful_components: int = 0
            total_components: int = 0

        class PerformanceAnalysis(FlextMeltanoModels.Value):
            """Performance analysis metrics."""

            execution_time: float = 0.0
            rows_processed: int = 0
            memory_usage: float = 0.0
            recommendations: t.StrSequence = Field(default_factory=list)

        class ServiceStatus(FlextMeltanoModels.Value):
            """Service status and capabilities."""

            status: str = c.DbtLdap.Statuses.OPERATIONAL
            service: str = ""
            capabilities: t.StrSequence = Field(default_factory=list)

        class AnalyticsReport(FlextMeltanoModels.Value):
            """Analytics report data."""

            report_type: str = "summary"
            generated_at: str = ""

        # =========================================================================
        # DBT CONFIGURATION MODELS
        # =========================================================================

        class DbtProjectConfig(FlextMeltanoModels.Value):
            """DBT project configuration (dbt_project.yml)."""

            name: str
            version: str = "1.0.0"
            profile: str = ""
            model_paths: t.StrSequence = Field(default_factory=lambda: ["models"])
            analysis_paths: t.StrSequence = Field(default_factory=lambda: ["analyses"])
            test_paths: t.StrSequence = Field(default_factory=lambda: ["tests"])
            seed_paths: t.StrSequence = Field(default_factory=lambda: ["seeds"])
            macro_paths: t.StrSequence = Field(default_factory=lambda: ["macros"])
            snapshot_paths: t.StrSequence = Field(default_factory=lambda: ["snapshots"])
            target_path: str = "target"
            clean_targets: t.StrSequence = Field(
                default_factory=lambda: ["target", "dbt_packages"]
            )
            target_schema: str = "public"
            tags: t.StrSequence = Field(default_factory=list)
            materialized: str = "table"

        class DbtProfileConfig(FlextMeltanoModels.Value):
            """DBT profile connection configuration."""

            type: str = "postgres"
            host: str = "localhost"
            user: str = "dbt_user"
            password: str = ""
            port: int = 5432
            dbname: str = "ldap_db"
            schema_name: str = "public"
            threads: int = 4

        class DbtSourceTable(FlextMeltanoModels.Value):
            """DBT source table definition."""

            name: str
            description: str = ""

        class DbtSourceSchema(FlextMeltanoModels.Value):
            """DBT source schema definition."""

            version: str = "2"
            sources: Sequence[Mapping[str, t.Serializable]] = Field(
                default_factory=lambda: list[Mapping[str, t.Serializable]]()
            )

        class DbtModelDefinition(FlextMeltanoModels.Value):
            """DBT model definition (schema.yml)."""

            version: str = "2"
            models: Sequence[Mapping[str, t.Serializable]] = Field(
                default_factory=lambda: list[Mapping[str, t.Serializable]]()
            )

        class DbtTestConfig(FlextMeltanoModels.Value):
            """DBT test configuration."""

            version: str = "2"
            models: Sequence[Mapping[str, t.Serializable]] = Field(
                default_factory=lambda: list[Mapping[str, t.Serializable]]()
            )
            columns: t.DbtLdap.LdapEntryMapping = Field(default_factory=dict)

        class DbtSourceFreshness(FlextMeltanoModels.Value):
            """DBT source freshness configuration."""

            warn_after: t.IntMapping = Field(default_factory=dict)
            error_after: t.IntMapping = Field(default_factory=dict)

        class DbtSourceDefinition(FlextMeltanoModels.Value):
            """Complete DBT source definition."""

            name: str
            description: str = ""
            tables: Sequence[Mapping[str, t.Serializable]] = Field(
                default_factory=lambda: list[Mapping[str, t.Serializable]]()
            )

        class DbtConfig(FlextMeltanoModels.Value):
            """General DBT execution configuration."""

            target: str = "dev"
            profiles_dir: str = ""
            project_dir: str = ""

        class ProjectStructureValidation(FlextMeltanoModels.Value):
            """DBT project structure validation result."""

            results: t.BoolMapping = Field(default_factory=dict)

        class OptimizationHints(FlextMeltanoModels.Value):
            """Query optimization hints."""

            add_indexes: bool = False
            index_columns: t.StrSequence = Field(default_factory=list)
            partition_by: str = ""
            filter_early: bool = False

        # =========================================================================
        # TRANSFORMATION MODELS
        # =========================================================================

        class TransformationConfig(FlextMeltanoModels.Value):
            """Transformation configuration."""

            source_table: str = ""
            transformations: t.StrMapping = Field(default_factory=dict)
            filters: t.StrSequence = Field(default_factory=list)

        class TransformationRule(FlextMeltanoModels.Value):
            """Transformation rule definition."""

            name: str = ""
            rules: t.StrMapping = Field(default_factory=dict)

        class DataValidationConfig(FlextMeltanoModels.Value):
            """Data validation configuration."""

            min_quality_threshold: str = "0.8"
            required_attributes: t.StrSequence = Field(default_factory=list)
            validate_dns: bool = True
            columns: t.DbtLdap.LdapEntryMapping = Field(default_factory=dict)

        # =========================================================================
        # LDAP MODELS
        # =========================================================================

        class LdapSchema(FlextMeltanoModels.Value):
            """LDAP schema configuration."""

            object_classes: t.StrSequence = Field(default_factory=list)
            required_attributes: t.StrSequence = Field(default_factory=list)

        class LdapQuery(FlextMeltanoModels.Value):
            """LDAP query configuration."""

            base_dn: str = ""
            filter_str: str = c.DbtLdap.Filters.DEFAULT
            attributes: t.StrSequence = Field(default_factory=list)
            scope: str = "SUBTREE"

        # =========================================================================
        # DOMAIN MODEL MRO CHAIN
        # =========================================================================

        class _DbtSerializable(FlextMeltanoModels.Entity):
            """Base for all DBT-serializable models — DRY to_dbt_dict."""

            def to_dbt_dict(self) -> t.ConfigurationMapping:
                """Convert to DBT dict — None values become empty strings."""
                data = self.model_dump()
                return {k: v if v is not None else "" for k, v in data.items()}

        class _DbtDimensionBase(_DbtSerializable):
            """Shared fields for dimension models (users, groups)."""

            common_name: str
            is_active: bool = True
            created_date: str | None = None
            modified_date: str | None = None

        class UserDimension(_DbtDimensionBase):
            """User dimension — validated at construction via model_validator."""

            user_id: str
            email: str | None = None
            display_name: str | None = None
            department: str | None = None
            manager_dn: str | None = None
            employee_number: str | None = None
            phone: str | None = None

            @model_validator(mode="after")
            def _check_required_fields(
                self,
            ) -> m.DbtLdap.UserDimension:
                """Validate user dimension business rules at construction."""
                if not self.user_id or not self.common_name:
                    msg = "User ID and common name are required"
                    raise ValueError(msg)
                return self

            @classmethod
            def from_ldap_entry(
                cls,
                entry: m.Ldif.Entry,
            ) -> m.DbtLdap.UserDimension:
                """Create user dimension from LDAP entry."""
                attrs = FlextDbtLdapModels._entry_attrs_mapping(entry)
                get_attr = FlextDbtLdapModels._get_attr
                la = c.DbtLdap.LdapAttributes
                return cls(
                    user_id=get_attr(attrs, la.UID, "") or "",
                    common_name=get_attr(attrs, la.CN, "") or "",
                    email=get_attr(attrs, la.MAIL),
                    display_name=get_attr(attrs, la.DISPLAY_NAME),
                    department=get_attr(attrs, la.DEPARTMENT),
                    manager_dn=get_attr(attrs, la.MANAGER),
                    employee_number=get_attr(attrs, la.EMPLOYEE_NUMBER),
                    phone=get_attr(attrs, la.TELEPHONE_NUMBER),
                    is_active=not (
                        la.USER_ACCOUNT_CONTROL in attrs
                        and "2" in str(attrs[la.USER_ACCOUNT_CONTROL][0])
                    ),
                    created_date=get_attr(attrs, la.CREATE_TIMESTAMP),
                    modified_date=get_attr(attrs, la.MODIFY_TIMESTAMP),
                )

        class GroupDimension(_DbtDimensionBase):
            """Group dimension — validated at construction via model_validator."""

            group_id: str
            description: str | None = None
            group_type: str | None = None
            member_count: int = 0

            @model_validator(mode="after")
            def _check_required_fields(
                self,
            ) -> m.DbtLdap.GroupDimension:
                """Validate group dimension business rules at construction."""
                if not self.group_id or not self.common_name:
                    msg = "Group ID and common name are required"
                    raise ValueError(msg)
                if self.member_count < 0:
                    msg = "Member count cannot be negative"
                    raise ValueError(msg)
                return self

            @classmethod
            def from_ldap_entry(
                cls,
                entry: m.Ldif.Entry,
            ) -> m.DbtLdap.GroupDimension:
                """Create group dimension from LDAP entry."""
                attrs = FlextDbtLdapModels._entry_attrs_mapping(entry)
                get_attr = FlextDbtLdapModels._get_attr
                la = c.DbtLdap.LdapAttributes
                member_count = len(attrs.get(la.MEMBER, [])) + len(
                    attrs.get(la.UNIQUE_MEMBER, []),
                )
                return cls(
                    group_id=get_attr(attrs, la.CN, "") or "",
                    common_name=get_attr(attrs, la.CN, "") or "",
                    description=get_attr(attrs, la.DESCRIPTION),
                    group_type=get_attr(attrs, la.GROUP_TYPE),
                    member_count=member_count,
                    is_active=True,
                    created_date=get_attr(attrs, la.CREATE_TIMESTAMP),
                    modified_date=get_attr(attrs, la.MODIFY_TIMESTAMP),
                )

        class MembershipFact(_DbtSerializable):
            """Membership fact — validated at construction via model_validator."""

            user_dn: str
            group_dn: str
            membership_type: str = c.DbtLdap.MembershipTypes.DIRECT
            is_primary: bool = False
            effective_date: str | None = None
            expiry_date: str | None = None

            @model_validator(mode="after")
            def _check_required_fields(
                self,
            ) -> m.DbtLdap.MembershipFact:
                """Validate membership fact business rules at construction."""
                if not self.user_dn or not self.group_dn:
                    msg = "User DN and Group DN are required"
                    raise ValueError(msg)
                return self

        # =========================================================================
        # TRANSFORMER METHODS (use module-level logger, no instance state)
        # =========================================================================

        @staticmethod
        def get_object_classes(entry: m.Ldif.Entry) -> t.StrSequence:
            """Extract object classes from entry attributes."""
            raw = FlextDbtLdapModels._entry_attrs_mapping(entry)
            return raw.get(c.DbtLdap.LdapAttributes.OBJECT_CLASS, [])

        @staticmethod
        def normalize_attributes(
            entry: m.Ldif.Entry,
        ) -> t.DbtLdap.LdapEntryMapping:
            """Normalize entry attributes to t.DbtLdap.LdapEntryMapping."""
            return FlextDbtLdapModels._entry_attrs_mapping(entry)

        def transform_groups(
            self,
            entries: Sequence[m.Ldif.Entry],
        ) -> Sequence[m.DbtLdap.GroupDimension]:
            """Transform LDAP entries to group dimensions."""
            return self._transform_entries_to_dimensions(
                entries=entries,
                is_entry_target=self._is_group_entry,
                build_dimension=m.DbtLdap.GroupDimension.from_ldap_entry,
                transform_label="group dimensions",
                failure_label="group entry",
            )

        def transform_memberships(
            self,
            entries: Sequence[m.Ldif.Entry],
        ) -> Sequence[m.DbtLdap.MembershipFact]:
            """Transform LDAP entries to membership facts."""
            logger.info(
                f"Transforming {len(entries)} LDAP entries to membership facts",
            )
            membership_facts: MutableSequence[m.DbtLdap.MembershipFact] = []
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
                except c.Meltano.Singer.SAFE_EXCEPTIONS:
                    logger.exception(
                        "Failed to transform memberships for entry: "
                        f"{str(entry.dn) if entry.dn is not None else ''}",
                    )
            logger.info("Transformed %d membership facts", len(membership_facts))
            return membership_facts

        def transform_users(
            self,
            entries: Sequence[m.Ldif.Entry],
        ) -> Sequence[m.DbtLdap.UserDimension]:
            """Transform LDAP entries to user dimensions."""
            return self._transform_entries_to_dimensions(
                entries=entries,
                is_entry_target=self._is_user_entry,
                build_dimension=m.DbtLdap.UserDimension.from_ldap_entry,
                transform_label="user dimensions",
                failure_label="user entry",
            )

        def _transform_entries_to_dimensions[TDimension](
            self,
            *,
            entries: Sequence[m.Ldif.Entry],
            is_entry_target: Callable[[m.Ldif.Entry], bool],
            build_dimension: Callable[[m.Ldif.Entry], TDimension],
            transform_label: str,
            failure_label: str,
        ) -> Sequence[TDimension]:
            logger.info(
                f"Transforming {len(entries)} LDAP entries to {transform_label}",
            )
            dimensions: MutableSequence[TDimension] = []
            for entry in entries:
                if not is_entry_target(entry):
                    continue
                try:
                    dimensions.append(build_dimension(entry))
                except c.Meltano.Singer.SAFE_EXCEPTIONS:
                    entry_dn = str(entry.dn) if entry.dn is not None else ""
                    logger.exception(
                        "Failed to transform %s: %s",
                        failure_label,
                        entry_dn,
                    )
            logger.info("Transformed %d %s", len(dimensions), transform_label)
            return dimensions

        def _extract_group_memberships(
            self,
            group_entry: m.Ldif.Entry,
        ) -> Sequence[m.DbtLdap.MembershipFact]:
            """Extract memberships from a group entry."""
            memberships: MutableSequence[m.DbtLdap.MembershipFact] = []
            attrs = self.normalize_attributes(group_entry)
            group_dn = str(group_entry.dn) if group_entry.dn is not None else ""
            for attr in c.DbtLdap.LdapAttributes.MEMBERSHIP_ATTRIBUTES:
                if attr in attrs:
                    memberships.extend(
                        m.DbtLdap.MembershipFact(
                            user_dn=member_dn,
                            group_dn=group_dn,
                            membership_type=c.DbtLdap.MembershipTypes.DIRECT,
                        )
                        for member_dn in attrs[attr]
                    )
            return memberships

        def _extract_user_memberships(
            self,
            user_entry: m.Ldif.Entry,
        ) -> Sequence[m.DbtLdap.MembershipFact]:
            """Extract memberships from a user entry."""
            memberships: MutableSequence[m.DbtLdap.MembershipFact] = []
            attrs = self.normalize_attributes(user_entry)
            user_dn = str(user_entry.dn) if user_entry.dn is not None else ""
            if c.DbtLdap.LdapAttributes.MEMBER_OF in attrs:
                memberships.extend(
                    m.DbtLdap.MembershipFact(
                        user_dn=user_dn,
                        group_dn=group_dn,
                        membership_type=c.DbtLdap.MembershipTypes.DIRECT,
                    )
                    for group_dn in attrs[c.DbtLdap.LdapAttributes.MEMBER_OF]
                )
            return memberships

        @staticmethod
        def _is_group_entry(entry: m.Ldif.Entry) -> bool:
            """Check if entry is a group entry using canonical schema mapping."""
            object_classes = m.DbtLdap.get_object_classes(entry)
            return any(
                cls in object_classes
                for cls in c.DbtLdap.LdapSchemaMapping.GROUPS_CLASSES
            )

        @staticmethod
        def _is_user_entry(entry: m.Ldif.Entry) -> bool:
            """Check if entry is a user entry using canonical schema mapping."""
            object_classes = m.DbtLdap.get_object_classes(entry)
            return any(
                cls in object_classes
                for cls in c.DbtLdap.LdapSchemaMapping.USERS_CLASSES
            )


# Short aliases

__all__: t.StrSequence = [
    "FlextDbtLdapModels",
    "m",
]

m = FlextDbtLdapModels
