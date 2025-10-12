
    
    

with all_values as (

    select
        group_size_category as value_field,
        count(*) as n_records

    from "flext_ldap_dev"."main_ldap_marts"."dim_groups"
    group by group_size_category

)

select *
from all_values
where value_field not in (
    'Large','Medium','Small','Empty'
)


