2026-09-29 22:24

Status: #baby

Tags: [[Kubernetes GenAI Autoscaling and Cost Control]]

# GenAI Scaling Signal

A GenAI scaling signal is a measurement that represents demand or saturation closely enough to justify changing capacity. CPU and memory are conventional signals, while request rate, queue depth, latency, token throughput, and GPU utilization can reflect model-serving demand more directly.

The metric must lead the failure it is meant to prevent. Scaling on a lagging average after latency has already collapsed may add capacity too late, especially when GPU nodes and model loading take minutes, so thresholds and stabilization windows should include provisioning delay.

# References

[[kubernetesforgenerativeaisolutions.pdf]]

