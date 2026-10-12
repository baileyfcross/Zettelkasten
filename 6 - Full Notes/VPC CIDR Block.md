2026-09-27 18:58

Status: #baby

Tags: [[Amazon VPC and Hybrid Networking]]

# VPC CIDR Block

A VPC CIDR block defines the IP address range from which its subnets receive addresses. CIDR notation states how many leading bits identify the network, so a smaller prefix length represents a larger address space.

The range should avoid overlap with networks that may later connect through peering, Transit Gateway, VPN, or Direct Connect. Address planning also reserves room for several availability zones and workload tiers; changing an undersized or conflicting design later can be disruptive.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
