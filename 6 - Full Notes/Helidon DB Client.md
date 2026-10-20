2026-10-19 22:48

Status: #baby

Tags: [[Helidon Database Client]]

# Helidon DB Client

Helidon DB Client is a unified database API for SE applications that abstracts relational JDBC access and MongoDB access behind the `DbClient` interface. It is configured through Helidon Config and exposes execution facilities without requiring application code to use a database-specific API for every operation.

The client implements `AutoCloseable` and is created from database configuration through a builder. Metrics, health checks, and tracing can be attached as services, and database statements can be named in configuration so their implementation can vary by environment.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
