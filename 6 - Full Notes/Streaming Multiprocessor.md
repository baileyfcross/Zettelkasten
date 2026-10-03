2026-10-03 16:51

Status: #baby

Tags: [[CUDA and NVIDIA GPU Architecture]]

# Streaming Multiprocessor

A streaming multiprocessor, or SM, is a primary compute engine inside an NVIDIA GPU. It combines execution units, registers, shared memory, cache, scheduling logic, and other resources needed to run blocks of CUDA threads.

Blocks from a [[CUDA Grid]] are assigned to SMs, and their threads execute in [[CUDA Warp|warps]]. Multiple resident warps allow an SM to keep making progress when some work is delayed, but memory bandwidth, dependencies, and resource limits still determine how much of the hardware remains productive.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

