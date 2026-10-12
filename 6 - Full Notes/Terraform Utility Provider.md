2026-09-30 23:18

Status: #baby

Tags: [[Terraform Utility Providers and Artifacts]]

# Terraform Utility Provider

A Terraform utility provider supplies supporting capabilities that are not tied to one cloud's infrastructure API. Providers for random values, time, local files, archives, TLS, external programs, and DNS can produce inputs or artifacts needed by resources managed through AWS, Azure, Google Cloud, or another platform.

Utility providers are most valuable when their resources make dependencies visible to the [[Terraform Dependency Graph]]. They also enlarge a module's dependency surface, so reusable modules should include them only when the behavior belongs inside the module's contract. A convenience that merely wraps an imperative deployment step may be clearer in the delivery pipeline.

# References

[[masteringterraform.pdf]]

