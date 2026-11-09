2026-10-30 17:24

Status: #baby

Tags: [[Spring Data Access and Persistence]]

# Spring CrudRepository Adapter

Spring's `CrudRepository` is a generic persistence contract for a repository's entity and identifier types. The book uses it as a stable port that Spring adapts first to PostgreSQL and then to MongoDB, demonstrating that the application-facing CRUD interface need not name the database technology.

The dependency and configuration choose the adapter, while the service retains the same calls. Persistence-specific mappings may still require an outer representation so those details do not make the shared domain entity store-dependent.

The Spring Boot 4 data discussion treats the generated repository as a ladder above hand-written JdbcClient SQL. Common save, find, delete, pagination, and derived-query contracts remove implementation boilerplate, but the choice between JDBC aggregates, JPA relationships, MongoDB documents, and reactive R2DBC remains an architectural choice rather than a property of the generic CRUD name.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]

[[javamicroservicesandcontainersinthecloud.epub]]

