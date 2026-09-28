2026-09-27 12:11

Status: #baby

Tags: [[AI-Assisted DevOps Practice]]

# AI-Assisted Infrastructure as Code

Infrastructure as Code is a natural target for AI assistance because it is text-based, pattern-heavy, and still deployed through deterministic platform tooling. A model can scaffold resources, explain relationships, draft parameter files, and identify common configuration issues.

Generated infrastructure is not automatically correct. Engineers must verify resource names, API versions, identities, permissions, SKUs, dependencies, and organizational policy, then use preview operations such as an Azure deployment what-if before applying the change. AI shortens the first draft; the IaC compiler, platform preview, security review, and accountable operator establish correctness.

The same boundary applies to Terraform: AI can summarize a [[Terraform Plan]], call attention to deletion or public exposure, and translate a large diff into reviewer questions. The original plan remains the deterministic evidence, and a protected pipeline still controls who can approve and apply it. A generated explanation is an aid to judgment rather than an authorization mechanism.

# References

[[agenticaifordevopsengineers.pdf]]
[[clouddevopsengineersguide.pdf]]
