2026-10-19 22:48

Status: #baby

Tags: [[Helidon Metrics Instrumentation]]

# Helidon Metric Metadata

Helidon metric metadata describes a registered measurement with a name, description, unit, scope, and optional tags. A `MetadataBuilder` can construct this description before the registry creates a programmatic metric.

Annotations expose corresponding parameters, including whether a name is absolute or relative to the annotated class. Accurate metadata determines how a measurement is identified and explained at the metrics endpoint, not how its value is calculated.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
