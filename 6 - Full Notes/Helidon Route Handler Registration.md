2026-10-19 22:48

Status: #baby

Tags: [[Helidon WebServer and WebClient]]

# Helidon Route Handler Registration

The Helidon routing builder can attach handlers directly to an HTTP method or register an `HttpService` beneath a path prefix. Direct registration suits a compact endpoint, while service registration delegates a related group of route rules to one object.

For example, a greeting service can be mounted under `/greet` while a lambda handles `/simple-greet`. The registered service then defines relative paths such as `/`, `/{name}`, and `/greeting`, so the outer prefix and inner rules compose into complete endpoints.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
