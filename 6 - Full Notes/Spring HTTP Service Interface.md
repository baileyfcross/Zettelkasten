2026-11-08 16:45

Status: #baby

Tags: [[Spring Web and Service Interfaces]]

# Spring HTTP Service Interface

A Spring HTTP service interface declares an outbound REST client as a focused Java contract. Type-level and method-level exchange annotations describe the base path, HTTP method, path variables, and return type, while `@ImportHttpServices` causes Spring to generate and register the proxy implementation.

The proxy uses a configured [[Spring RestClient]] so request construction stays at the adapter boundary. URLs should come from external configuration, and timeouts still require deliberate client settings. Small interfaces preserve service-specific contracts better than one general remote-client type and can return records, response wrappers, or reactive types according to the calling boundary.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
