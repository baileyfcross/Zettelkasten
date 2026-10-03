2026-10-03 16:51

Status: #baby

Tags: [[NVIDIA Data Center GPU Selection]]

# GPU Memory Bandwidth

GPU memory bandwidth measures how quickly data can move between device memory and the execution resources that consume it. A model can fit within [[GPU Memory Capacity]] yet perform below its potential when weights, activations, or intermediate values cannot reach the compute units fast enough.

Bandwidth should be evaluated with cache behavior, access patterns, numerical format, and the wider data path. A high specification does not guarantee useful throughput if preprocessing, storage, interconnects, or irregular memory access leave the GPU waiting.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

