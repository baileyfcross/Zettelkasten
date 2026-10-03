2026-09-29 22:24

Status: #baby

Tags: [[Kubernetes GPU Allocation and Sharing]] · [[NVIDIA GPU Sharing and Fleet Management]]

# GPU Resource Request in Kubernetes

A GPU resource request in Kubernetes uses a vendor extended-resource name such as `nvidia.com/gpu` in the container resource limits. The scheduler places the pod on a node advertising enough devices, often combined with a node selector and a toleration for GPU-node taints.

The book notes that GPU resources must be declared in limits, either alone or with an equal request. A successful placement also requires a compatible device plugin, host driver, container runtime, and workload image; the manifest cannot create missing hardware support.

The request can be combined with labels, selectors, affinity, taints, tolerations, and namespace quotas to express model, memory, topology, tenancy, or service-tier constraints. MIG resources require the node geometry and advertised profile name to match what the pod requests.

# References

[[kubernetesforgenerativeaisolutions.pdf]]

[[nvidiagpuinfrastructurefundamentals.pdf]]
