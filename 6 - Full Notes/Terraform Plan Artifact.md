2026-09-30 23:18

Status: #baby

Tags: [[Terraform Delivery and Production Operations]]

# Terraform Plan Artifact

A Terraform plan artifact is the saved binary result of `terraform plan -out=...`. It captures the exact set of proposed actions so a later [[Terraform Apply]] can execute what reviewers examined instead of calculating a new plan after approval.

The artifact belongs to one configuration, state snapshot, provider set, and execution context. It should be short-lived and protected because it can contain sensitive values even when the human-readable output redacts them. A pipeline can render or summarize the plan for review while passing the original artifact through the approval boundary, invalidating it when source or state changes.

# References

[[masteringterraform.pdf]]

