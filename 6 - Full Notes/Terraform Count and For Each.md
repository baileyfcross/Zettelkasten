2026-09-30 23:18

Status: #baby

Tags: [[Terraform HCL and Module Design]]

# Terraform Count and For Each

`count` and `for_each` create multiple instances from one Terraform block. `count` assigns numeric indexes and works well for interchangeable instances, while `for_each` assigns stable keys from a set or map and is better when each instance has a durable identity.

Removing an item from the middle of a counted list can shift later indexes and make Terraform propose avoidable replacements. A keyed map preserves the addresses of unaffected instances and makes the [[Terraform Plan]] easier to interpret. The same addressing rules apply to imports, module instances, and references, so the choice becomes part of the configuration's long-term state model.

# References

[[masteringterraform.pdf]]

