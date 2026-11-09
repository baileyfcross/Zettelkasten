2026-11-08 16:45

Status: #baby

Tags: [[Spring Cloud Operations and Native Runtime]]

# Spring Cloud Gateway Route

A Spring Cloud Gateway route combines predicates that match an incoming request, filters that transform or protect the exchange, and a target URI. A discovery-aware `lb://` target resolves a logical service name and forwards to a healthy instance without exposing internal addresses to the client.

Gateway implements the [[API Gateway Pattern]] on a nonblocking WebFlux and Netty core. It can centralize TLS termination, authentication, rate limiting, caching, path rewriting, and circuit-breaker fallback, but business logic should remain in downstream services. Route and connect timeouts bound the resources consumed by a slow dependency.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
