2026-10-03 16:51

Status: #baby

Tags: [[NVIDIA GPU Sharing and Fleet Management]]

# MIG Profile

A MIG profile is a predefined compute-and-memory shape for an instance on a supported NVIDIA GPU. A name such as `1g.5gb` identifies a compute-slice count and an approximate memory allocation for the relevant device configuration; it is not an arbitrary percentage chosen independently by the administrator.

Profile names and capacities vary by GPU generation and memory configuration, so a platform must discover the shapes supported by the installed hardware. The selected profile must fit the model and runtime state while leaving a device geometry that can accommodate the expected mixture of other workloads.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

