2026-10-03 16:51

Status: #baby

Tags: [[CUDA and NVIDIA GPU Architecture]]

# CUDA Programming Model

CUDA is NVIDIA's parallel-computing platform and programming model for executing non-graphics workloads on an NVIDIA [[Graphics Processing Unit]]. It separates a CPU-side host that coordinates the application from a device that executes parallel functions called [[CUDA Kernel|kernels]].

The model expresses scalable work through a [[CUDA Thread|thread]], [[CUDA Thread Block|block]], and [[CUDA Grid|grid]] hierarchy. Software exposes parallelism without permanently assigning each logical work item to a physical core; the runtime and GPU schedule blocks on available execution resources.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

