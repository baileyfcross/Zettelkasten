2026-09-29 22:24

Status: #baby

Tags: [[GenAI Observability on Kubernetes]]

# Grafana GenAI Operations Dashboard

A Grafana GenAI operations dashboard combines cluster, pod, application, GPU, log, and trace views for a serving path. Panels can relate request latency and error rate to replica count, token throughput, accelerator utilization, and the model version in service.

The dashboard is an investigation surface rather than an availability mechanism. Queries, variables, units, data-source permissions, and alert links should be versioned, and tenants should not gain visibility into another application's prompts or model telemetry through a shared workspace.

# References

[[kubernetesforgenerativeaisolutions.pdf]]

