2026-10-03 16:51

Status: #baby

Tags: [[CUDA and NVIDIA GPU Architecture]]

# cuBLAS

cuBLAS is NVIDIA's GPU-accelerated implementation of the Basic Linear Algebra Subprograms interface. It supplies tuned vector and matrix routines, including matrix multiplication used throughout dense neural layers, transformer projections, and attention.

The library separates mathematical intent from device-specific optimization. Frameworks can invoke reliable routines rather than retuning the same operation for every GPU generation, and supported implementations can use [[Tensor Core|Tensor Cores]] when shapes, formats, and hardware permit.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

