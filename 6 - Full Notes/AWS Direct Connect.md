2026-09-27 18:58

Status: #baby

Tags: [[Amazon VPC and Hybrid Networking]]

# AWS Direct Connect

AWS Direct Connect provides dedicated private network connectivity between a customer location and AWS. It can offer more predictable bandwidth and avoid routing workload traffic over the public internet.

A direct circuit is not automatically encrypted and should not be treated as its own disaster-recovery path. Organizations may combine it with VPN encryption or backup connectivity. Provisioning lead time and physical provider dependencies make it a planned infrastructure service rather than an instant attachment.

Virtual interfaces determine what the connection reaches. A private VIF reaches private VPC resources through a virtual private gateway or Direct Connect gateway, a public VIF reaches public AWS endpoints, and a transit VIF reaches VPCs through Transit Gateway. This logical separation lets one physical connection support distinct routing scopes.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]

[[awsforsolutionsarchitectsthirdedition.pdf]]
