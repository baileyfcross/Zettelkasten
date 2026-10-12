2026-09-27 18:58

Status: #baby

Tags: [[Amazon VPC and Hybrid Networking]]

# AWS NAT Gateway

An AWS NAT gateway lets resources in private subnets initiate IPv4 connections to the internet while preventing unsolicited inbound sessions from being routed directly to them. The private subnet routes outbound traffic to a NAT gateway placed in a public subnet.

A NAT gateway is zonal and incurs hourly and processing charges. Resilient designs place gateways in the zones they serve rather than depending on one cross-zone path. It provides translation, not application filtering or identity authorization.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
