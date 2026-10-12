2026-10-11 21:26

Status: #baby

Tags: [[Docker Networking and Compose]]

# Compose Dependency Readiness

Compose dependency readiness distinguishes a dependency container being started from its service being able to accept work. Simple startup ordering can launch a database before an API, yet the API may still fail while the database initializes schemas or begins listening.

A dependency can expose a meaningful health check and the dependent service can wait for a healthy condition, but application retries and timeouts remain necessary. Readiness is dynamic: a service that was healthy at startup can later fail, so durable behavior cannot rely solely on the initial Compose order.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]
