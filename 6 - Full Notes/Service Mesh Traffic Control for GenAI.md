2026-09-29 22:24

Status: #baby

Tags: [[Kubernetes GenAI Network and Endpoint Security]]

# Service Mesh Traffic Control for GenAI

Service-mesh traffic control applies routing, retries, timeouts, circuit breaking, mutual TLS, identity, authorization, and telemetry to communication among GenAI microservices. Sidecar or ambient data-plane components enforce policy without adding each mechanism to model and retrieval code.

Retries and timeouts require model-aware limits because an inference request may be expensive and non-idempotent from the caller's perspective. The mesh complements NetworkPolicy: one governs authenticated application traffic, while the other establishes basic network reachability boundaries.

# References

[[kubernetesforgenerativeaisolutions.pdf]]

