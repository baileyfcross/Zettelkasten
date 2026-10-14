2026-09-29 22:24

Status: #baby

Tags: [[Kubernetes GPU Allocation and Sharing]] · [[NVIDIA GPU Sharing and Fleet Management]]

# NVIDIA Multi-Instance GPU

NVIDIA Multi-Instance GPU partitions supported physical hardware into independent instances with dedicated memory and compute slices. Kubernetes can advertise named MIG profiles as extended resources and schedule pods against a profile that matches their required partition.

MIG provides stronger isolation and more predictable performance than software-only sharing, but the available shapes are constrained by the GPU model and active partition layout. Reconfiguration and scheduling must consider how profiles consume the device's finite slices.

Each [[MIG Profile]] is a predefined compute-and-memory shape for the installed GPU configuration. Platform operation therefore separates three steps: configure the device geometry, advertise the resulting resources through a device plugin, and schedule workloads against an available profile.

# References

[[kubernetesforgenerativeaisolutions.pdf]]

[[nvidiagpuinfrastructurefundamentals.pdf]]
