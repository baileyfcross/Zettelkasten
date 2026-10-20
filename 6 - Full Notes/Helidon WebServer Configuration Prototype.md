2026-10-19 22:48

Status: #baby

Tags: [[Helidon WebServer and WebClient]]

# Helidon WebServer Configuration Prototype

`WebServerConfig` is the configuration prototype from which a Helidon `WebServer` runtime instance is created. The server implements a runtime API parameterized by that prototype, separating the description assembled by configuration from the running server built from it.

`WebServerConfig.Builder` replaces the older builder nested directly in the server interface. It can describe multiple server sockets and optional multiple routings before `build()` freezes the configuration into an immutable [[Helidon WebServer]].

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
