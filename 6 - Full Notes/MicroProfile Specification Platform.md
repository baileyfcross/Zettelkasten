2026-10-19 22:48

Status: #baby

Tags: [[MicroProfile and Jakarta Standards]]

# MicroProfile Specification Platform

MicroProfile is a suite of specifications for optimizing enterprise Java for microservice architectures. It began as a collaboration among middleware vendors and a Java user community with goals of vendor-neutral governance, portable behavior, compatible implementations, and a consistent view across application tiers.

The initial platform combined CDI, JSON Processing, and RESTful Web Services, then added cloud-oriented capabilities such as configuration, fault tolerance, metrics, health, JWT propagation, API description, client calls, messaging, context propagation, GraphQL, long-running actions, and telemetry. [[Helidon MP Programming Model]] implements this standards-oriented model.

The specifications address concerns that a Jakarta EE microservice otherwise would implement separately: configuration source resolution, resilience annotations, runtime health signals, token-to-container identity, type-safe outbound clients, OpenAPI description, and OpenTelemetry-aligned tracing. Their value is the common contract across compatible runtimes rather than one vendor's convenience API.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]

[[procloud-nativejavaeeapps_devopswithmicroprofilejakartaee11apisand.epub]]
