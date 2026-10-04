2026-10-03 17:11

Status: #baby

Tags: [[Cloud-Native Reliability and Service Objectives]]

# Static Threshold Suitability

A static threshold is suitable when a system has a known boundary whose meaning does not drift with ordinary workload variation. API rate limits, worker-thread ceilings, queue capacities, contractual objectives, and predictable latency or retry limits are examples.

Applying fixed limits to every dynamic infrastructure metric produces large maintenance burdens and false alarms. Elastic systems often need [[Adaptive Observability Baseline|adaptive baselines]] for changing behavior while preserving static thresholds for hard limits and clearly defined commitments.

# References

[[observabilityintheai-nativeera.pdf]]
