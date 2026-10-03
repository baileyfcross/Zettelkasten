2026-10-03 16:51

Status: #baby

Tags: [[CUDA and NVIDIA GPU Architecture]]

# Tensor Core

A Tensor Core is specialized NVIDIA GPU hardware for supported matrix multiply-accumulate operations. Dense layers, convolutions, transformer projections, and attention repeatedly use this mathematical pattern, allowing suitable work to reach higher throughput than a general FP32 path.

Tensor Core use depends on the whole software path: numerical format, operation shape, GPU generation, framework, and optimized libraries must align. [[Mixed-Precision GPU Computation]], [[cuBLAS]], [[cuDNN]], and TensorRT can select or prepare operations that make effective use of these units.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

