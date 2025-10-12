
    
    

select
    group_id as unique_field,
    count(*) as n_records

from "flext_ldap_dev"."main_ldap_marts"."dim_groups"
where group_id is not null
group by group_id
having count(*) > 1


