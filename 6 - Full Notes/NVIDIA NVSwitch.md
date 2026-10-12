2026-10-03 16:51

Status: #baby

Tags: [[NVIDIA Data Center GPU Selection]]

# NVIDIA NVSwitch

NVIDIA NVSwitch creates a switched fabric among multiple NVLink-connected GPUs. It extends beyond point-to-point links so a larger local group can exchange data through high-bandwidth paths suitable for tightly coupled data or model parallelism.

The fabric remains a property of the physical system topology, not merely of the GPU model. A scheduler should keep communicating work on devices connected by the appropriate NVSwitch domain; otherwise a job may run across slower paths and lose scaling efficiency.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

