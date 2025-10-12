
    
    

select
    dn as unique_field,
    count(*) as n_records

from "flext_ldap_dev"."ldap"."organizational_units"
where dn is not null
group by dn
having count(*) > 1


