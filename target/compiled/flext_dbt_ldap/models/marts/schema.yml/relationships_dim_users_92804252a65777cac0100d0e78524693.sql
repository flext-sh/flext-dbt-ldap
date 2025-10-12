
    
    

with child as (
    select organizational_unit_id as from_field
    from "flext_ldap_dev"."main_ldap_marts"."dim_users"
    where organizational_unit_id is not null
),

parent as (
    select dn as to_field
    from "flext_ldap_dev"."main_ldap_intermediate"."int_org_hierarchy"
)

select
    from_field

from child
left join parent
    on child.from_field = parent.to_field

where parent.to_field is null


