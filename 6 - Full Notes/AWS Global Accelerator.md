2026-09-27 18:58

Status: #baby

Tags: [[AWS Availability Scaling and Edge Delivery]]

# AWS Global Accelerator

AWS Global Accelerator provides static anycast IP addresses that accept user traffic at the nearest AWS edge and carry it across the AWS global network to healthy regional endpoints. Endpoint health and configured traffic controls allow it to redirect new connections when a regional resource becomes unavailable.

The service is useful for latency-sensitive TCP or UDP applications and multi-region failover. Unlike an [[Amazon CloudFront Distribution]], it does not primarily cache application content; it optimizes and stabilizes the network path to the application.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
