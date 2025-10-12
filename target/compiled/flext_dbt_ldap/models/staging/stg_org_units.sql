

with source_data as (
    select *
    from "flext_ldap_dev"."ldap"."organizational_units"
    where 
  case
    when dn is null then false
    when dn = '' then false
    when dn !~ '^[a-zA-Z]+=[^,]+' then false
    when dn like '%,,' then false
    when dn like '%=' then false
    else true
  end

),

transformed as (
    select
        
    dn,
    case
    when dn is not null and dn is not null and dn != ''
    then json_build_object(
      'rdn', split_part(dn, ',', 1),
      'rdn_value', split_part(split_part(dn, '=', 2), ',', 1),
      'rdn_attribute', split_part(dn, '=', 1),
      'parent_dn', regexp_replace(dn, '^[^,]+,', ''),
      'base_dn', 
  regexp_replace(
    dn, 
    '^[^,]+,?', 
    '', 
    'g'
  )
,
      'depth', 
  array_length(string_to_array(dn, ','), 1)
,
      'valid', 
  case
    when dn is null then false
    when dn = '' then false
    when dn !~ '^[a-zA-Z]+=[^,]+' then false
    when dn like '%,,' then false
    when dn like '%=' then false
    else true
  end

    )
    else null
  end
,
    ou as ou_name,
    description,
    businessCategory as business_category,
    postalAddress as postal_address,
    telephoneNumber as phone,
    
  case
    when objectClass is null 
    then '[]'::json
    when json_typeof(objectClass::json) = 'array' 
    then objectClass::json
    when objectClass::text = '' 
    then '[]'::json
    else json_build_array(objectClass)::json
  end
 as object_classes,
    
  case
    -- GeneralizedTime format (YYYYMMDDHHMMSS[.f]Z)
    when createTimestamp ~ '^\d{14}\.?\d*Z?$'
    then to_timestamp(
      substring(createTimestamp from 1 for 14),
      'YYYYMMDDHHMISS'
    )
    -- UTC format (YYYYMMDDHHMMSSZ)
    when createTimestamp ~ '^\d{14}Z$'
    then to_timestamp(
      substring(createTimestamp from 1 for 14),
      'YYYYMMDDHHMISS'
    ) at time zone 'UTC'
    -- Windows FileTime (100ns intervals since 1601-01-01)
    when createTimestamp ~ '^\d{18}$'
    then timestamp '1601-01-01 00:00:00' + 
         (createTimestamp::bigint / 10000000) * interval '1 second'
    -- Unix timestamp
    when createTimestamp ~ '^\d{10}$'
    then to_timestamp(createTimestamp::integer)
    -- ISO 8601 format
    when createTimestamp ~ '^\d{4}-\d{2}-\d{2}'
    then createTimestamp::timestamp
    else null
  end
 as created_at,
    
  case
    -- GeneralizedTime format (YYYYMMDDHHMMSS[.f]Z)
    when modifyTimestamp ~ '^\d{14}\.?\d*Z?$'
    then to_timestamp(
      substring(modifyTimestamp from 1 for 14),
      'YYYYMMDDHHMISS'
    )
    -- UTC format (YYYYMMDDHHMMSSZ)
    when modifyTimestamp ~ '^\d{14}Z$'
    then to_timestamp(
      substring(modifyTimestamp from 1 for 14),
      'YYYYMMDDHHMISS'
    ) at time zone 'UTC'
    -- Windows FileTime (100ns intervals since 1601-01-01)
    when modifyTimestamp ~ '^\d{18}$'
    then timestamp '1601-01-01 00:00:00' + 
         (modifyTimestamp::bigint / 10000000) * interval '1 second'
    -- Unix timestamp
    when modifyTimestamp ~ '^\d{10}$'
    then to_timestamp(modifyTimestamp::integer)
    -- ISO 8601 format
    when modifyTimestamp ~ '^\d{4}-\d{2}-\d{2}'
    then modifyTimestamp::timestamp
    else null
  end
 as modified_at,
    managedBy as managed_by_dn,
    parent_dn as parent_ou_dn
,

        -- Calculate OU depth in hierarchy
        array_length(string_to_array(dn, ','), 1) - 1 as hierarchy_depth,

        -- Check if it's a top-level OU
        case
            when parent_dn = 'dc=example,dc=com' then true
            else false
        end as is_top_level,

        -- OU type classification
        case
            when lower(ou_name) in ('users', 'people', 'employees') then 'User Container'
            when lower(ou_name) in ('groups', 'roles') then 'Group Container'
            when lower(ou_name) in ('computers', 'servers', 'workstations') then 'Computer Container'
            when lower(ou_name) in ('services', 'applications') then 'Service Container'
            when business_category is not null then 'Business Unit'
            else 'General Container'
        end as ou_type,

        -- Extract year from created timestamp
        extract(year from 
  case
    -- GeneralizedTime format (YYYYMMDDHHMMSS[.f]Z)
    when createTimestamp ~ '^\d{14}\.?\d*Z?$'
    then to_timestamp(
      substring(createTimestamp from 1 for 14),
      'YYYYMMDDHHMISS'
    )
    -- UTC format (YYYYMMDDHHMMSSZ)
    when createTimestamp ~ '^\d{14}Z$'
    then to_timestamp(
      substring(createTimestamp from 1 for 14),
      'YYYYMMDDHHMISS'
    ) at time zone 'UTC'
    -- Windows FileTime (100ns intervals since 1601-01-01)
    when createTimestamp ~ '^\d{18}$'
    then timestamp '1601-01-01 00:00:00' + 
         (createTimestamp::bigint / 10000000) * interval '1 second'
    -- Unix timestamp
    when createTimestamp ~ '^\d{10}$'
    then to_timestamp(createTimestamp::integer)
    -- ISO 8601 format
    when createTimestamp ~ '^\d{4}-\d{2}-\d{2}'
    then createTimestamp::timestamp
    else null
  end
) as created_year

    from source_data
)

select * from transformed