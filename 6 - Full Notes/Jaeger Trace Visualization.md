2026-09-27 22:21

Status: #baby

Tags: [[Cloud-Native Observability]]

# Jaeger Trace Visualization

Jaeger is a tracing backend that receives spans and presents the reconstructed request as a timeline across services. Its waterfall view makes the relative duration and ordering of operations visible, helping an investigator locate a slow database call or failing downstream service.

Jaeger depends on consistent trace context and [[OpenTelemetry Trace Instrumentation|instrumentation]] from the participating applications. A local all-in-one instance can support experimentation, while production use needs deliberate storage, retention, access, and sampling. A clear visualization cannot repair missing or incorrectly propagated spans.

# References

[[clouddevopsengineersguide.pdf]]

