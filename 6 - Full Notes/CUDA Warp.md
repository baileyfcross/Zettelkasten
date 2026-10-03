2026-10-03 16:51

Status: #baby

Tags: [[CUDA and NVIDIA GPU Architecture]]

# CUDA Warp

A CUDA warp is a hardware execution group of threads selected together by a [[Warp Scheduler]] on a [[Streaming Multiprocessor]]. The book depicts 32 threads per warp, with several warps potentially resident and ready on the same SM.

Warps provide the scheduler with interchangeable groups of work. When one warp waits for memory or another dependency, a different ready warp can issue instructions, provided the kernel exposes enough parallel work and the SM has the resources to keep multiple warps resident.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

