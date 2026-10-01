2026-09-30 23:18

Status: #baby

Tags: [[Terraform Utility Providers and Artifacts]]

# Terraform Archive File

Terraform's archive provider packages files or directories into formats such as ZIP so the resulting artifact can be referenced by infrastructure resources. This is common in serverless delivery, where a function resource or storage object needs a deterministic deployment bundle.

An archive resource makes the package and its checksum visible to the [[Terraform Plan]], allowing content changes to trigger deployment. Compilation and testing still belong before this step: Terraform is packaging an artifact, not replacing a language build system. Large application releases may also benefit from a separate artifact repository and the [[Terraform Serverless Deployment Boundary]] rather than embedding every delivery action in state.

# References

[[masteringterraform.pdf]]

