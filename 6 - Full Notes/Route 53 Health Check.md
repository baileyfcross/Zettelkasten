2026-09-27 18:58

Status: #baby

Tags: [[AWS Availability Scaling and Edge Delivery]]

# Route 53 Health Check

A Route 53 health check evaluates the reachability or health of an endpoint, a CloudWatch alarm, or a calculated combination of other checks. Its result can be associated with DNS records used by a failover-aware [[Route 53 Routing Policy]].

The check should test a condition that represents real service usefulness, not merely whether a machine responds. If an endpoint becomes unhealthy, Route 53 can omit its record and direct new DNS resolutions toward a healthy alternative, subject to DNS caching and record time-to-live.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
