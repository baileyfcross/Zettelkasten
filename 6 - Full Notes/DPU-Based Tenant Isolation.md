2026-10-03 16:51

Status: #baby

Tags: [[GPU Virtualization and DPU Offload]]

# DPU-Based Tenant Isolation

DPU-based tenant isolation places selected network, storage, encryption, inspection, and telemetry controls outside the tenant operating system. The independently managed DPU forms a node-level boundary that a guest or container cannot simply reconfigure from within its own workload environment.

This isolation addresses a different layer from [[NVIDIA Multi-Instance GPU|MIG]] or [[NVIDIA vGPU]]. MIG separates hardware accelerator resources, vGPU separates VM-visible access, and a DPU protects and observes the infrastructure data path surrounding those tenants.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

