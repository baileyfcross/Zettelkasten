2026-09-30 23:18

Status: #baby

Tags: [[Terraform Delivery and Production Operations]]

# Terraform State Refactoring

Terraform state refactoring changes a resource's configuration address without replacing the remote object. A declarative `moved` block records the old and new addresses in HCL, while `terraform state mv` performs the equivalent mapping imperatively.

This is necessary when repeated resources become a [[Terraform Module]], a module is renamed, or an object moves between scopes. Without the mapping, the [[Terraform Plan]] interprets the old address as removed and the new one as absent, often proposing destroy and create. Declarative moves travel through review and can provide an upgrade path to all module consumers; removal and re-import are more disruptive fallbacks when resources cross state boundaries.

# References

[[masteringterraform.pdf]]

