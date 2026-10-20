2026-10-19 22:48

Status: #baby

Tags: [[Helidon WebServer and WebClient]]

# Helidon HTTP Routing

Helidon HTTP routing composes request-response handlers with matching rules. A route associates an HTTP method and optional path pattern with one or more handlers that implement the application's behavior for matching requests.

`HttpRouting` extends the general routing lifecycle and supplies a builder with methods such as `get`, `put`, `post`, `head`, and `any`. It can combine individual handlers with registered service objects, allowing a [[Helidon WebServer]] to mount simple lambdas and larger endpoint groups in the same routing graph.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
