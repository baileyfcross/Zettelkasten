2026-09-27 22:21

Status: #baby

Tags: [[Cloud-Native Observability]]

# OpenTelemetry Trace Instrumentation

OpenTelemetry trace instrumentation adds a common mechanism for applications to create and export spans. Language SDKs can instrument common frameworks and propagate trace context as a request crosses service boundaries, keeping independently executed operations connected to one [[Distributed Request Trace]].

Instrumentation is the evidence-producing layer rather than the analysis interface. Spans are forwarded through a supported protocol to a tracing backend, where they are stored and assembled. The application must still choose useful operation names and attributes without recording sensitive payloads or generating more high-cardinality data than the backend can sustain.

# References

[[clouddevopsengineersguide.pdf]]

