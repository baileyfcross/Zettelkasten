2026-09-29 22:24

Status: #baby

Tags: [[Kubernetes GPU Allocation and Sharing]]

# GPU Resource Request in Kubernetes

A GPU resource request in Kubernetes uses a vendor extended-resource name such as `nvidia.com/gpu` in the container resource limits. The scheduler places the pod on a node advertising enough devices, often combined with a node selector and a toleration for GPU-node taints.

The book notes that GPU resources must be declared in limits, either alone or with an equal request. A successful placement also requires a compatible device plugin, host driver, container runtime, and workload image; the manifest cannot create missing hardware support.

# References

[[kubernetesforgenerativeaisolutions.pdf]]

