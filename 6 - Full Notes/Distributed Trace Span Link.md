2026-11-06 12:32

Status: #baby

Tags: [[Cloud-Native Observability]]

# Distributed Trace Span Link

A distributed trace span link records a relationship to another span without making that span the single parent. It is useful when one operation consumes several messages, combines parallel work, aggregates events, or otherwise depends on spans from multiple traces.

For a message batch, instrumentation can extract each message's trace context and attach a link from the processing span to every contributing message. This preserves evidence that a parent-child tree cannot express and avoids inventing one causal parent for a many-input operation. Backend support varies, so the relationship must be verified in the selected [[Jaeger Trace Visualization|trace visualization]] or other store.

A link does not merge or repair a broken trace. [[OpenTelemetry Context Propagation]] continues causal context when the protocol supports it; a span link explicitly records an additional relationship when continuation would be misleading or impossible.

# References

[[observabilityforlegacysystems_methodsandsolutionswithopentelemetry.epub]]
