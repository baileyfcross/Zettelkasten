2026-11-08 16:45

Status: #baby

Tags: [[Spring Security and Identity]]

# Spring Security Reactive Filter Chain

A Spring Security reactive filter chain protects WebFlux routes through nonblocking authentication and authorization components. Matchers and OAuth resource-server configuration apply before a handler runs, while the resolved security context is carried through the reactive subscriber context rather than assumed to live in one dedicated request thread.

Functional handlers can obtain the authenticated principal from the request or reactive security context without blocking. Identity lookup and token validation must also use reactive contracts when they perform I/O. The policy goals match servlet security, but thread-local assumptions and blocking adapters can break the reactive execution model.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
