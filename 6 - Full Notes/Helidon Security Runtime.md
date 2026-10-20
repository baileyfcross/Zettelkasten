2026-10-19 22:48

Status: #baby

Tags: [[Helidon Security Integration]]

# Helidon Security Runtime

The Helidon Security runtime coordinates authentication, authorization, audit, and outbound security. The `Security` interface bootstraps those capabilities, integrates them with other Helidon components, and serves as the main runtime entry point for security contexts.

The runtime separates a security decision from the web handler that consumes its result. WebServer integration can require authentication and roles before a handler runs, while application code can inspect the resulting [[Helidon Security Context]] when it needs the caller's identity.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
