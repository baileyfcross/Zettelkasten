2026-10-03 16:51

Status: #baby

Tags: [[NVIDIA AI Inference Stack]]

# Triton Model Control Mode

Triton model control mode determines when the inference server loads repository contents. NONE loads selected models at startup and ignores later changes, EXPLICIT permits model-management APIs to load and unload them, and POLL periodically detects repository changes.

The mode is an operational choice about control and change visibility. It should align with artifact promotion, access policy, rollout automation, and rollback because a repository update has different effects depending on how the server observes it.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

