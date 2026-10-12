2026-09-27 11:11

Status: #baby

Tags: [[.NET Microservice Communication and Workers]]

# Typed HTTP Client

A typed HTTP client wraps `HttpClient` in a class whose methods express operations against one remote service. The class owns the base address, request construction, response parsing, and service-specific failure handling, while callers depend on its domain-oriented interface.

Registering the typed client through `IHttpClientFactory` centralizes handler management and configuration. It also provides a natural attachment point for resilience policies such as bounded retries or circuit breaking.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
