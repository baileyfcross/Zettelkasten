2026-09-27 18:58

Status: #baby

Tags: [[AWS Availability Scaling and Edge Delivery]]

# Route 53 Routing Policy

A Route 53 routing policy controls how DNS answers are chosen when a name has multiple possible resources. AWS supports policies for simple responses, weighted traffic splits, latency-based selection, geographic rules, geoproximity, failover, and multivalue answers.

The policy encodes a traffic objective rather than moving application data itself. For health-aware failover, it can combine records with a [[Route 53 Health Check]] so unhealthy endpoints stop appearing in eligible answers.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
