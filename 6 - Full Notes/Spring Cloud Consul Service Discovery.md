2026-11-08 16:45

Status: #baby

Tags: [[Spring Cloud Operations and Native Runtime]]

# Spring Cloud Consul Service Discovery

Spring Cloud Consul lets a Boot service register its logical name and current location with a Consul agent and discover other registered services at runtime. Actuator health information can update the registry so unhealthy instances are removed from the set offered to callers.

A load-balanced RestClient or WebClient can use a logical hostname, query the registry, and select a healthy instance through [[Spring Cloud Client-Side Load Balancing]]. This is a framework implementation of [[Client-Side Service Discovery]]. Consul's address must itself be externalized and highly available; on Kubernetes, native service discovery may remove the need for an additional registry.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
