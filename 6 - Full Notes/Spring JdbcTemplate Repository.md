2026-11-08 16:45

Status: #baby

Tags: [[Spring Data Access and Persistence]]

# Spring JdbcTemplate Repository

`JdbcTemplate` is Spring's classic abstraction over JDBC resource management. A repository supplies SQL, parameters, and a row mapper while the template opens and closes connections, prepares statements, iterates results, and returns affected-row counts for insert, update, or delete operations.

Queries can bind values through placeholders rather than concatenating input into SQL, and the row mapper makes the database-to-domain conversion explicit. This level is useful when the application needs direct SQL control but does not want connection and result-set boilerplate. [[Spring JdbcClient Fluent Data Access]] wraps the same foundation with a more compact fluent interface.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
