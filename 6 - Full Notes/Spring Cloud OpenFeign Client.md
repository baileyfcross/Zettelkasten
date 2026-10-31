2026-10-30 17:24

Status: #baby

Tags: [[Spring Microservice Application Architecture]]

# Spring Cloud OpenFeign Client

A Spring Cloud OpenFeign client declares a remote HTTP service as a Java interface. An annotation names the service or URL, and mapped interface methods describe the requests, allowing Spring Cloud to generate the concrete client adapter.

The declarative form removes repeated call construction from application code and makes the outgoing port explicit. Configuration can still supply endpoint and client behavior, while the core depends on the interface rather than a hand-written HTTP invocation sequence.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

