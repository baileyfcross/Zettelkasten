2026-09-27 18:58

Status: #baby

Tags: [[Amazon VPC and Hybrid Networking]]

# AWS Transit Gateway

AWS Transit Gateway is a regional hub that connects multiple VPCs and on-premises networks. Attachments and transit route tables replace many individual peering relationships with a hub-and-spoke topology.

Centralization simplifies large network estates and can segment groups of attachments through separate routing domains. It also concentrates routing policy, so propagation, inspection paths, address plans, and ownership must be deliberately governed.

Each attachment associates with one transit-gateway route table and may propagate routes to one or more tables. This permits segmented hub-and-spoke designs, such as isolating production and development while sharing inspection or hybrid connectivity, without assuming every attached network can reach every other attachment.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]

[[awsforsolutionsarchitectsthirdedition.pdf]]
