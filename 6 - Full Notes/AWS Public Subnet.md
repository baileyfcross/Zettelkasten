2026-09-27 18:58

Status: #baby

Tags: [[Amazon VPC and Hybrid Networking]]

# AWS Public Subnet

An AWS public subnet has a route to an internet gateway. A resource in it can communicate directly with the internet only when it also has a public address and its security controls permit the traffic.

Public does not mean unrestricted. Load balancers, NAT gateways, and carefully managed bastion hosts are typical public-subnet resources, while application and database servers can remain in private subnets. Route and address together create the reachable path.

In the source's minimal AWS topology, the public-facing path combines a subnet route, internet gateway, instance addressing, and a security group that permits the required administration or application port. Omitting any one of those elements breaks reachability even though the subnet is labeled public.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
[[javamicroservicesandcontainersinthecloud.epub]]
