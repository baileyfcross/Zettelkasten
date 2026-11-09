2026-11-08 16:45

Status: #baby

Tags: [[Spring Web and Service Interfaces]]

# Spring WebFlux Functional Endpoint

A Spring WebFlux functional endpoint separates a router function from a handler function. The router matches an HTTP method and path and delegates the request, while the handler extracts inputs, invokes a reactive service, and maps the resulting publisher into a `ServerResponse`.

This is an explicit alternative to annotation-based reactive controllers, not a different runtime. Both execute on WebFlux and should preserve a nonblocking chain through remote and data access. Functional routing can make route composition and filters visible in configuration, while handlers remain focused on protocol translation rather than business orchestration.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
