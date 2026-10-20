2026-10-19 22:48

Status: #baby

Tags: [[Helidon WebServer and WebClient]]

# Helidon WebServer External Configuration

External WebServer configuration loads host, port, and related settings from a Helidon `Config` tree and supplies the `server` node to the server builder. The conventional source is `application.yaml`, although supported property or configuration formats can provide the same subtree.

This separates deployment-specific listener settings from Java routing logic. The application can register routes in code while changing the listening address without recompiling, using the facilities described by [[Helidon Configuration System]].

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
