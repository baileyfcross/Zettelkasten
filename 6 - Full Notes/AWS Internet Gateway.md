2026-09-27 18:58

Status: #baby

Tags: [[Amazon VPC and Hybrid Networking]]

# AWS Internet Gateway

An AWS internet gateway is a horizontally scaled VPC component that connects routed public traffic between the VPC and the internet. A route table sends eligible destination traffic to the gateway, and resources need suitable public addressing for return translation.

Attaching a gateway does not expose every resource. Subnet routes and security controls still decide which traffic can pass. This separation lets one VPC contain both public and private subnets.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
