2026-10-19 22:48

Status: #baby

Tags: [[Helidon WebServer and WebClient]]

# Helidon WebClient Configuration

Helidon WebClient configuration controls connection and read timeouts, redirect following and limits, cookies, default headers, base addressing, and registered client services. These values can be supplied directly to the builder or loaded from a `client` subtree in application configuration.

The external form allows an environment to adjust network behavior without rewriting the client code. The builder combines that subtree with programmatic choices such as a base URI and a [[Helidon WebClient Metrics Service]] before producing the client.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
