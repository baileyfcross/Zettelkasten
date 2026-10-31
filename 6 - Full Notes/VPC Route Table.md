2026-09-27 18:58

Status: #baby

Tags: [[Amazon VPC and Hybrid Networking]]

# VPC Route Table

A VPC route table maps destination CIDR ranges to targets such as the local VPC, an internet or NAT gateway, a peering connection, a virtual private gateway, or a Transit Gateway. Each subnet is associated with a route table.

The most specific matching route is selected. Route tables create paths but do not override security groups or network ACLs, so successful connectivity requires routing and traffic policy to agree in both directions.

The book's Terraform topology associates routes with the subnets used by EC2 and EKS resources and targets internet or NAT gateways according to the desired exposure. This makes routing an explicit dependency of workload placement rather than a default that every subnet can safely share.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
[[javamicroservicesandcontainersinthecloud.epub]]
