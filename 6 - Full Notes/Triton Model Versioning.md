2026-10-03 16:51

Status: #baby

Tags: [[NVIDIA AI Inference Stack]]

# Triton Model Versioning

Triton model versioning keeps numbered artifacts for one model name inside the [[Triton Model Repository]]. Version policy determines which of those artifacts are eligible to load, allowing an operator to preserve older models, introduce a candidate, or control which version receives requests.

Versioned files do not by themselves provide approval or rollback discipline. The release process must associate each version with evaluation evidence, configuration, dependency compatibility, and a traffic or recovery plan.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

