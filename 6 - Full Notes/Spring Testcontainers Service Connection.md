2026-11-08 16:45

Status: #baby

Tags: [[Spring Application Testing]] [[Docker Development and Testing]]

# Spring Testcontainers Service Connection

A Spring Testcontainers service connection recognizes a managed container's service type and contributes the corresponding dynamic connection details to the Boot application context. A MongoDB, RabbitMQ, Kafka, or compatible database container can therefore replace manually copied host, port, username, and password properties in an integration test.

The mechanism builds on [[Testcontainers Integration Testing]] and reduces configuration code, but the container still needs an explicit lifecycle and a compatible image. Running the real engine catches behavior an embedded substitute can miss. A test-aware application launcher can also start the production main method with those containers for a zero-install local development environment.

In the source's Redis example, `@Testcontainers` enables lifecycle support, a static `@Container` declares the managed dependency, and `@ServiceConnection` supplies its connection information to the Spring context. The test therefore needs neither a preinstalled Redis process nor a fixed `application-test.properties` host and port.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]

[[whendockermeetsjava_apracticalguidetodockerforjavaandspringbootapp.epub]]
