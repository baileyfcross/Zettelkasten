2026-09-29 22:24

Status: #baby

Tags: [[Kubernetes GPU Allocation and Sharing]] · [[NVIDIA GPU Sharing and Fleet Management]]

# NVIDIA DCGM Exporter

NVIDIA DCGM Exporter exposes Data Center GPU Manager telemetry in a Prometheus-compatible format. It reports measures such as utilization, memory use, temperature, power, and health for accelerators visible on Kubernetes nodes.

The exporter is appropriate when drivers and device support already exist and only monitoring needs to be added. Its metrics can support dashboards, alerts, and custom autoscaling, but thresholds should distinguish sustained saturation from short training or inference bursts.

Within DCGM's operating model, the exporter is one consumer of data gathered by the [[DCGM Host Engine]]. Prometheus stores the labeled time series and Grafana presents them, while workload metadata lets operators connect a device or MIG-instance signal to a node, pod, namespace, or service.

# References

[[kubernetesforgenerativeaisolutions.pdf]]

[[nvidiagpuinfrastructurefundamentals.pdf]]
