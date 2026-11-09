2026-11-08 16:45

Status: #baby

Tags: [[Spring Data Access and Persistence]]

# Spring Data R2DBC Repository

A Spring Data R2DBC repository exposes relational operations through `Mono` and `Flux` without the blocking JDBC driver model. R2DBC connections, queries, and transactions participate in a reactive pipeline, and `DatabaseClient` supplies lower-level fluent SQL when generated CRUD methods are insufficient.

The database schema must still be created explicitly, and production applications need a reactive connection pool. Calling `block` on the event loop defeats the design, while backpressure and bounded demand remain relevant for large results. R2DBC is therefore a complete nonblocking path rather than a reactive wrapper around [[Spring JdbcTemplate Repository]].

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
