
    
    

select
    group_name as unique_field,
    count(*) as n_records

from "flext_ldap_dev"."main_ldap_staging"."stg_groups"
where group_name is not null
group by group_name
having count(*) > 1


