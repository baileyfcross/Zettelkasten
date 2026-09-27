2026-09-27 18:58

Status: #baby

Tags: [[AWS Availability Scaling and Edge Delivery]]

# AWS Fault Tolerance

Fault tolerance is the capacity to continue operating when a component fails, often with little or no visible interruption. It requires enough redundancy and isolation that a failed instance, zone, or network path does not exhaust the workload's remaining capacity.

It is stronger than simply having backups: backups support recovery, whereas fault-tolerant architecture keeps serving requests during failure. AWS designs often combine multiple [[AWS Availability Zone|Availability Zones]], [[Elastic Load Balancing]], health checks, and automatically replaced compute capacity to approach this goal.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
