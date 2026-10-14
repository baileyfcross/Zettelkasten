2026-09-30 23:18

Status: #baby

Tags: [[Terraform Cloud Deployment Patterns]]

# Terraform Serverless Deployment Boundary

Serverless architecture removes fixed server or cluster capacity but changes the boundary between infrastructure and application delivery. Terraform provisions storage, functions, identities, databases, gateways, and supporting configuration, while a build produces static web files or a function archive suited to the provider's runtime.

The deployment artifact may be referenced directly by Terraform, as with an [[Terraform Archive File|archive]] uploaded for a function, or deployed by a later cloud-specific command. Unlike a [[Terraform VM Deployment Pipeline]], moving to serverless often requires application refactoring and creates stronger provider coupling. Separating framework resources from frequent code releases can keep infrastructure plans small while preserving independent rollback of application artifacts.

# References

[[masteringterraform.pdf]]

