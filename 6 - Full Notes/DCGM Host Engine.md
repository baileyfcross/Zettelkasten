2026-10-03 16:51

Status: #baby

Tags: [[NVIDIA GPU Sharing and Fleet Management]]

# DCGM Host Engine

The DCGM host engine is the central service that gathers NVIDIA GPU fleet data and exposes discovery, telemetry, diagnostics, health, and policy capabilities to management clients. It separates continuous device collection from each tool that consumes the information.

The [[dcgmi CLI]] and programming interfaces can query the service, while an exporter can translate selected signals for Prometheus. This shared source keeps interactive diagnosis, automated rules, and dashboards anchored to the same device and MIG-instance observations.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

