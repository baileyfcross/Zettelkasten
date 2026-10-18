2026-10-18 15:54

Status: #baby

Tags: [[Microservice Security and Observability]]

# Mutual TLS Between Microservices

Mutual TLS between microservices protects a connection and requires both endpoints to present identities through certificates. The client verifies that it reached the intended service, the service verifies the calling workload, and encryption protects the traffic in transit.

Mutual authentication does not decide what the caller may do; authorization still needs a policy based on the verified identity and request. The mechanism also creates certificate issuance, storage, rotation, revocation, and observability work. A failed or expired certificate can become an availability incident, so lifecycle automation is part of the security design. User-facing [[Token-Based Authentication]] may coexist with mutual TLS because client identity and workload identity address different trust boundaries.

# References

[[artofdecodingmicroservices.epub]]
