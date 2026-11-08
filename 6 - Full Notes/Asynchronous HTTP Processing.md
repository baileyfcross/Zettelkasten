2026-11-06 13:52

Status: #baby

Tags: [[Microservice Communication and Resilience]]

# Asynchronous HTTP Processing

Asynchronous HTTP processing releases a server's request worker while a potentially blocking operation is incomplete, then completes the response from another execution context. The HTTP connection may remain open, but the container thread becomes available for other requests instead of waiting on a remote service or slow I/O.

In Spring MVC, a controller can return a `Callable`, `DeferredResult`, or `CompletableFuture`. `DeferredResult` is useful when an external thread or messaging callback produces the result: the handler exits, Spring retains the response, and the later completion triggers response delivery. This improves concurrency for waiting work but does not increase the capacity of the downstream dependency, so timeouts and resource limits still matter.

# References

[[practicalmicroservicesarchitecturalpatterns.epub]]
