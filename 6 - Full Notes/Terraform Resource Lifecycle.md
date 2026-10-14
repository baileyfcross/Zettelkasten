2026-09-30 23:18

Status: #baby

Tags: [[Terraform HCL and Module Design]]

# Terraform Resource Lifecycle

The `lifecycle` block modifies how Terraform responds when a [[Terraform Resource]] differs from configuration. `create_before_destroy` can reduce replacement downtime, `prevent_destroy` can reject accidental deletion, `ignore_changes` can delegate selected attributes to another controller, and `replace_triggered_by` can tie replacement to another object's change.

These controls change risk rather than eliminate it. Creating first may require duplicate names or capacity, ignored attributes can conceal drift, and prevention can block intentional retirement. Each rule should express a durable ownership or availability requirement and remain visible in the [[Terraform Plan]] rather than serving as a blanket way to silence inconvenient changes.

# References

[[masteringterraform.pdf]]

