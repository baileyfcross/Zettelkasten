2026-09-30 23:18

Status: #baby

Tags: [[Terraform Delivery and Production Operations]]

# Terraform Blue-Green Migration

A Terraform blue-green migration replaces manually provisioned or poorly structured infrastructure with a newly built environment that is managed by Terraform from its first resource. Workloads move gradually from the legacy blue environment to a tested green environment, after which traffic is cut over and the old environment is retired.

This can be safer and cleaner than importing a large landscape whose generated code requires extensive repair. The method costs temporary duplicate capacity and demands careful data synchronization, identity, DNS, and rollback planning. It applies the general [[Blue-Green Deployment]] technique at environment scale, exchanging import complexity for an explicit migration and cutover process.

# References

[[masteringterraform.pdf]]

