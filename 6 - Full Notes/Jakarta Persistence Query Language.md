2026-11-08 14:08

Status: #baby

Tags: [[Jakarta Persistence and Data Access]]

# Jakarta Persistence Query Language

The Jakarta Persistence Query Language is a string-based query language that resembles SQL but addresses persistent entities, their fields, and their relationships rather than database tables and rows. The persistence provider translates a JPQL expression into the SQL dialect required by the configured database.

An EntityManager executes either a dynamic query supplied at the call site or a named query declared under a stable name, often on the entity. Parameters keep values separate from query structure, and typed query creation can state the expected Java result type. JPQL is especially suitable when the query shape is known in advance.

# References

[[procloud-nativejavaeeapps_devopswithmicroprofilejakartaee11apisand.epub]]
