2026-10-03 16:51

Status: #baby

Tags: [[NVIDIA AI Inference Stack]]

# NVIDIA TensorRT

NVIDIA TensorRT is an inference optimizer and runtime that converts a supported trained model, often through [[ONNX Model Format|ONNX]], into an engine tuned for a target NVIDIA GPU environment. Its objective is lower latency, higher throughput, and reduced memory use.

Optimization can include precision calibration, graph transformation, kernel autotuning, and layer fusion. The resulting [[TensorRT Engine]] is hardware- and configuration-aware, so quality and performance must be benchmarked on the intended deployment rather than assumed from conversion success.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

