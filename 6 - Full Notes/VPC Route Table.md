2026-09-27 18:58

Status: #baby

Tags: [[Amazon VPC and Hybrid Networking]]

# VPC Route Table

A VPC route table maps destination CIDR ranges to targets such as the local VPC, an internet or NAT gateway, a peering connection, a virtual private gateway, or a Transit Gateway. Each subnet is associated with a route table.

The most specific matching route is selected. Route tables create paths but do not override security groups or network ACLs, so successful connectivity requires routing and traffic policy to agree in both directions.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
