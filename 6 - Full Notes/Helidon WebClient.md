2026-10-19 22:48

Status: #baby

Tags: [[Helidon WebServer and WebClient]]

# Helidon WebClient

Helidon WebClient is the SE component for processing HTTP requests and responses against an endpoint. It complements WebServer, Config, and Security and can be created with defaults, from a `WebClientConfig`, or through a builder consumer.

The original client was reactive to pair with the earlier Netty server. Helidon 4 changed it to a blocking, synchronous API aligned with [[Helidon Nima Virtual-Thread Runtime]], while retaining builder-based configuration, redirect handling, security, tracing, and metrics integration.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
