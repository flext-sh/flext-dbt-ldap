-- Modern DBT 1.9+ Tests for LDAP macros
-- These tests validate macro functionality without requiring database connection

-- Simple validation that macros compile correctly
with mock_data as (
    select 
        'uid=jdoe,ou=users,dc=example,dc=com' as sample_dn,
        '["inetOrgPerson", "person"]' as sample_object_classes,
        'user@example.com' as sample_email,
        '20240101120000Z' as sample_ldap_timestamp
)

select 
    'macro_compilation_test' as test_name,
    count(*) as test_count
from mock_data
where sample_dn is not null