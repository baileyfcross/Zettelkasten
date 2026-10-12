2026-09-27 18:58

Status: #baby

Tags: [[AWS Availability Scaling and Edge Delivery]]

# Amazon Route 53 Hosted Zone

An Amazon Route 53 hosted zone is a container for DNS records that describe how traffic for a domain or subdomain should be resolved. A public hosted zone answers requests on the internet, while a private hosted zone provides names within associated [[Amazon VPC|VPCs]].

Records can point clients toward load balancers, CloudFront distributions, servers, or other endpoints. The hosted zone establishes the administrative DNS boundary; a [[Route 53 Routing Policy]] determines how Route 53 selects among multiple candidate records.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
