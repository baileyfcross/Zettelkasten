2026-09-27 22:21

Status: #baby

Tags: [[Cloud-Native Observability]]

# Distributed Request Trace

A distributed request trace records the end-to-end path of one request through several services. A trace identifier joins the journey, while each service contributes a span that records its portion of the work and the time it consumed.

The assembled timeline reveals where latency or failure occurred in a microservice call chain. Metrics can identify that a service is slow and logs can explain an individual event; the trace shows which dependency or operation dominated the user's request. [[OpenTelemetry Trace Instrumentation]] supplies spans that a backend such as [[Jaeger Trace Visualization|Jaeger]] can assemble and display.

# References

[[clouddevopsengineersguide.pdf]]

