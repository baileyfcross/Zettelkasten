2026-10-19 22:48

Status: #baby

Tags: [[MicroProfile and Jakarta Standards]]

# MicroProfile OpenAPI Endpoint

MicroProfile OpenAPI provides Java interfaces and programming models for producing an OpenAPI description from a JAX-RS application. The resulting language-neutral contract lets people and tools discover REST operations without reading source code or inferring behavior from captured traffic.

A compatible MicroProfile implementation automatically exposes the description at `/openapi`. This makes the generated document an operational endpoint tied to the running service and connects it to the broader [[OpenAPI and Swagger]] contract model.

OpenAPI annotations can keep high-level metadata, resource descriptions, parameters, operations, and response contracts next to Jakarta REST code. Runtime generation reduces the distance between implementation and documentation, but the annotations must still describe actual status codes and representations if the endpoint is to remain trustworthy.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]

[[procloud-nativejavaeeapps_devopswithmicroprofilejakartaee11apisand.epub]]
