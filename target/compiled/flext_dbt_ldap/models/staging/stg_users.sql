

with source_data as (
    select *
    from "flext_ldap_dev"."ldap"."users"
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
    uid,
    cn as common_name,
    sn as surname,
    givenName as given_name,
    coalesce(displayName, cn) as display_name,
    mail as email,
    case
      when mail ~ '^[^@]+@[^@]+\.[^@]+$'
      then lower(split_part(mail, '@', 2))
      else null
    end as email_domain,
    telephoneNumber as phone,
    mobile as mobile_phone,
    title as job_title,
    department,
    employeeNumber as employee_id,
    manager as manager_dn,
    
  case
    when memberOf is null 
    then '[]'::json
    when json_typeof(memberOf::json) = 'array' 
    then memberOf::json
    when memberOf::text = '' 
    then '[]'::json
    else json_build_array(memberOf)::json
  end
 as member_of,
    
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
    userAccountControl as account_control,
    case
        when userAccountControl::int & 2 = 2 then true
        else false
    end as is_disabled,
    
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
    description,
    case
      when dn like '%ou=%'
      then split_part(split_part(dn, 'ou=', 2), ',', 1)
      else null
    end as organizational_unit
,
        -- Additional computed fields
        case
            when email is not null then true
            else false
        end as has_email,

        case
            when employee_id is not null then 'Employee'
            when uid like 'svc-%' then 'Service Account'
            when uid like 'app-%' then 'Application Account'
            else 'Standard User'
        end as account_type,

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

        -- Days since last modification
        current_date - 
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
::date as days_since_modified

    from source_data
)

select * from transformed