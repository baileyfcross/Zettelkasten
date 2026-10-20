2026-10-19 22:48

Status: #baby

Tags: [[Helidon WebServer and WebClient]]

# Helidon WebServer

Helidon WebServer is an immutably configured HTTP server for SE applications. Its API combines server lifecycle and monitoring with listener configuration, routing, error handling, metrics, and health endpoints, and `start()` activates the completed server instance.

Helidon 4 rebuilt this component on [[Helidon Nima Virtual-Thread Runtime]] rather than the Netty-based reactive server used by earlier release trains. A server can be created from an existing `WebServerConfig` or from a builder consumer that customizes the configuration.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
