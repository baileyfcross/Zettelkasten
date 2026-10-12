2026-09-27 18:58

Status: #baby

Tags: [[Amazon VPC and Hybrid Networking]]

# AWS Private Subnet

An AWS private subnet lacks a direct route from its instances to an internet gateway. It is suited to application and database components that should not accept unsolicited internet connections.

Private resources can still initiate outbound access through a NAT gateway, reach AWS services through appropriate endpoints, or communicate with connected private networks. Privacy therefore describes routing exposure, while security groups, network ACLs, identity, and application controls provide additional layers.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
