2026-09-30 23:18

Status: #baby

Tags: [[Terraform Delivery and Production Operations]]

# Terraform Bulk Import Strategy

A bulk import strategy discovers existing cloud resources, generates Terraform configuration, and constructs state at a scale impractical for individual import commands. Tools can narrow discovery by provider, resource type, region, project, resource group, or tags so one batch corresponds to a deliberate workspace boundary.

Generated configuration is a starting point rather than production-quality design. It commonly contains hardcoded values, redundant explicit dependencies, missing write-only secrets, and provider-specific details that fail validation or propose changes. Teams should run [[Terraform Plan]] immediately, allocate time for refactoring, and constrain the [[Terraform Import Blast Radius]]; a slower manual import or [[Terraform Blue-Green Migration]] may yield a cleaner system.

# References

[[masteringterraform.pdf]]

