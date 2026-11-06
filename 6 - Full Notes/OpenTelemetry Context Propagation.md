2026-11-06 12:32

Status: #baby

Tags: [[Cloud-Native Observability]]

# OpenTelemetry Context Propagation

OpenTelemetry context propagation preserves a causal request relationship when execution crosses a service boundary. Instrumentation reads the current context, extracts an incoming representation from a carrier, creates or continues spans, injects the outgoing representation, and transfers completed telemetry separately to a backend.

The source distinguishes propagation across services from passing context between threads inside one process. An internal worker can receive the context directly, while an HTTP or messaging boundary needs a propagator that encodes and decodes it. OpenTelemetry uses text-map carriers and defaults to W3C trace context; a composite propagator can support additional formats such as B3 when old and new services coexist.

Correct instrumentation is as important as the header format. A missing or incompatible extraction creates a new [[Distributed Request Trace]] instead of continuing the existing one, while asynchronous messaging may require a [[Distributed Trace Span Link]] rather than a false parent-child relationship. Propagation should be tested across every protocol and agent combination used by the request path.

# References

[[observabilityforlegacysystems_methodsandsolutionswithopentelemetry.epub]]
