2026-10-03 16:51

Status: #baby

Tags: [[GPU Virtualization and DPU Offload]]

# MIG and vGPU Layering

MIG and vGPU layering uses a hardware-isolated MIG instance as the resource beneath a hypervisor-delivered virtual GPU on supported platforms. MIG defines the compute-and-memory boundary; vGPU and the hypervisor present accelerator access to a VM.

The combination shows that the technologies operate at different layers rather than being universal alternatives. Requirements should first identify the hardware isolation need and the VM delivery boundary, then verify that the GPU, MIG geometry, vGPU release, hypervisor, guest, and licensing combination is supported.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

