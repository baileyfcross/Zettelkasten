2026-10-19 22:48

Status: #baby

Tags: [[Helidon Configuration System]]

# Helidon Config Tree

Helidon `Config` is an immutable tree that loads and processes external configuration properties for an application. A node can be selected by a key path and converted to a scalar, list, subtree, or mapped Java type without exposing the original file representation to consuming code.

Calling `Config.create()` uses default classpath files and the runtime environment, while the source-accepting form adds explicitly selected inputs. The tree becomes the shared representation through which components such as WebServer, WebClient, DB Client, and Security receive their configuration.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
