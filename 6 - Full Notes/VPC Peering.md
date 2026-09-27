2026-09-27 18:58

Status: #baby

Tags: [[Amazon VPC and Hybrid Networking]]

# VPC Peering

VPC peering privately connects two VPCs so routed resources can communicate across AWS infrastructure. The VPCs may be in different accounts or regions, provided their address ranges do not overlap and both sides add routes and permissions.

Peering is one-to-one and not transitive: if A peers with B and B peers with C, A does not automatically reach C. A dense mesh becomes operationally difficult, which motivates [[AWS Transit Gateway]] for many-network connectivity.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
