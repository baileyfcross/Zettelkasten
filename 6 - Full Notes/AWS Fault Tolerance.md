2026-09-27 18:58

Status: #baby

Tags: [[AWS Availability Scaling and Edge Delivery]]

# AWS Fault Tolerance

Fault tolerance is the capacity to continue operating when a component fails, often with little or no visible interruption. It requires enough redundancy and isolation that a failed instance, zone, or network path does not exhaust the workload's remaining capacity.

It is stronger than simply having backups: backups support recovery, whereas fault-tolerant architecture keeps serving requests during failure. AWS designs often combine multiple [[AWS Availability Zone|Availability Zones]], [[Elastic Load Balancing]], health checks, and automatically replaced compute capacity to approach this goal.

Fault tolerance therefore describes behavior during a failure, while high availability may accept a short interruption as the service recovers. Greater tolerance usually requires more independent capacity, state replication, and automated failover, so the appropriate design follows business impact and service objectives rather than treating maximum redundancy as free.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
[[clouddevopsengineersguide.pdf]]
