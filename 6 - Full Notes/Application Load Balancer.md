2026-09-27 18:58

Status: #baby

Tags: [[AWS Availability Scaling and Edge Delivery]]

# Application Load Balancer

An Application Load Balancer operates at the application layer and routes HTTP or HTTPS requests to target groups. Listener rules can select a destination using properties such as the request host or path, allowing several services to share one entry point.

The load balancer performs health checks and works naturally with an [[EC2 Auto Scaling Group]], containers, and IP-address targets. It is suited to web applications and service-oriented architectures where content-aware routing matters more than raw connection throughput.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
