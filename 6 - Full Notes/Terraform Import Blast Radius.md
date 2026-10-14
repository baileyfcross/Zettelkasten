2026-09-30 23:18

Status: #baby

Tags: [[Terraform Delivery and Production Operations]]

# Terraform Import Blast Radius

Terraform import blast radius is the set of existing resources, teams, permissions, and failure consequences placed under one root module and state during adoption. Import is the moment when previously informal infrastructure receives an explicit management boundary, so grouping everything a discovery tool can see creates a long-term operational liability.

Resources should be grouped by function, ownership, deployment cadence, and dependency. Tags, projects, resource groups, accounts, and regions can narrow a [[Terraform Bulk Import Strategy]], while independent states prevent one plan from touching unrelated systems. A focused boundary also makes generated code easier to understand and reduces the impact of later [[Terraform Upgrade Strategy|upgrades]] or state refactoring.

# References

[[masteringterraform.pdf]]

