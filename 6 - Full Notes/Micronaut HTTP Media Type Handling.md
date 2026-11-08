2026-11-08 16:00

Status: #baby

Tags: [[Micronaut REST Application Framework]]

# Micronaut HTTP Media Type Handling

Micronaut controllers can declare the representation they produce and can set a response's content type explicitly. The book demonstrates separate endpoints returning the same message as a Java object serialized to JSON and as an explicitly constructed XML response.

The declared media type forms part of the HTTP contract: it tells the runtime and client how to interpret the entity. Supporting JSON and XML does not create two conceptual resources; it creates two representations whose availability should agree with routing and content-negotiation policy.

# References

[[prorestfulapiswithmicronaut.epub]]
