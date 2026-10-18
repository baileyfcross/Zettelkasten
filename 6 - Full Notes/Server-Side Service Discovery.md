2026-10-18 15:54

Status: #baby

Tags: [[Microservice Communication and Resilience]]

# Server-Side Service Discovery

Server-side service discovery sends a request to a load balancer, gateway, or router that queries the [[Service Registry]] and forwards the request to an available instance. The caller uses one stable endpoint and does not implement registry access or selection logic.

Centralized routing supports clients written with different technologies and provides one place for balancing and health-aware decisions. It also adds an infrastructure hop whose capacity and failure behavior must be engineered. The router should scale, avoid stale registry data, and expose routing telemetry. Compared with [[Client-Side Service Discovery]], this approach moves complexity out of application clients but makes the routing tier a shared dependency.

# References

[[artofdecodingmicroservices.epub]]
