2026-10-19 22:48

Status: #baby

Tags: [[MicroProfile and Jakarta Standards]]

# MicroProfile Config Externalization

MicroProfile Config externalizes microservice settings into environment variables, system properties, or property files. A value can be injected at runtime with `@ConfigProperty`, allowing environment or lifecycle-stage differences to change without rebuilding and repackaging the application.

The conventional file is `microprofile-config.properties`, although another application property file can be used by a runtime. In a Helidon MP quickstart, server host and port, optional metric behavior, and an application greeting share this external configuration boundary.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
