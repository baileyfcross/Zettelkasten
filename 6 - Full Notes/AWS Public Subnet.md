2026-09-27 18:58

Status: #baby

Tags: [[Amazon VPC and Hybrid Networking]]

# AWS Public Subnet

An AWS public subnet has a route to an internet gateway. A resource in it can communicate directly with the internet only when it also has a public address and its security controls permit the traffic.

Public does not mean unrestricted. Load balancers, NAT gateways, and carefully managed bastion hosts are typical public-subnet resources, while application and database servers can remain in private subnets. Route and address together create the reachable path.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
