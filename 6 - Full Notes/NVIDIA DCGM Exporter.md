2026-09-29 22:24

Status: #baby

Tags: [[Kubernetes GPU Allocation and Sharing]]

# NVIDIA DCGM Exporter

NVIDIA DCGM Exporter exposes Data Center GPU Manager telemetry in a Prometheus-compatible format. It reports measures such as utilization, memory use, temperature, power, and health for accelerators visible on Kubernetes nodes.

The exporter is appropriate when drivers and device support already exist and only monitoring needs to be added. Its metrics can support dashboards, alerts, and custom autoscaling, but thresholds should distinguish sustained saturation from short training or inference bursts.

# References

[[kubernetesforgenerativeaisolutions.pdf]]

