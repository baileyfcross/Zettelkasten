2026-10-30 17:24

Status: #baby

Tags: [[Spring Microservice Application Architecture]]

# Spring REST Controller Adapter

A Spring REST controller is a driving adapter that turns HTTP requests and JSON payloads into calls on application services. Request mappings associate routes and HTTP methods with Java methods, and the returned domain or representation objects become HTTP responses.

The controller belongs at the delivery boundary rather than inside the domain model. Its responsibility is protocol and format translation, leaving business behavior and persistence to inner services and driven ports.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

