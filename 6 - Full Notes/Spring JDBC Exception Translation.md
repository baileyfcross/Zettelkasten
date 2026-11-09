2026-11-08 16:45

Status: #baby

Tags: [[Spring Data Access and Persistence]]

# Spring JDBC Exception Translation

Spring JDBC exception translation converts vendor-specific checked SQL failures into the framework's `DataAccessException` runtime hierarchy. A repository layer can therefore report categories such as integrity violation or unavailable resource without making its callers depend on one driver's exception types.

Translation is applied around managed data-access components while JdbcTemplate also performs it for template operations. Business code should handle only failures for which it has a defined recovery or domain meaning rather than catching raw `SQLException`. The abstraction improves portability, but logs and telemetry still need the underlying cause for diagnosis.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
