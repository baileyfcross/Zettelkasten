2026-10-19 22:48

Status: #baby

Tags: [[MicroProfile and Jakarta Standards]]

# Jakarta EE Core Profile

The Jakarta EE Core Profile is a minimal standards base for cloud-native runtimes, including runtimes that perform application work at build time. Jakarta EE 10 introduced it to support smaller deployments, microservices, and ahead-of-time compilation.

Its specifications include RESTful Web Services, JSON Processing, JSON Binding, Contexts and Dependency Injection, Dependency Injection, Interceptors, and Annotations. This set overlaps the foundational standards that let MicroProfile applications expose resources, exchange JSON, and manage components without requiring the entire Jakarta EE Platform.

This overlap gives MicroProfile a portable Jakarta programming base while its own specifications add cloud-native concerns such as external configuration, fault tolerance, health, JWT, API description, and telemetry. A small runtime can implement the profile and the relevant MicroProfile APIs without presenting every full-platform facility.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]

[[procloud-nativejavaeeapps_devopswithmicroprofilejakartaee11apisand.epub]]
