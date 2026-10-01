2026-09-30 23:18

Status: #baby

Tags: [[Terraform HCL and Module Design]]

# Terraform Data Source

A Terraform data source reads an existing object or external fact without declaring that Terraform should create it. Its attributes can feed resources, outputs, or provider configuration, making it a bridge from the current environment into declarative configuration.

Data sources are particularly useful between layers: a downstream workspace can look up a cluster, network, or image provisioned upstream and use the result as an input. That convenience also creates a runtime dependency that should be explicit in the [[Terraform Layered Workspace Architecture]]; a lookup by an unstable name can make a supposedly reproducible plan depend on whatever happens to exist.

# References

[[masteringterraform.pdf]]

