2026-10-19 22:48

Status: #baby

Tags: [[MicroProfile and Jakarta Standards]]

# MicroProfile Type-Safe REST Client

The MicroProfile Rest Client specification defines a type-safe way for Java code to invoke REST services over HTTP. Instead of assembling each request as unrelated strings, an application can describe resource paths and HTTP operations through Java contracts aligned with Jakarta RESTful Web Services.

This preserves the endpoint structure in code while leaving the runtime responsible for the client invocation. It belongs to the declarative, standards-based side of [[Helidon MP Programming Model]], whereas the SE model provides the programmatic [[Helidon WebClient]].

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
