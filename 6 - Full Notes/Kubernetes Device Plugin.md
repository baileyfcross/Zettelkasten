2026-09-29 22:24

Status: #baby

Tags: [[Kubernetes GPU Allocation and Sharing]] · [[NVIDIA GPU Sharing and Fleet Management]]

# Kubernetes Device Plugin

A Kubernetes device plugin runs on applicable nodes, registers a vendor-specific extended resource with the kubelet, reports available devices, prepares allocated hardware for containers, and updates health. The kubelet publishes the resulting allocatable resource to the API server for scheduling.

The plugin makes an accelerator schedulable but does not install every required driver or library. The node image, container runtime, device plugin, workload image, and requested resource name must form a compatible chain before a model pod can use the hardware.

For MIG, hardware configuration creates the available instance shapes and the NVIDIA device plugin advertises them according to its selected strategy. This separates device partitioning from resource discovery and from the scheduler's later placement decision.

# References

[[kubernetesforgenerativeaisolutions.pdf]]

[[nvidiagpuinfrastructurefundamentals.pdf]]
