2026-09-30 23:18

Status: #baby

Tags: [[Terraform Utility Providers and Artifacts]]

# Terraform DNS Automation

Terraform DNS providers manage records through DNS servers or services that may sit outside the primary cloud provider. This lets an address or hostname created in one control plane feed a record in another, preserving the relationship in the [[Terraform Dependency Graph]].

DNS is often a shared organizational boundary, so record ownership and credentials should match the team responsible for the zone. A small application workspace may own only its names, while a central network workspace controls the zone itself. Separating those responsibilities limits the [[Terraform Import Blast Radius|blast radius]] and avoids granting every infrastructure pipeline broad authority over enterprise naming.

# References

[[masteringterraform.pdf]]

