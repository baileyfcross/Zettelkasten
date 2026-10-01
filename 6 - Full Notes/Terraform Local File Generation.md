2026-09-30 23:18

Status: #baby

Tags: [[Terraform Utility Providers and Artifacts]]

# Terraform Local File Generation

Terraform's local and template capabilities can render configuration from resource attributes and write it as a file. A managed local-file resource participates in the [[Terraform Dependency Graph]], so a file that needs an endpoint or identifier is produced only after Terraform can resolve that value.

Generated files are appropriate for handoff artifacts such as inventory or application configuration, but their lifetime is tied to the runner's filesystem unless a later stage publishes them. Secrets should not be written casually to an ephemeral workspace or committed to Git. Encoding structured values directly and making the consumer explicit keeps file generation from becoming hidden configuration management.

# References

[[masteringterraform.pdf]]

