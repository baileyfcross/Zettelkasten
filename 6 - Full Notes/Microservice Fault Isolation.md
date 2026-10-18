2026-10-18 15:54

Status: #baby

Tags: [[Microservice Architecture Adoption]]

# Microservice Fault Isolation

Microservice fault isolation limits a service failure so unrelated capabilities can continue operating. Separate processes and resources create potential containment boundaries: a failed recommendation service, for example, need not make ordering unavailable if callers can detect the failure and use an acceptable degraded path.

Isolation is not automatic. Synchronous call chains, shared databases, exhausted connection pools, or uncontrolled retries can transmit one dependency's failure to many callers. Timeouts, [[Circuit Breaker|circuit breakers]], bulkheads, fallbacks, health checks, and capacity limits enforce the intended boundary. The service contract should state what a caller receives during degradation so a fallback preserves known behavior rather than concealing a different failure.

# References

[[artofdecodingmicroservices.epub]]
