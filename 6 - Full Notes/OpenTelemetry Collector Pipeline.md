2026-10-03 17:11

Status: #baby

Tags: [[Observability Signals and Semantic Context]]

# OpenTelemetry Collector Pipeline

An OpenTelemetry Collector pipeline receives telemetry from instrumented applications and other sources, processes it, and exports it to one or more storage or analysis backends. Receivers define inputs, processors normalize, enrich, sample, or filter data, and exporters define destinations.

The collector is vendor-neutral infrastructure rather than an observability database. It can reduce duplication and move context enrichment out of individual applications, but it must itself be sized and monitored so unhealthy receivers, dropped signals, or saturated exporters do not silently create blind spots.

# References

[[observabilityintheai-nativeera.pdf]]
