2026-09-27 18:58

Status: #baby

Tags: [[Amazon VPC and Hybrid Networking]]

# VPC Security Group

A VPC security group is a stateful allow-list firewall attached to supported network interfaces or resources. Inbound and outbound rules specify protocol, port, and source or destination, which may include another security group.

Because the control is stateful, return traffic for an allowed connection is permitted without a matching reverse rule. Security groups contain no explicit deny rule, so designs begin closed and add only required flows between application tiers.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
