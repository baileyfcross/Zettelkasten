2026-09-27 18:58

Status: #baby

Tags: [[Amazon VPC and Hybrid Networking]]

# VPC Security Group

A VPC security group is a stateful allow-list firewall attached to supported network interfaces or resources. Inbound and outbound rules specify protocol, port, and source or destination, which may include another security group.

Because the control is stateful, return traffic for an allowed connection is permitted without a matching reverse rule. Security groups contain no explicit deny rule, so designs begin closed and add only required flows between application tiers.

The source applies separate security boundaries to the EC2 microservice host, Kubernetes management host, and EKS worker nodes. Terraform rules expose only the administration, cluster, or application flows the topology needs, while routing alone cannot authorize those connections.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
[[javamicroservicesandcontainersinthecloud.epub]]
