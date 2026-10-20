2026-10-19 22:48

Status: #baby

Tags: [[Helidon Metrics Instrumentation]]

# Helidon Gauge Metric

Helidon's `@Gauge` annotation exposes the current numeric value returned by a field or method. Unlike a counter, the value is managed by application code and can rise or fall between observations.

The example records application uptime by capturing the application-scope initialization event and returning elapsed seconds from the annotated method. Its unit becomes part of the metric name and exposition metadata.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
