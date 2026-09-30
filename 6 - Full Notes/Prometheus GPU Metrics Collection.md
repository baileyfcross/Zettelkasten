2026-09-29 22:24

Status: #baby

Tags: [[GenAI Observability on Kubernetes]]

# Prometheus GPU Metrics Collection

Prometheus GPU metrics collection discovers DCGM Exporter targets and scrapes labeled time series for accelerator utilization, memory, temperature, power, and health. Kubernetes metadata connects a device measurement to the node and workload using it.

The series can drive dashboards, alerts, and KEDA or adapter-backed autoscaling. Averages can hide one saturated device among idle peers, so queries should preserve device and pod dimensions before aggregating them for capacity decisions.

# References

[[kubernetesforgenerativeaisolutions.pdf]]

