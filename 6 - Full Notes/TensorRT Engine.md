2026-10-03 16:51

Status: #baby

Tags: [[NVIDIA AI Inference Stack]]

# TensorRT Engine

A TensorRT engine is the optimized executable representation produced for a supported model and target NVIDIA environment. It contains selected kernels, precision decisions, fused operations, memory planning, and other choices made during TensorRT build optimization.

The engine is less portable than the source framework or ONNX graph because its choices depend on the target hardware and software context. It should be versioned with its build configuration, validated model quality, compatibility information, and performance evidence.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

