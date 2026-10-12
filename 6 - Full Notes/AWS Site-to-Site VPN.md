2026-09-27 18:58

Status: #baby

Tags: [[Amazon VPC and Hybrid Networking]]

# AWS Site-to-Site VPN

AWS Site-to-Site VPN connects an on-premises network to a VPC or Transit Gateway through encrypted IPsec tunnels over the public internet. Redundant tunnels provide alternate paths when one endpoint or path fails.

VPN deployment is faster and less dedicated than a private circuit, but throughput and latency depend on internet conditions. Routing, customer gateway configuration, encryption parameters, and failover testing determine whether the nominal redundancy is usable.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
