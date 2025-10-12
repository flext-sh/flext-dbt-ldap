
    
    

select
    email as unique_field,
    count(*) as n_records

from (select * from "flext_ldap_dev"."main_ldap_marts"."dim_users" where email is not null) dbt_subquery
where email is not null
group by email
having count(*) > 1


