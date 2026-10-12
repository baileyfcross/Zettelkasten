2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Monitoring and Log Operations]]

# PromQL for Kubernetes

PromQL selects, filters, aggregates, and transforms Prometheus time series. In Kubernetes, label joins and aggregations can turn per-container counters into namespace request rates, workload error ratios, node saturation, or other operational views.

Counter metrics generally need rate calculations over a time window, while gauges can be inspected or aggregated directly. Query correctness depends on label semantics and missing-series behavior, so a visually plausible graph should be validated against the events it claims to represent.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

