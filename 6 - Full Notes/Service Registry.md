2026-10-18 15:54

Status: #baby

Tags: [[Microservice Communication and Resilience]]

# Service Registry

A service registry records the available instances for a logical service and the network locations at which they can be reached. Instances register when they become available and are removed when they stop or fail health checks, allowing callers to discover a changing replica set rather than depend on fixed addresses.

The registry must itself be available, secured, and kept current. Stale entries can route calls to failed instances, while unauthorized registration can redirect traffic. Discovery can be performed by the caller through [[Client-Side Service Discovery]] or by a router through [[Server-Side Service Discovery]]. In either case, health checks, deregistration, load balancing, and monitoring are part of the mechanism rather than optional additions.

# References

[[artofdecodingmicroservices.epub]]
