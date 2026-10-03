2026-10-03 16:51

Status: #baby

Tags: [[NVIDIA AI Inference Stack]]

# Model Portability and Hardware Optimization

Model portability and hardware optimization are separate deployment concerns. [[ONNX Model Format|ONNX]] decouples a model from one training framework, while [[NVIDIA TensorRT|TensorRT]] specializes a supported graph for an NVIDIA GPU and [[NVIDIA Triton Inference Server|Triton]] operates the result as a service.

The distinction prevents one tool from being treated as the whole inference stack. A portable model may be slow without target optimization, and an optimized engine still needs versioning, health, scaling, and observability.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

