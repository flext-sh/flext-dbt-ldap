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


def _described_field[T](default: T, description: str) -> T:
    return Field(default=default, description=description)


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

            total_entries: int = _described_field(0, "Total LDAP entries evaluated")
            valid_dns: int = _described_field(0, "Entries with valid DNs")
            valid_entries: int = _described_field(
                0,
                "Entries satisfying required attributes",
            )
            quality_score: float = _described_field(0.0, "Validation quality score")
            validation_passed: bool = _described_field(
                False,
                "Whether validation met the configured threshold",
            )

        class DbtRunStatus(FlextMeltanoModels.Value):
            """Status of a DBT transformation run."""

            status: str = _described_field(
                c.Meltano.StreamStatus.PENDING,
                "Lifecycle status for the DBT execution",
            )
            models_run: t.StrSequence = Field(
                default_factory=list,
                description="DBT models executed during the run",
            )
            entries_processed: int = _described_field(
                0,
                "LDAP entries processed by the run",
            )

        class DbtLdapPipelineResult(FlextMeltanoModels.Value):
            """Result of a complete LDAP-to-DBT pipeline run."""

            extracted_entries: int = _described_field(
                0,
                "LDAP entries extracted by the pipeline",
            )

        class SyncResult(FlextMeltanoModels.Value):
            """Result of full data warehouse sync."""

            overall_success: bool = _described_field(
                False,
                "Whether every sync component completed successfully",
            )
            successful_components: int = _described_field(
                0,
                "Number of successful sync components",
            )
            total_components: int = _described_field(
                0,
                "Total sync components evaluated",
            )

        class PerformanceAnalysis(FlextMeltanoModels.Value):
            """Performance analysis metrics."""

            execution_time: float = _described_field(
                0.0,
                "Execution time in seconds",
            )
            rows_processed: int = _described_field(0, "Rows processed by the run")
            memory_usage: float = _described_field(
                0.0,
                "Peak memory usage in megabytes",
            )
            recommendations: t.StrSequence = Field(
                default_factory=list,
                description="Performance tuning recommendations",
            )

        class ServiceStatus(FlextMeltanoModels.Value):
            """Service status and capabilities."""

            status: str = _described_field(
                c.DbtLdap.OPERATIONAL,
                "Current service health status",
            )
            service: str = _described_field("", "Service name")
            capabilities: t.StrSequence = Field(
                default_factory=list,
                description="Supported public service capabilities",
            )

        class AnalyticsReport(FlextMeltanoModels.Value):
            """Analytics report data."""

            report_type: str = _described_field("summary", "Report category")
            generated_at: str = _described_field("", "Report generation timestamp")

        # =========================================================================
        # DBT CONFIGURATION MODELS
        # =========================================================================

        class DbtProjectConfig(FlextMeltanoModels.Value):
            """DBT project configuration (dbt_project.yml)."""

            name: str = Field(description="DBT project name")
            version: str = _described_field(
                c.Meltano.CONSTANTS_VERSION,
                "DBT project version",
            )
            profile: str = _described_field("", "DBT profile name")
            model_paths: t.StrSequence = _described_field(
                ["models"],
                "Directories containing DBT models",
            )
            analysis_paths: t.StrSequence = _described_field(
                ["analyses"],
                "Directories containing DBT analyses",
            )
            test_paths: t.StrSequence = _described_field(
                ["tests"],
                "Directories containing DBT tests",
            )
            seed_paths: t.StrSequence = _described_field(
                ["seeds"],
                "Directories containing DBT seeds",
            )
            macro_paths: t.StrSequence = _described_field(
                ["macros"],
                "Directories containing DBT macros",
            )
            snapshot_paths: t.StrSequence = _described_field(
                ["snapshots"],
                "Directories containing DBT snapshots",
            )
            target_path: str = _described_field(
                c.Meltano.PREFIX_TARGET,
                "Directory used for DBT build artifacts",
            )
            clean_targets: t.StrSequence = _described_field(
                [c.Meltano.PREFIX_TARGET, "dbt_packages"],
                "Directories cleaned by DBT maintenance commands",
            )
            target_schema: str = _described_field(
                "public",
                "Default database schema for DBT relations",
            )
            tags: t.StrSequence = Field(
                default_factory=list,
                description="Tags applied to generated DBT resources",
            )
            materialized: str = _described_field(
                c.Meltano.DBT_MATERIALIZATION_TABLE,
                "Default DBT materialization strategy",
            )

        class DbtProfileConfig(FlextMeltanoModels.Value):
            """DBT profile connection configuration."""

            type: str = _described_field("postgres", "Database adapter type")
            host: str = _described_field(c.LOCALHOST, "Database host")
            user: str = _described_field("dbt_user", "Database user name")
            password: str = _described_field("", "Database password")
            port: int = _described_field(
                c.Meltano.DB_PORT_POSTGRES,
                "Database port",
            )
            dbname: str = _described_field("ldap_db", "Database name")
            schema_name: str = _described_field(
                "public",
                "Target schema for DBT models",
            )
            threads: int = _described_field(4, "Number of DBT worker threads")

        class DbtSourceTable(FlextMeltanoModels.Value):
            """DBT source table definition."""

            name: str = Field(description="DBT source table name")
            description: str = _described_field("", "DBT source table description")

        class DbtSourceSchema(FlextMeltanoModels.Value):
            """DBT source schema definition."""

            version: str = _described_field("2", "DBT schema.yml version")
            sources: Sequence[Mapping[str, t.Serializable]] = Field(
                default_factory=lambda: list[Mapping[str, t.Serializable]](),
                description="DBT source definitions",
            )

        class DbtModelDefinition(FlextMeltanoModels.Value):
            """DBT model definition (schema.yml)."""

            version: str = _described_field("2", "DBT schema.yml version")
            models: Sequence[Mapping[str, t.Serializable]] = Field(
                default_factory=lambda: list[Mapping[str, t.Serializable]](),
                description="DBT model definitions",
            )

        class DbtTestConfig(FlextMeltanoModels.Value):
            """DBT test configuration."""

            version: str = _described_field("2", "DBT schema.yml version")
            models: Sequence[Mapping[str, t.Serializable]] = Field(
                default_factory=lambda: list[Mapping[str, t.Serializable]](),
                description="DBT test model definitions",
            )
            columns: t.DbtLdap.LdapEntryMapping = Field(
                default_factory=dict,
                description="Column-level DBT tests keyed by attribute name",
            )

        class DbtSourceFreshness(FlextMeltanoModels.Value):
            """DBT source freshness configuration."""

            warn_after: t.IntMapping = Field(
                default_factory=dict,
                description="Warning freshness thresholds",
            )
            error_after: t.IntMapping = Field(
                default_factory=dict,
                description="Error freshness thresholds",
            )

        class DbtSourceDefinition(FlextMeltanoModels.Value):
            """Complete DBT source definition."""

            name: str = Field(description="DBT source name")
            description: str = _described_field("", "DBT source description")
            tables: Sequence[Mapping[str, t.Serializable]] = Field(
                default_factory=lambda: list[Mapping[str, t.Serializable]](),
                description="Tables declared for the DBT source",
            )

        class DbtConfig(FlextMeltanoModels.Value):
            """General DBT execution configuration."""

            target: str = _described_field(
                c.DbtLdap.DEFAULT_TARGET,
                "Named DBT target to execute against",
            )
            profiles_dir: str = _described_field(
                "", "Path to the DBT profiles directory"
            )
            project_dir: str = _described_field("", "Path to the DBT project directory")

        class ProjectStructureValidation(FlextMeltanoModels.Value):
            """DBT project structure validation result."""

            results: t.BoolMapping = Field(
                default_factory=dict,
                description="Validation results keyed by project artifact",
            )

        class OptimizationHints(FlextMeltanoModels.Value):
            """Query optimization hints."""

            add_indexes: bool = _described_field(
                False,
                "Whether index recommendations should be applied",
            )
            index_columns: t.StrSequence = Field(
                default_factory=list,
                description="Columns recommended for indexing",
            )
            partition_by: str = _described_field(
                "",
                "Suggested partition key for large tables",
            )
            filter_early: bool = _described_field(
                False,
                "Whether filters should be pushed earlier in the query",
            )

        # =========================================================================
        # TRANSFORMATION MODELS
        # =========================================================================

        class TransformationConfig(FlextMeltanoModels.Value):
            """Transformation configuration."""

            source_table: str = _described_field(
                "", "Source table used by the transformation"
            )
            transformations: t.StrMapping = Field(
                default_factory=dict,
                description="Column transformation expressions",
            )
            filters: t.StrSequence = Field(
                default_factory=list,
                description="Filter expressions applied before transformation",
            )

        class TransformationRule(FlextMeltanoModels.Value):
            """Transformation rule definition."""

            name: str = _described_field("", "Transformation rule name")
            rules: t.StrMapping = Field(
                default_factory=dict,
                description="Named transformation rules",
            )

        class DataValidationConfig(FlextMeltanoModels.Value):
            """Data validation configuration."""

            min_quality_threshold: float = _described_field(
                c.DbtLdap.DEFAULT_QUALITY_THRESHOLD,
                "Minimum validation score accepted for LDAP data",
            )
            required_attributes: t.StrSequence = Field(
                default_factory=list,
                description="LDAP attributes required for a valid entry",
            )
            validate_dns: bool = _described_field(
                True,
                "Whether distinguished names must be present",
            )
            columns: t.DbtLdap.LdapEntryMapping = Field(
                default_factory=dict,
                description="Column validation configuration keyed by attribute",
            )

        # =========================================================================
        # LDAP MODELS
        # =========================================================================

        class LdapSchema(FlextMeltanoModels.Value):
            """LDAP schema configuration."""

            object_classes: t.StrSequence = Field(
                default_factory=list,
                description="LDAP object classes associated with the schema",
            )
            required_attributes: t.StrSequence = Field(
                default_factory=list,
                description="LDAP attributes required by the schema",
            )

        class LdapQuery(FlextMeltanoModels.Value):
            """LDAP query configuration."""

            base_dn: str = _described_field("", "LDAP base DN for the query")
            filter_str: str = _described_field(
                c.Ldap.Filters.ALL_ENTRIES_FILTER,
                "LDAP search filter",
            )
            attributes: t.StrSequence = Field(
                default_factory=list,
                description="LDAP attributes requested by the query",
            )
            scope: str = _described_field(
                c.Ldap.SearchDefaults.DEFAULT_SCOPE,
                "LDAP search scope",
            )

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

            common_name: str = Field(description="Canonical common name")
            is_active: bool = _described_field(
                True, "Whether the directory record is active"
            )
            created_date: str | None = Field(
                default=None,
                description="Source creation timestamp",
            )
            modified_date: str | None = Field(
                default=None,
                description="Source modification timestamp",
            )

        class UserDimension(_DbtDimensionBase):
            """User dimension — validated at construction via model_validator."""

            user_id: str = Field(description="Canonical user identifier")
            email: str | None = Field(default=None, description="Primary user email")
            display_name: str | None = Field(
                default=None,
                description="Display name shown to users",
            )
            department: str | None = Field(
                default=None,
                description="User department name",
            )
            manager_dn: str | None = Field(
                default=None,
                description="Distinguished name of the manager",
            )
            employee_number: str | None = Field(
                default=None,
                description="Employee number from LDAP",
            )
            phone: str | None = Field(default=None, description="Primary phone number")

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
                return cls(
                    user_id=get_attr(attrs, c.DbtLdap.UID, "") or "",
                    common_name=get_attr(attrs, c.DbtLdap.CN, "") or "",
                    email=get_attr(attrs, c.DbtLdap.MAIL),
                    display_name=get_attr(attrs, c.DbtLdap.DISPLAY_NAME),
                    department=get_attr(attrs, c.DbtLdap.DEPARTMENT),
                    manager_dn=get_attr(attrs, c.DbtLdap.MANAGER),
                    employee_number=get_attr(attrs, c.DbtLdap.EMPLOYEE_NUMBER),
                    phone=get_attr(attrs, c.DbtLdap.TELEPHONE_NUMBER),
                    is_active=not (
                        c.DbtLdap.USER_ACCOUNT_CONTROL in attrs
                        and "2" in str(attrs[c.DbtLdap.USER_ACCOUNT_CONTROL][0])
                    ),
                    created_date=get_attr(attrs, c.DbtLdap.CREATE_TIMESTAMP),
                    modified_date=get_attr(attrs, c.DbtLdap.MODIFY_TIMESTAMP),
                )

        class GroupDimension(_DbtDimensionBase):
            """Group dimension — validated at construction via model_validator."""

            group_id: str = Field(description="Canonical group identifier")
            description: str | None = Field(
                default=None,
                description="Group description from LDAP",
            )
            group_type: str | None = Field(
                default=None,
                description="Group type classification",
            )
            member_count: int = _described_field(0, "Number of direct group members")

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
                member_count = len(attrs.get(c.DbtLdap.MEMBER, [])) + len(
                    attrs.get(c.DbtLdap.UNIQUE_MEMBER, []),
                )
                return cls(
                    group_id=get_attr(attrs, c.DbtLdap.CN, "") or "",
                    common_name=get_attr(attrs, c.DbtLdap.CN, "") or "",
                    description=get_attr(attrs, c.DbtLdap.DESCRIPTION),
                    group_type=get_attr(attrs, c.DbtLdap.GROUP_TYPE),
                    member_count=member_count,
                    is_active=True,
                    created_date=get_attr(attrs, c.DbtLdap.CREATE_TIMESTAMP),
                    modified_date=get_attr(attrs, c.DbtLdap.MODIFY_TIMESTAMP),
                )

        class MembershipFact(_DbtSerializable):
            """Membership fact — validated at construction via model_validator."""

            user_dn: str = Field(description="Member distinguished name")
            group_dn: str = Field(description="Group distinguished name")
            membership_type: str = _described_field(
                c.DbtLdap.DIRECT,
                "Membership relationship type",
            )
            is_primary: bool = _described_field(
                False,
                "Whether the membership is the primary assignment",
            )
            effective_date: str | None = Field(
                default=None,
                description="Membership effective timestamp",
            )
            expiry_date: str | None = Field(
                default=None,
                description="Membership expiry timestamp",
            )

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
            return raw.get(c.Ldap.LdapAttributeNames.OBJECT_CLASS, [])

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
                except c.Meltano.SINGER_SAFE_EXCEPTIONS:
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
                except c.Meltano.SINGER_SAFE_EXCEPTIONS:
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
            for attr in c.DbtLdap.MEMBERSHIP_ATTRIBUTES:
                if attr in attrs:
                    memberships.extend(
                        m.DbtLdap.MembershipFact(
                            user_dn=member_dn,
                            group_dn=group_dn,
                            membership_type=c.DbtLdap.DIRECT,
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
            if c.DbtLdap.MEMBER_OF in attrs:
                memberships.extend(
                    m.DbtLdap.MembershipFact(
                        user_dn=user_dn,
                        group_dn=group_dn,
                        membership_type=c.DbtLdap.DIRECT,
                    )
                    for group_dn in attrs[c.DbtLdap.MEMBER_OF]
                )
            return memberships

        @staticmethod
        def _is_group_entry(entry: m.Ldif.Entry) -> bool:
            """Check if entry is a group entry using canonical schema mapping."""
            object_classes = m.DbtLdap.get_object_classes(entry)
            return any(cls in object_classes for cls in c.DbtLdap.GROUPS_CLASSES)

        @staticmethod
        def _is_user_entry(entry: m.Ldif.Entry) -> bool:
            """Check if entry is a user entry using canonical schema mapping."""
            object_classes = m.DbtLdap.get_object_classes(entry)
            return any(cls in object_classes for cls in c.DbtLdap.USERS_CLASSES)


# Short aliases

__all__: t.StrSequence = [
    "FlextDbtLdapModels",
    "m",
]

m = FlextDbtLdapModels
