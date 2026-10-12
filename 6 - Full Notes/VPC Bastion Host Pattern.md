2026-09-27 18:58

Status: #baby

Tags: [[Amazon VPC and Hybrid Networking]]

# VPC Bastion Host Pattern

The VPC bastion host pattern places a tightly controlled administrative host in a public subnet and permits it to reach instances in private subnets. Operators connect to the bastion first, then use private addressing for the internal target.

The bastion becomes a sensitive choke point. Its inbound source range, authentication, patching, logging, and allowed destinations should be minimized. The pattern limits direct exposure but does not justify broad trust from the bastion to every private resource.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
