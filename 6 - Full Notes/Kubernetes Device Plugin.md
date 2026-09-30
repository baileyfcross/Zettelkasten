2026-09-29 22:24

Status: #baby

Tags: [[Kubernetes GPU Allocation and Sharing]]

# Kubernetes Device Plugin

A Kubernetes device plugin runs on applicable nodes, registers a vendor-specific extended resource with the kubelet, reports available devices, prepares allocated hardware for containers, and updates health. The kubelet publishes the resulting allocatable resource to the API server for scheduling.

The plugin makes an accelerator schedulable but does not install every required driver or library. The node image, container runtime, device plugin, workload image, and requested resource name must form a compatible chain before a model pod can use the hardware.

# References

[[kubernetesforgenerativeaisolutions.pdf]]

