

with source_data as (
    select *
    from "flext_ldap_dev"."ldap"."groups"
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
    cn as group_name,
    description,
    
  case
    when member is null 
    then '[]'::json
    when json_typeof(member::json) = 'array' 
    then member::json
    when member::text = '' 
    then '[]'::json
    else json_build_array(member)::json
  end
 as members,
    
  case
    when memberUid is null 
    then '[]'::json
    when json_typeof(memberUid::json) = 'array' 
    then memberUid::json
    when memberUid::text = '' 
    then '[]'::json
    else json_build_array(memberUid)::json
  end
 as member_uids,
    
  case
    when member is null then 0
    when member::text = '' then 0
    when json_typeof(
  case
    when member is null 
    then '[]'::json
    when json_typeof(member::json) = 'array' 
    then member::json
    when member::text = '' 
    then '[]'::json
    else json_build_array(member)::json
  end
) = 'array'
    then json_array_length(
  case
    when member is null 
    then '[]'::json
    when json_typeof(member::json) = 'array' 
    then member::json
    when member::text = '' 
    then '[]'::json
    else json_build_array(member)::json
  end
)
    else 1
  end
 as member_count,
    groupType as group_type,
    case
        when groupType::int & 2147483648 = 2147483648 then 'Security'
        else 'Distribution'
    end as group_category,
    
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
    case
      when dn like '%ou=%'
      then split_part(split_part(dn, 'ou=', 2), ',', 1)
      else null
    end as organizational_unit
,

        -- Group classification
        case
            when group_name like 'app-%' then 'Application'
            when group_name like 'role-%' then 'Role-based'
            when group_name like 'dept-%' then 'Department'
            when group_name like 'team-%' then 'Team'
            when group_name like 'project-%' then 'Project'
            else 'General'
        end as group_classification,

        -- Check if group is empty
        case
            when 
  case
    when member is null then 0
    when member::text = '' then 0
    when json_typeof(
  case
    when member is null 
    then '[]'::json
    when json_typeof(member::json) = 'array' 
    then member::json
    when member::text = '' 
    then '[]'::json
    else json_build_array(member)::json
  end
) = 'array'
    then json_array_length(
  case
    when member is null 
    then '[]'::json
    when json_typeof(member::json) = 'array' 
    then member::json
    when member::text = '' 
    then '[]'::json
    else json_build_array(member)::json
  end
)
    else 1
  end
 = 0 then true
            when 
  case
    when member is null then 0
    when member::text = '' then 0
    when json_typeof(
  case
    when member is null 
    then '[]'::json
    when json_typeof(member::json) = 'array' 
    then member::json
    when member::text = '' 
    then '[]'::json
    else json_build_array(member)::json
  end
) = 'array'
    then json_array_length(
  case
    when member is null 
    then '[]'::json
    when json_typeof(member::json) = 'array' 
    then member::json
    when member::text = '' 
    then '[]'::json
    else json_build_array(member)::json
  end
)
    else 1
  end
 = 1
                and members::text like '%placeholder%' then true
            else false
        end as is_empty,

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
) as created_year,

        -- Check if recently modified (within 30 days)
        case
            when current_date - 
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
::date <= 30
            then true
            else false
        end as recently_modified

    from source_data
)

select * from transformed