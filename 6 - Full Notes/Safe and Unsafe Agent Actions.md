2026-09-27 12:11

Status: #baby

Tags: [[DevOps Agent Safety and Autonomy]]

# Safe and Unsafe Agent Actions

Safe agent actions in CI/CD are usually observational or advisory: classify a failure, summarize tests, draft documentation, suggest a pull request, or identify a likely remediation. These activities improve understanding without directly changing production state.

Unsafe actions include auto-merging protected branches, deploying to production, disabling failing tests, and modifying security policy. An agent trying to complete a goal may remove the very control that exposed a problem. Capability design should therefore distinguish useful analysis from authority that can bypass evidence, review, or recovery.

# References

[[agenticaifordevopsengineers.pdf]]
