2026-10-03 16:51

Status: #baby

Tags: [[GPU Virtualization and DPU Offload]]

# vGPU Profile

A vGPU profile defines the framebuffer allocation and class of capability presented to a virtual machine. Profiles turn shared physical capacity into named service shapes that a platform can assign, quota, monitor, and account for.

A profile operates through the hypervisor and NVIDIA vGPU software, unlike a [[MIG Profile]], which describes a hardware partition. On supported systems the two can be layered, but profile choice still requires sufficient memory, expected compute share, workload type, license, and platform compatibility.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

