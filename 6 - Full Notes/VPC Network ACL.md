2026-09-27 18:58

Status: #baby

Tags: [[Amazon VPC and Hybrid Networking]]

# VPC Network ACL

A VPC network access control list is a stateless set of numbered allow and deny rules applied at a subnet boundary. Inbound and outbound traffic are evaluated separately in rule order until a match is found.

Because the control is stateless, return traffic needs its own applicable rule, including ephemeral ports where required. NACLs provide coarse subnet guardrails, while [[VPC Security Group|security groups]] provide stateful resource-level permissions.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
