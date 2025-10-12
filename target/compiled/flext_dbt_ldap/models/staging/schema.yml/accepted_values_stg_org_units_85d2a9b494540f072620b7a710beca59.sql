
    
    

with all_values as (

    select
        ou_type as value_field,
        count(*) as n_records

    from "flext_ldap_dev"."main_ldap_staging"."stg_org_units"
    group by ou_type

)

select *
from all_values
where value_field not in (
    'User Container','Group Container','Computer Container','Service Container','Business Unit','General Container'
)


