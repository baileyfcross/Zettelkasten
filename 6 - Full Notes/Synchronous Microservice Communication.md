2026-10-18 15:54

Status: #baby

Tags: [[Microservice Communication and Resilience]]

# Synchronous Microservice Communication

Synchronous microservice communication makes a caller wait for a service to return a response. HTTP APIs, GraphQL requests, and gRPC calls can provide a direct request-response flow when the caller needs an immediate result and the interaction can be expressed through an explicit contract.

The waiting relationship couples availability and latency: a slow dependency holds the caller's resources, and a chain of calls can transmit one failure across several services. Timeouts, [[Circuit Breaker|circuit breaking]], bounded retries, and fallbacks keep that dependency visible and limited. When immediate completion is unnecessary or traffic needs buffering, [[Asynchronous Microservices|asynchronous communication]] can separate producer and consumer availability instead.

# References

[[artofdecodingmicroservices.epub]]
