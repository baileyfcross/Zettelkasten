2026-10-19 22:48

Status: #baby

Tags: [[Helidon Database Client]]

# Helidon DB Client Tracing

Helidon DB Client tracing is an interceptor service that creates trace information around database statements. It can be attached to the client builder so all matching operations are observed without adding tracing calls to each service method.

The example registers `DbClientTracing` alongside counter and timer services and makes the resulting database trace available to a tracing system such as Zipkin or Jaeger. Named statements give those observations a stable operation identity.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
