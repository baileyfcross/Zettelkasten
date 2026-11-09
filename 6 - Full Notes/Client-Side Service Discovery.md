2026-10-18 15:54

Status: #baby

Tags: [[Microservice Communication and Resilience]]

# Client-Side Service Discovery

Client-side service discovery makes the calling service query a [[Service Registry]] and choose one healthy target instance. The client can apply a load-balancing rule such as round robin, least connections, weighted selection, or a stable hash before making the request directly.

Removing an intermediate router can reduce one network hop and lets the client respond intelligently to instance health. The cost is duplicated discovery and balancing logic in every client language or framework. Registry caching, retries, and stale-instance handling must also be consistent. This approach fits environments with strong shared client libraries; heterogeneous consumers may favor [[Server-Side Service Discovery]] so the routing logic stays in infrastructure.

The Spring Cloud example uses Consul as the registry and a load-balanced RestClient to resolve a logical service name. Services register at startup, Actuator health removes unhealthy instances from the usable set, and the client replaces the logical hostname with one concrete address for each call. In Kubernetes, the platform's service discovery can make the additional registry unnecessary.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]

[[artofdecodingmicroservices.epub]]
