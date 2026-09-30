2026-09-29 22:24

Status: #baby

Tags: [[GenAI Observability on Kubernetes]]

# DCGM GPU Metric

A DCGM GPU metric represents accelerator health or behavior, including compute utilization, framebuffer memory, temperature, power, and device errors. DCGM Exporter makes those measurements available with labels that Prometheus can query.

One metric is not a utilization verdict. Low compute may be paired with full memory, high power may be normal for a training phase, and a periodic spike may satisfy an interactive workload, so several measurements should be interpreted with model throughput and request latency.

# References

[[kubernetesforgenerativeaisolutions.pdf]]

