2026-10-03 16:51

Status: #baby

Tags: [[NVIDIA GPU Platform Operations]]

# GPU Diagnostic Ladder

A GPU diagnostic ladder starts with broad configuration and state evidence, then narrows only when earlier checks justify more detail. Container and Kubernetes events verify request and scheduling, NVIDIA-SMI checks device and process state, DCGM supplies fleet health, Nsight Systems locates application-wide delay, and Nsight Compute explains a kernel.

The sequence prevents every symptom from being treated as a CUDA kernel problem. Each rung asks a different question and hands a more specific hypothesis to the next tool, preserving time and reducing unsupported remediation.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

