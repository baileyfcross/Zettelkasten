2026-10-19 22:48

Status: #baby

Tags: [[MicroProfile and Jakarta Standards]]

# MicroProfile Config Externalization

MicroProfile Config externalizes microservice settings into environment variables, system properties, or property files. A value can be injected at runtime with `@ConfigProperty`, allowing environment or lifecycle-stage differences to change without rebuilding and repackaging the application.

The conventional file is `microprofile-config.properties`, although another application property file can be used by a runtime. In a Helidon MP quickstart, server host and port, optional metric behavior, and an application greeting share this external configuration boundary.

The specification presents configuration as config sources, converters, and values. System properties, environment variables, and application properties have descending default ordinals, so deployment-level settings can override packaged defaults. Applications can inject a value directly, request an Optional for absence, or use a Provider or Supplier when each access must resolve the latest value.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]

[[procloud-nativejavaeeapps_devopswithmicroprofilejakartaee11apisand.epub]]
