2026-09-29 22:24

Status: #baby

Tags: [[Kubernetes GPU Allocation and Sharing]]

# NVIDIA GPU Operator

The NVIDIA GPU Operator automates Kubernetes GPU software through the operator pattern. It can manage drivers, the container runtime integration, device plugin, node labeling, DCGM monitoring, and configuration needed to make NVIDIA accelerators usable.

Central automation reduces node-by-node drift, but it also becomes part of the cluster's critical upgrade path. Operator, driver, CUDA, hardware, and Kubernetes compatibility should be tested before rollout, especially when active inference workloads depend on a specific version.

# References

[[kubernetesforgenerativeaisolutions.pdf]]

