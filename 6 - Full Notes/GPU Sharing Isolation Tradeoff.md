2026-09-29 22:24

Status: #baby

Tags: [[Kubernetes GPU Allocation and Sharing]] · [[NVIDIA GPU Sharing and Fleet Management]]

# GPU Sharing Isolation Tradeoff

The GPU sharing isolation tradeoff compares fixed hardware partitions, concurrent process sharing, and scheduled time slices. MIG dedicates memory and compute slices, MPS shares execution among CUDA processes, and time-slicing alternates access with minimal capacity guarantees.

Choosing among them requires workload evidence. Multi-tenant or latency-sensitive inference benefits from predictable isolation, while cooperative notebooks or bursty small models may value higher aggregate utilization even when individual performance varies.

NVIDIA vGPU adds a separate comparison at the hypervisor boundary: it presents accelerator resources to virtual machines, whereas MIG first partitions supported hardware. The delivery model, tenant trust, performance predictability, and management layer determine which boundary is appropriate.

# References

[[kubernetesforgenerativeaisolutions.pdf]]

[[nvidiagpuinfrastructurefundamentals.pdf]]
