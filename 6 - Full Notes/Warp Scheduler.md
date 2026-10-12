2026-10-03 16:51

Status: #baby

Tags: [[CUDA and NVIDIA GPU Architecture]]

# Warp Scheduler

A warp scheduler selects a ready [[CUDA Warp]] on a [[Streaming Multiprocessor]] and issues its instructions to the available execution units. It does not remove dependencies; it chooses among resident work whose next instruction can proceed.

Maintaining several ready warps supports [[GPU Latency Hiding]]. If one group waits for memory, the scheduler can issue another group, so long as the kernel exposes enough parallelism and register or shared-memory use has not limited residency too severely.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

