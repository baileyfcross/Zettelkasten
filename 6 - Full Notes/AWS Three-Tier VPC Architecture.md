2026-09-27 18:58

Status: #baby

Tags: [[Amazon VPC and Hybrid Networking]]

# AWS Three-Tier VPC Architecture

An AWS three-tier VPC architecture separates an internet-facing load-balancing layer, an application compute layer, and a persistent database layer. Each tier occupies subnets and security groups that allow only the flows required from the adjacent layer.

Replicating tiers across availability zones combines isolation with high availability. Users reach the load balancer, the load balancer reaches healthy application targets, and only the application tier reaches the database. This reduces the blast radius of a compromised public endpoint.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
