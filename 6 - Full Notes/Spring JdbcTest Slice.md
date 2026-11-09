2026-11-08 16:45

Status: #baby

Tags: [[Spring Data Access and Persistence]]

# Spring JdbcTest Slice

`@JdbcTest` loads a focused Spring test context containing JDBC infrastructure and an embedded database instead of the entire application. User-defined repository beans can be imported explicitly, giving a fast integration test of SQL, mapping, and schema behavior.

Each test runs transactionally and rolls back by default, isolating cases without manual cleanup. The slice is narrower than `@SpringBootTest`, but an embedded engine can still differ from production. A separate test against a containerized production database can verify dialect and engine behavior that the focused slice cannot establish.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
