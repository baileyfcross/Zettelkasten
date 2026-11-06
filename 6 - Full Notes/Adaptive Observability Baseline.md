2026-10-03 17:11

Status: #baby

Tags: [[Cloud-Native Reliability and Service Objectives]]

# Adaptive Observability Baseline

An adaptive observability baseline models normal behavior from historical data and identifies values outside an expected range. A rolling baseline can update continuously, a multidimensional baseline can separate endpoints or regions, and a seasonal baseline can distinguish business hours, weekends, or holidays.

Baselines are useful when autoscaling and variable demand make one fixed threshold impractical. They still require validation: an algorithm can learn a degraded condition as normal, and an anomaly is only a prompt for investigation until impact and context are established.

The current source adds detector interval and evidence maturity to that validation. Short intervals respond quickly but can learn ordinary workload fluctuations as anomalies; longer intervals smooth noise but increase detection latency. [[Anomaly Grade and Confidence]] should be retained with the entity and time bucket so a strong deviation learned from little data is not treated as equivalent to a well-established pattern.

# References

[[observabilityintheai-nativeera.pdf]]
[[observabilityforlegacysystems_methodsandsolutionswithopentelemetry.epub]]
