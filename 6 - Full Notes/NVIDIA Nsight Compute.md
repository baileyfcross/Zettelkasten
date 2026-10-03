2026-10-03 16:51

Status: #baby

Tags: [[CUDA and NVIDIA GPU Architecture]]

# NVIDIA Nsight Compute

NVIDIA Nsight Compute profiles an individual GPU kernel using measures such as occupancy, instruction execution, memory behavior, and stalls. It helps determine why a selected kernel is limited by compute resources, memory access, dependencies, or launch configuration.

The tool is a deeper step after [[NVIDIA Nsight Systems]] locates a suspicious kernel on the wider timeline. It should not be the first response to every fleet or container problem because device discovery, scheduling, data delivery, and host configuration may fail before kernel execution begins.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

