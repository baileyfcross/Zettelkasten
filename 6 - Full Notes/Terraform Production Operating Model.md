2026-09-30 23:18

Status: #baby

Tags: [[Terraform Delivery and Production Operations]]

# Terraform Production Operating Model

A Terraform production operating model aligns repositories, states, permissions, and release processes with the team that owns the environment. A standalone application team may keep application and infrastructure together, a shared-infrastructure team may operate networks or clusters consumed by many teams, and a shared-service team must coordinate both application interfaces and infrastructure dependencies.

The correct boundary depends on ownership and downstream coupling rather than a universal repository layout. Long-lived state needs access control, encryption, versioning, backups, and regional recovery, while [[Terraform Layered Workspace Architecture|workspace layers]] limit disruption between teams. Operability is a design requirement: a system that cannot be changed or recovered safely during an outage is not production-ready merely because Terraform created it.

# References

[[masteringterraform.pdf]]

