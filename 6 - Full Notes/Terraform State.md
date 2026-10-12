2026-09-27 22:21

Status: #baby

Tags: [[Terraform Core Workflow and State]]

# Terraform State

Terraform state records the mapping between resources named in configuration and the real infrastructure objects Terraform manages. Planning uses this mapping to compare the declared target with what is already known and what currently exists, preventing every execution from rediscovering or recreating the whole environment.

State is operationally sensitive because it exposes infrastructure details and may contain secret values. A local `terraform.tfstate` file should not be committed to Git. Collaborative and automated use should place it in a protected [[Terraform Remote Backend]] where it persists beyond one workstation or temporary pipeline runner.

State is also a deliberate scope boundary: unmanaged objects are outside Terraform's responsibility even when they share the same cloud environment. Large or unrelated systems should be separated into workspaces whose permissions, deployment cadence, and failure domains align with the teams that operate them.

# References

[[clouddevopsengineersguide.pdf]]
[[masteringterraform.pdf]]
