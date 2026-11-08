2026-11-08 14:08

Status: #baby

Tags: [[Cloud-Native Observability]]

# MicroProfile Telemetry Instrumentation Modes

MicroProfile Telemetry supports automatic, manual, and optional agent-based instrumentation for Jakarta EE applications. Once telemetry is enabled, automatic instrumentation creates traces for Jakarta REST endpoints and client calls and propagates trace context without application code changes.

Manual instrumentation adds spans to CDI-aware methods with WithSpan and SpanAttribute annotations or uses an injected OpenTelemetry Tracer for direct control over span lifecycle, attributes, errors, and status. An implementation may also attach a Java agent to instrument supported libraries without modifying the application. These modes can be combined, with sampling, export, batching, and resource identity controlled through configuration.

# References

[[procloud-nativejavaeeapps_devopswithmicroprofilejakartaee11apisand.epub]]
