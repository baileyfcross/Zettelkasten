2026-10-19 22:48

Status: #baby

Tags: [[Helidon Database Client]]

# Helidon DB Client Backpressure

Helidon DB Client supports backpressure when it delivers a query result set. Rows are processed according to demand from the query subscriber rather than being pushed without regard for the consumer's capacity.

For JDBC, this flow-control behavior is layered over an executor-wrapped blocking driver; for MongoDB, it works with the native reactive driver. The common behavior is part of the client's effort to present database access through a consistent reactive API.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
