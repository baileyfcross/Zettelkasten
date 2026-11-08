2026-09-27 22:21

Status: #baby

Tags: [[Cloud-Native Observability]] [[Docker Observability Operations]]

# OpenTelemetry Trace Instrumentation

OpenTelemetry trace instrumentation adds a common mechanism for applications to create and export spans. Language SDKs can instrument common frameworks and propagate trace context as a request crosses service boundaries, keeping independently executed operations connected to one [[Distributed Request Trace]].

Instrumentation is the evidence-producing layer rather than the analysis interface. Spans are forwarded through a supported protocol to a tracing backend, where they are stored and assembled. The application must still choose useful operation names and attributes without recording sensitive payloads or generating more high-cardinality data than the backend can sustain.

OpenTelemetry instrumentation gives containerized applications a vendor-neutral way to emit trace context and spans. Exporting through a collector decouples application code from a particular backend and lets deployment configuration control batching, enrichment, and routing.

The legacy-systems source separates four responsibilities that are easy to conflate: instrument the relevant method, extract incoming context, inject and propagate outgoing context, and transfer completed spans to storage. Known frameworks may be handled automatically, while custom Java code or unsupported middleware can require an [[OpenTelemetry Java Agent Extension]]. A successful export does not prove continuity; propagation format and parent relationships must be tested across every service and messaging boundary.

MicroProfile Telemetry integrates OpenTelemetry with the Jakarta EE programming model. It can instrument Jakarta REST endpoints and clients automatically, add spans declaratively to CDI methods, expose the Tracer for explicit span lifecycle and error recording, or use an optional Java agent for supported libraries. Sampling, batching, service attributes, and OTLP export remain deployment configuration rather than fixed application logic.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]

[[clouddevopsengineersguide.pdf]]

[[observabilityforlegacysystems_methodsandsolutionswithopentelemetry.epub]]

[[procloud-nativejavaeeapps_devopswithmicroprofilejakartaee11apisand.epub]]

