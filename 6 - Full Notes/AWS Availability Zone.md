2026-09-27 18:58

Status: #baby

Tags: [[AWS Global Infrastructure and Support]]

# AWS Availability Zone

An AWS Availability Zone is an isolated collection of one or more data centers inside an [[AWS Region]]. Zones in a region are connected by low-latency links while being separated so that a localized power, cooling, or facility failure is less likely to affect all of them.

Deploying replicas across zones supports high availability, but the application must distribute traffic and maintain recoverable state. A subnet belongs to one zone even though its VPC spans the region, making zone placement part of network and workload design.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
