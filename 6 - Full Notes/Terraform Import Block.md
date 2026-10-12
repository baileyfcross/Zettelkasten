2026-09-30 23:18

Status: #baby

Tags: [[Terraform Delivery and Production Operations]]

# Terraform Import Block

A Terraform `import` block declaratively maps an existing remote object's provider identifier to a resource address in configuration. Unlike the imperative `terraform import` command, the block can travel through a [[Terraform GitOps Pipeline]] and be reviewed with the resource definition it will populate in state.

Imports commonly require two changes: one adds the resource configuration and import block, and a later one removes the block after a successful apply. `for_each` or `count` can describe multiple mappings, but the addresses and external identifiers must match precisely. Import establishes state ownership; it does not guarantee that handwritten configuration matches the object's current settings, so a no-change [[Terraform Plan]] is the reconciliation target.

# References

[[masteringterraform.pdf]]

