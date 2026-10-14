2026-09-27 22:21

Status: #baby

Tags: [[Terraform Core Workflow and State]]

# Terraform Remote Backend

A Terraform remote backend stores [[Terraform State]] in a shared, persistent service instead of only on the machine running Terraform. This is necessary for team workflows and CI jobs because a temporary runner disappears after execution and would otherwise lose the mapping to infrastructure it created.

An S3 backend can centralize the state under an environment-specific key and allow authorized runners to read and update it. Backend access needs narrowly scoped permissions, protected storage, and [[Terraform State Locking]]. Staging and production should use separate state keys so a change intended for one environment cannot silently modify the other.

Equivalent backends use Azure Storage or Google Cloud Storage, but their naming, authentication, and isolation boundaries differ. Versioning, cross-region replication, and separate administrative scopes preserve the ability to control infrastructure even when a runner, region, or ordinary application account is compromised or unavailable.

# References

[[clouddevopsengineersguide.pdf]]
[[masteringterraform.pdf]]
