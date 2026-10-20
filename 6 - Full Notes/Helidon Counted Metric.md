2026-10-19 22:48

Status: #baby

Tags: [[Helidon Metrics Instrumentation]]

# Helidon Counted Metric

Helidon's `@Counted` annotation marks a method, constructor, or class whose invocations should increment a counter in the applicable metric registry. A named method annotation creates a metric associated with that invocation point, while a class annotation creates counters for its constructors and methods.

The counter increases monotonically as the annotated operation runs. If code invokes an annotated element after its expected metric has disappeared from the registry, the implementation reports an illegal state rather than silently recreating unrelated measurement history.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
