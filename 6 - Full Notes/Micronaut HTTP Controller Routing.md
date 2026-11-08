2026-11-08 16:00

Status: #baby

Tags: [[Micronaut REST Application Framework]]

# Micronaut HTTP Controller Routing

A Micronaut HTTP controller declares a base route with Controller and maps Java methods to HTTP operations through annotations such as Get, Post, Put, and Delete. Method-level paths extend the controller path, and template values can be bound to method parameters.

This annotation model keeps the public route and verb near the method that handles them. The controller can delegate its work to an injected service or repository, leaving route selection and response conversion at the HTTP boundary rather than mixing them with persistence behavior.

# References

[[prorestfulapiswithmicronaut.epub]]
