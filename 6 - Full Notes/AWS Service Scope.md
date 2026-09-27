2026-09-27 18:58

Status: #baby

Tags: [[AWS Global Infrastructure and Support]]

# AWS Service Scope

AWS service scope describes whether a service or resource is global, regional, or zonal. Global services use an account-wide control plane, regional services are configured independently in each region, and zonal resources reside in one availability zone.

Scope determines how failures, names, policies, and replication must be handled. An EC2 instance is zonal, a VPC is regional, and some identity or DNS capabilities operate globally. Architecture should follow the documented scope instead of assuming every AWS object shares the same boundary.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
