2026-10-19 22:48

Status: #baby

Tags: [[Helidon Metrics Instrumentation]]

# Helidon Prometheus Metrics Format

Helidon metric endpoints use Prometheus text format by default. Comment-like lines beginning with `# HELP` document a metric, while `# TYPE` declares it as a counter, gauge, histogram, summary, or untyped measurement before samples are listed.

Samples carry values and optional label pairs such as `mp_scope`, a histogram unit, or a response-status range. Metric names are normalized for exposition—for example, dotted base names become underscore-separated—while the scope remains an explicit label.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
