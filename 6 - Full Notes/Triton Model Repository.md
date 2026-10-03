2026-10-03 16:51

Status: #baby

Tags: [[NVIDIA AI Inference Stack]]

# Triton Model Repository

A Triton model repository organizes each served model by name, numbered versions, and configuration that describes inputs, outputs, batching, and runtime behavior. It turns model delivery into a predictable deployment artifact instead of an unstructured group of files.

Repository contents and [[Triton Model Control Mode|model control mode]] jointly determine what becomes active. Version identity, volume mounts, permissions, backend compatibility, and validation should be checked before a rollout because a running Triton process can still fail to load a model.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

