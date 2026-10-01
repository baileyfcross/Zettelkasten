2026-09-30 23:18

Status: #baby

Tags: [[Terraform HCL and Module Design]]

# Terraform Meta-Argument

A Terraform meta-argument changes how Terraform manages a block rather than configuring the remote object represented by that block. Examples include `count`, `for_each`, `depends_on`, `provider`, and `lifecycle`; they affect instance creation, dependency ordering, provider selection, or change behavior.

Meta-arguments belong to Terraform's execution model, so their use can alter resource addresses and the [[Terraform Dependency Graph]]. Choosing [[Terraform Count and For Each|for_each instead of count]], for example, changes how instances retain identity. Explicit dependencies and lifecycle exceptions should remain narrow because they override the behavior Terraform would otherwise infer from values and provider schemas.

# References

[[masteringterraform.pdf]]

