2026-10-30 17:24

Status: #baby

Tags: [[Spring Web and Service Interfaces]]

# Spring REST Controller Adapter

A Spring REST controller is a driving adapter that turns HTTP requests and JSON payloads into calls on application services. Request mappings associate routes and HTTP methods with Java methods, and the returned domain or representation objects become HTTP responses.

The controller belongs at the delivery boundary rather than inside the domain model. Its responsibility is protocol and format translation, leaving business behavior and persistence to inner services and driven ports.

The Spring Boot 4 request lifecycle places the adapter behind the DispatcherServlet, handler mapping, and handler adapter. Path variables and request bodies become method arguments, validation can fail before business code runs, and an HTTP message converter serializes the returned representation. This makes status, headers, validation, and media types controller concerns while the service remains transport-independent.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]

[[javamicroservicesandcontainersinthecloud.epub]]

