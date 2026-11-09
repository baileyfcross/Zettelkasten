2026-11-06 13:52

Status: #baby

Tags: [[Microservice Communication and Resilience]] [[Spring Cloud Operations and Native Runtime]]

# Spring Cloud Client-Side Load Balancing

Spring Cloud LoadBalancer lets a service-side HTTP or TCP client choose among instances of a logical dependency. Its default round-robin policy can distribute calls across replicas, while configuration can add timeouts, retries, backoff, caching, or a different selection algorithm.

The caller combines instance selection with discovery rather than depending on one fixed endpoint. If an instance disappears, traffic can move to a remaining instance, improving availability at the cost of redundant capacity. This mechanism belongs beside [[Client-Side Service Discovery]] and [[Service Registry]]; it does not replace health information or make a stateful service safe to call through arbitrary replicas.

In the Spring Boot 4 cloud example, a load-balanced RestClient builder resolves a logical `customer-service` hostname through Consul. Discovery supplies the healthy instance set and the load balancer replaces the logical address with a concrete endpoint. This lets replicas join or leave without changing the caller's configuration, provided registry health is accurate.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]

[[practicalmicroservicesarchitecturalpatterns.epub]]
