2026-10-19 22:48

Status: #baby

Tags: [[Helidon Metrics Instrumentation]]

# Helidon Timed Metric

Helidon's `@Timed` annotation measures the frequency and duration distribution of invocations for a method, constructor, or class. Each execution contributes a duration to an underlying timer that produces count and timing statistics.

A resource method can combine `@Timed` with `@Counted` so the same endpoint reports both invocation volume and latency behavior. Name, description, unit, scope, tags, and absolute-name selection describe how the metric is registered and exposed.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
