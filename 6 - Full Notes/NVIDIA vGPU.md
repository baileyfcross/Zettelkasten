2026-10-03 16:51

Status: #baby

Tags: [[GPU Virtualization and DPU Offload]]

# NVIDIA vGPU

NVIDIA vGPU is a software platform that presents assigned portions of a physical GPU to guest virtual machines. It combines hypervisor integration, the [[NVIDIA vGPU Manager]], a [[NVIDIA vGPU Guest Driver]], profiles, licensing, scheduling controls, and telemetry.

From inside the VM, the assigned resource behaves like an available accelerator; from the operator side, the device remains centrally managed and shareable. The exact GPU, hypervisor, vGPU release, guest operating system, and driver combination must come from a validated support matrix.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

