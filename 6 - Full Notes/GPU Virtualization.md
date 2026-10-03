2026-10-03 16:51

Status: #baby

Tags: [[GPU Virtualization and DPU Offload]]

# GPU Virtualization

GPU virtualization divides or schedules physical accelerator capacity so separately managed guests, users, or workloads can consume virtual GPU resources. It improves utilization when a full dedicated device would leave compute or memory idle.

The service boundary matters. [[NVIDIA vGPU]] presents resources through a hypervisor to virtual machines, while [[NVIDIA Multi-Instance GPU|MIG]] creates predefined hardware partitions. Isolation, performance predictability, licensing, lifecycle management, and the tenant delivery model determine which approach fits.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

