2026-11-06 12:32

Status: #baby

Tags: [[Cloud-Native Observability]]

# OpenTelemetry Baggage Context

OpenTelemetry baggage is a set of key-value context that can be propagated through request headers across several services. It can carry a bounded business identifier, such as an order or transaction reference, when a technical trace identifier alone cannot connect all of the user actions that belong to one process.

Baggage differs from a span attribute. Baggage travels across boundaries and can influence multiple spans; an attribute describes a particular span and is exported with telemetry rather than forwarded as request context. The propagation benefit also creates cost and risk: baggage enlarges headers, is often manually instrumented, may not cross every messaging system, and must not become a channel for sensitive payloads.

The source recommends using the lightest mechanism that answers the operational question. Search-only metadata may belong in span attributes, while a carefully selected identifier can justify baggage when it must survive an end-to-end path. [[OpenTelemetry Context Propagation]] performs the text-map injection and extraction.

# References

[[observabilityforlegacysystems_methodsandsolutionswithopentelemetry.epub]]
