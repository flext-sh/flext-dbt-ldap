
    
    

select
    mail as unique_field,
    count(*) as n_records

from "flext_ldap_dev"."ldap"."users"
where mail is not null
group by mail
having count(*) > 1


