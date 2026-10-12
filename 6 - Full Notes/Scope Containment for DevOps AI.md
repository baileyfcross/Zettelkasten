2026-09-27 12:11

Status: #baby

Tags: [[DevOps AI Governance]]

# Scope Containment for DevOps AI

Scope containment prevents an AI system from acting on repositories, environments, files, or workflow stages outside the task it was given. A request concerning a test branch should not permit changes to production YAML or unrelated infrastructure.

Containment begins in the prompt but must also exist in the surrounding system. Repository selection, tool allowlists, environment boundaries, file filters, credentials, and policy gates should all encode the permitted scope. This makes relevance a technical safeguard rather than a request that the model can accidentally ignore.

# References

[[agenticaifordevopsengineers.pdf]]
