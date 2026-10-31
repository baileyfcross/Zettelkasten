2026-09-27 18:58

Status: #baby

Tags: [[Amazon VPC and Hybrid Networking]]

# AWS Private Subnet

An AWS private subnet lacks a direct route from its instances to an internet gateway. It is suited to application and database components that should not accept unsolicited internet connections.

Private resources can still initiate outbound access through a NAT gateway, reach AWS services through appropriate endpoints, or communicate with connected private networks. Privacy therefore describes routing exposure, while security groups, network ACLs, identity, and application controls provide additional layers.

The EKS topology places worker capacity across subnets and availability zones while control-plane connectivity enters through AWS-managed interfaces. Terraform must declare the routes and security relationships that let private nodes join the cluster and reach required external resources without accepting direct inbound internet sessions.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
[[javamicroservicesandcontainersinthecloud.epub]]
