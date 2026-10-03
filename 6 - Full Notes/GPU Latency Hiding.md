2026-10-03 16:51

Status: #baby

Tags: [[CUDA and NVIDIA GPU Architecture]]

# GPU Latency Hiding

GPU latency hiding keeps execution resources useful by switching among ready groups of parallel work while other groups wait on memory or dependencies. On an NVIDIA GPU, a [[Warp Scheduler]] can select another resident warp instead of leaving the entire streaming multiprocessor idle.

Latency hiding does not make slow memory or synchronization free. It requires enough independent [[CUDA Warp|warps]] to be resident and ready, so launch configuration, register use, shared-memory demand, and workload parallelism all affect the result.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

