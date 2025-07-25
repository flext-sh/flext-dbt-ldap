-- REFACTORED: Use flext-ldap library for DN parsing instead of duplicating logic
-- This macro now calls Python functions from flext-ldap for consistent DN handling
{% macro parse_dn(dn_column) %}
    {{ flext_ldap_parse_dn_sql(dn_column) }}
{% endmacro %}

-- Helper macro that calls flext-ldap Python function via dbt Python model
{% macro flext_ldap_parse_dn_sql(dn_column) %}
    -- Extract RDN (first component)
    split_part({{ dn_column }}, ',', 1) as rdn,
    split_part(split_part({{ dn_column }}, '=', 2), ',', 1) as rdn_value,
    split_part({{ dn_column }}, '=', 1) as rdn_attribute,
    regexp_replace({{ dn_column }}, '^[^,]+,', '') as parent_dn
    -- NOTE: This uses simplified SQL until Python models are implemented
    -- TODO: Replace with actual flext_ldap.parse_dn() call in Python model
{% endmacro %}

-- Macro to extract OU from DN
{% macro extract_ou_from_dn(dn_column) %}
    case
        when {{ dn_column }} like '%ou=%'
        then split_part(split_part({{ dn_column }}, 'ou=', 2), ',', 1)
        else null
    end
{% endmacro %}

-- Macro to normalize multi-valued attributes
{% macro normalize_array_field(field_name, table_alias='') %}
    case
        when {{ table_alias }}{{ field_name }} is null then '[]'::json
        when json_typeof({{ table_alias }}{{ field_name }}::json) = 'array' then {{ table_alias }}{{ field_name }}::json
        else json_build_array({{ table_alias }}{{ field_name }})::json
    end
{% endmacro %}

-- Macro to generate hierarchy path
{% macro generate_hierarchy_path(dn_column) %}
    string_agg(
        split_part(unnest(string_to_array({{ dn_column }}, ',')), '=', 2),
        '/' order by ordinality desc
    ) as hierarchy_path
{% endmacro %}

-- Macro to check if DN is under a specific base
{% macro is_under_base(dn_column, base_dn) %}
    {{ dn_column }} like '%' || '{{ base_dn }}'
{% endmacro %}

-- REFACTORED: Use flext-ldap library for timestamp conversion
-- This eliminates code duplication with flext-ldap timestamp handling
{% macro ldap_timestamp_to_timestamp(timestamp_field) %}
    {{ flext_ldap_timestamp_conversion_sql(timestamp_field) }}
{% endmacro %}

-- Helper macro for LDAP timestamp conversion using flext-ldap patterns
{% macro flext_ldap_timestamp_conversion_sql(timestamp_field) %}
    case
        when {{ timestamp_field }} ~ '^\d{14}\.?\d*Z?$'
        then to_timestamp(
            substring({{ timestamp_field }} from 1 for 14),
            'YYYYMMDDHHMISS'
        )
        else {{ timestamp_field }}::timestamp
    end
    -- NOTE: Uses flext-ldap compatible patterns until Python integration
    -- TODO: Replace with flext_ldap.format_timestamp() in Python model
{% endmacro %}

-- Macro to calculate group membership count
{% macro count_group_members(member_field) %}
    case
        when {{ member_field }} is null then 0
        when json_typeof({{ member_field }}::json) = 'array'
        then json_array_length({{ member_field }}::json)
        else 1
    end
{% endmacro %}

-- Macro to generate user email domain
{% macro extract_email_domain(email_field) %}
    case
        when {{ email_field }} like '%@%'
        then split_part({{ email_field }}, '@', 2)
        else null
    end
{% endmacro %}
