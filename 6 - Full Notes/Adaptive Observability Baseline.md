2026-10-03 17:11

Status: #baby

Tags: [[Cloud-Native Reliability and Service Objectives]]

# Adaptive Observability Baseline

An adaptive observability baseline models normal behavior from historical data and identifies values outside an expected range. A rolling baseline can update continuously, a multidimensional baseline can separate endpoints or regions, and a seasonal baseline can distinguish business hours, weekends, or holidays.

Baselines are useful when autoscaling and variable demand make one fixed threshold impractical. They still require validation: an algorithm can learn a degraded condition as normal, and an anomaly is only a prompt for investigation until impact and context are established.

# References

[[observabilityintheai-nativeera.pdf]]
