
    
    

select
    user_id || '_' || group_id as unique_field,
    count(*) as n_records

from "flext_ldap_dev"."main_ldap_marts"."fact_memberships"
where user_id || '_' || group_id is not null
group by user_id || '_' || group_id
having count(*) > 1


