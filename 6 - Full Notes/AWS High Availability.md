2026-09-27 18:58

Status: #baby

Tags: [[AWS Availability Scaling and Edge Delivery]]

# AWS High Availability

High availability is the ability of a workload to remain accessible despite ordinary component failures. On AWS, it is commonly pursued by running redundant resources across multiple [[AWS Availability Zone|Availability Zones]], distributing traffic with [[Elastic Load Balancing]], and replacing unhealthy capacity through an [[EC2 Auto Scaling Group]].

Availability is a design property rather than a feature that can be switched on. Dependencies, data stores, health checks, recovery procedures, and the geographic scope of failure all determine whether redundancy actually keeps the service usable.

An Application Load Balancer and an Auto Scaling group can distribute requests and replace unhealthy instances across zones, but they do not make a stateful dependency highly available by themselves. The architecture must remove single points of failure through every request path and test behavior when a zone, instance, or dependency is unavailable.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
[[clouddevopsengineersguide.pdf]]
