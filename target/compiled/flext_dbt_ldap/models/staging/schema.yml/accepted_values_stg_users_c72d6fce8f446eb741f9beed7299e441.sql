
    
    

with all_values as (

    select
        account_type as value_field,
        count(*) as n_records

    from "flext_ldap_dev"."main_ldap_staging"."stg_users"
    group by account_type

)

select *
from all_values
where value_field not in (
    'Employee','Service Account','Application Account','Standard User'
)


