
    
    

with child as (
    select group_id as from_field
    from "flext_ldap_dev"."main_ldap_marts"."fact_memberships"
    where group_id is not null
),

parent as (
    select group_id as to_field
    from "flext_ldap_dev"."main_ldap_marts"."dim_groups"
)

select
    from_field

from child
left join parent
    on child.from_field = parent.to_field

where parent.to_field is null


