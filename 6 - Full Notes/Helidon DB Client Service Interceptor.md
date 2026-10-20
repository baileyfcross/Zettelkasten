2026-10-19 22:48

Status: #baby

Tags: [[Helidon Database Client]]

# Helidon DB Client Service Interceptor

A Helidon `DbClientService` can modify the data used to execute a statement and react to its result. Services are attached to the DB Client builder and run in registration order, or according to priority when discovered through Java service loading.

The functional service contract supplies a common interception point for cross-cutting behavior. Helidon uses it to attach [[Helidon DB Client Metrics]], [[Helidon DB Client Health Check]], and [[Helidon DB Client Tracing]] without placing that instrumentation inside every database operation.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
