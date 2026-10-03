2026-10-03 16:51

Status: #baby

Tags: [[GPU Virtualization and DPU Offload]]

# DPU Security Offload

DPU security offload enforces encryption, inspection, segmentation, access policy, or firewall functions on a processor outside the tenant operating system. Placing controls at the network and storage boundary preserves host CPU capacity and makes policy harder for a compromised guest to disable.

The design supports zero-trust and multi-tenant platforms by adding an independently managed enforcement point. It complements, rather than replaces, hypervisor, Kubernetes, network, identity, and GPU-partition controls at other layers.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

