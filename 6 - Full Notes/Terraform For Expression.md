2026-09-30 23:18

Status: #baby

Tags: [[Terraform HCL and Module Design]]

# Terraform For Expression

A Terraform `for` expression transforms one collection into another without creating resource instances by itself. It can map every object to one attribute, construct a keyed object, filter elements with a condition, or normalize caller input before it reaches a resource or module.

This separates data shaping from repetition. A [[Terraform Local Value]] can use a `for` expression to produce a stable map, after which [[Terraform Count and For Each|for_each]] creates resources with meaningful keys. Keeping transformations explicit makes interface assumptions easier to review and avoids duplicating the same indexing logic throughout a configuration.

# References

[[masteringterraform.pdf]]

