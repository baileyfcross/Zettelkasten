2026-10-03 16:51

Status: #baby

Tags: [[CUDA and NVIDIA GPU Architecture]]

# CUDA Thread

A CUDA thread is the smallest logical execution unit in the [[CUDA Programming Model]]. Each thread follows the kernel instructions for its assigned portion of the data and has an identity that lets it select that portion.

Threads are organized into a [[CUDA Thread Block]] and later executed by hardware in [[CUDA Warp|warps]]. Exposing many independent threads gives the scheduler enough ready work to occupy the GPU while some groups wait on data or dependencies.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

