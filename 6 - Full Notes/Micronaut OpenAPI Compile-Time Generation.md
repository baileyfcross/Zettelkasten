2026-11-08 16:00

Status: #baby

Tags: [[Micronaut REST Application Framework]]

# Micronaut OpenAPI Compile-Time Generation

Micronaut OpenAPI uses an annotation processor and OpenAPI annotations to produce a machine-readable API description during compilation. Application metadata can declare a title, version, description, license, and contact while schema annotations describe exposed model types.

The generated YAML is placed under the build's META-INF Swagger output. Static-resource routing can publish that artifact through an HTTP path, giving consumers access to the compiled contract without hand-copying it into a separate documentation project.

# References

[[prorestfulapiswithmicronaut.epub]]
