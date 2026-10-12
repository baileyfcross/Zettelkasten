2026-09-27 18:58

Status: #baby

Tags: [[AWS Availability Scaling and Edge Delivery]]

# Network Load Balancer

A Network Load Balancer distributes TCP, UDP, and TLS connections at the transport layer. It is designed for very high throughput and low latency and can expose static IP addresses, which is useful when clients or firewalls require predictable network endpoints.

Its routing decisions do not inspect HTTP paths in the manner of an [[Application Load Balancer]]. The two services therefore solve different problems: a Network Load Balancer is selected for connection-level performance and protocol support, while application-aware routing belongs at layer seven.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
