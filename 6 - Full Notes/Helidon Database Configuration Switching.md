2026-10-19 22:48

Status: #baby

Tags: [[Helidon Database Client]]

# Helidon Database Configuration Switching

Helidon DB Client moves the database source, connection details, and named statements into configuration. A deployment can select a JDBC or MongoDB implementation and provide its native queries while the Java service continues to depend on `DbClient`.

The abstraction does not make SQL and MongoDB syntax identical; configuration holds the implementation-specific expression. It instead keeps that difference outside the service's source code so a database choice or environment-specific statement does not require recompilation.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
