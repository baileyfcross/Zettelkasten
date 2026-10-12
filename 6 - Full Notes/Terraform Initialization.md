2026-09-30 23:18

Status: #baby

Tags: [[Terraform Core Workflow and State]]

# Terraform Initialization

`terraform init` prepares a working directory before planning or applying. It installs the required [[Terraform Provider|providers]], retrieves referenced [[Terraform Module|modules]], and configures the [[Terraform Remote Backend]] that will supply and persist state.

Initialization is context-sensitive rather than a one-time global setup. A pipeline can pass backend settings such as a bucket, region, key, or prefix without hardcoding environment-specific storage in reusable configuration. Pinning tool, provider, and module versions makes the initialized dependency set repeatable across developer machines and automation runners.

# References

[[masteringterraform.pdf]]

