
    
    

select
    cn as unique_field,
    count(*) as n_records

from "flext_ldap_dev"."ldap"."groups"
where cn is not null
group by cn
having count(*) > 1


