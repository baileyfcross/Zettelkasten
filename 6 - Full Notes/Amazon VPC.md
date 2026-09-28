2026-09-27 18:58

Status: #baby

Tags: [[Amazon VPC and Hybrid Networking]]

# Amazon VPC

Amazon Virtual Private Cloud defines a logically isolated regional network for AWS resources. The customer selects address ranges, creates zonal subnets, attaches gateways, and uses route and security controls to determine which components can communicate.

A VPC spans the availability zones of its region, but a subnet does not. This lets an application place replicas in separate zones while sharing a regional network boundary. Isolation is configurable, not automatic proof that every resource is private.

The solutions-architecture source treats the VPC as a routing system as well as an address boundary. Main route tables provide defaults, subnet associations can select different routes, and gateways or inspection endpoints become effective only when the relevant route tables direct traffic through them.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]

[[awsforsolutionsarchitectsthirdedition.pdf]]
