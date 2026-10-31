2026-10-18 15:54

Status: #baby

Tags: [[Microservice Communication and Resilience]]

# Synchronous Microservice Communication

Synchronous microservice communication makes a caller wait for a service to return a response. HTTP APIs, GraphQL requests, and gRPC calls can provide a direct request-response flow when the caller needs an immediate result and the interaction can be expressed through an explicit contract.

The waiting relationship couples availability and latency: a slow dependency holds the caller's resources, and a chain of calls can transmit one failure across several services. Timeouts, [[Circuit Breaker|circuit breaking]], bounded retries, and fallbacks keep that dependency visible and limited. When immediate completion is unnecessary or traffic needs buffering, [[Asynchronous Microservices|asynchronous communication]] can separate producer and consumer availability instead.

The source contrasts point-to-point HTTP with brokered messaging: one unresponsive provider can cause the synchronous consumer's user request to fail its service-level expectation. If a result is truly required, RPC is direct; when no immediate downstream information is needed, messaging avoids making the caller wait for a remote completion.

# References

[[artofdecodingmicroservices.epub]]
[[javamicroservicesandcontainersinthecloud.epub]]
