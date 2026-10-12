2026-10-03 16:51

Status: #baby

Tags: [[NVIDIA GPU Platform Operations]]

# NGC Container

An NGC container packages a tested user-space environment for a GPU workload, including a base operating-system layer, CUDA runtime, accelerated libraries, framework or tool, and supporting application dependencies. Examples include environments for PyTorch, TensorFlow, Triton, TensorRT, RAPIDS, and DeepStream.

The container does not carry the physical GPU or replace the host driver. Reproducibility depends on pinning an image identity and validating that its user-space CUDA stack is compatible with the driver and hardware supplied by the host.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

