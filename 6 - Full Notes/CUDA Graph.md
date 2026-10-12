2026-10-03 16:51

Status: #baby

Tags: [[CUDA and NVIDIA GPU Architecture]]

# CUDA Graph

A CUDA Graph captures a sequence of GPU operations and their dependencies as a reusable execution graph. After the graph is instantiated, an application can replay the prepared workflow instead of repeating the full host-side setup for every small [[CUDA Kernel]] launch.

The technique is most useful when a stable path contains many short operations whose launch overhead is large relative to their computation, such as some low-latency inference paths. It changes submission efficiency and predictability, not the model or arithmetic being executed.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

