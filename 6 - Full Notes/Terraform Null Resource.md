2026-09-30 23:18

Status: #baby

Tags: [[Terraform Utility Providers and Artifacts]]

# Terraform Null Resource

A Terraform null resource gives procedural provisioners a place in the dependency graph even though it creates no external infrastructure object. Trigger values determine when Terraform considers the resource changed and reruns the associated local or remote command.

This is an escape hatch for behavior unsupported by a provider, not a general deployment architecture. Terraform cannot model the command's internal effects or reverse them safely, and the runner must supply every required executable, network path, and credential. A dedicated pipeline stage or a real provider is preferable when the action has an independent lifecycle, while [[Terraform External Data Source]] is a narrower choice for read-only integration.

# References

[[masteringterraform.pdf]]

