
    
    

select
    dn as unique_field,
    count(*) as n_records

from "flext_ldap_dev"."main_ldap_staging"."stg_groups"
where dn is not null
group by dn
having count(*) > 1


