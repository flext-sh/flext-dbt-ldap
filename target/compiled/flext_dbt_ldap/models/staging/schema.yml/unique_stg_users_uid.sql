
    
    

select
    uid as unique_field,
    count(*) as n_records

from "flext_ldap_dev"."main_ldap_staging"."stg_users"
where uid is not null
group by uid
having count(*) > 1


