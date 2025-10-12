
    
    

with all_values as (

    select
        group_category as value_field,
        count(*) as n_records

    from "flext_ldap_dev"."main_ldap_staging"."stg_groups"
    group by group_category

)

select *
from all_values
where value_field not in (
    'Security','Distribution'
)


