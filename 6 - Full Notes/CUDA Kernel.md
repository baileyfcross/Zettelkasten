2026-10-03 16:51

Status: #baby

Tags: [[CUDA and NVIDIA GPU Architecture]]

# CUDA Kernel

A CUDA kernel is a function launched by the host to execute in parallel on an NVIDIA GPU. A launch creates many [[CUDA Thread|threads]] that apply the same kernel to different elements, rows, tiles, samples, or other portions of a workload.

The complete kernel launch is represented by a [[CUDA Grid]] of thread blocks. Kernel speed therefore depends on both the useful arithmetic and the costs of launch coordination, memory movement, synchronization, and the chosen execution configuration.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

