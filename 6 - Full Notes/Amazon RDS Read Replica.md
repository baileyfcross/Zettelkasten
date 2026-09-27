2026-09-27 18:58

Status: #baby

Tags: [[AWS Managed Database Services]]

# Amazon RDS Read Replica

An Amazon RDS read replica asynchronously copies changes from a source database and exposes another endpoint for read traffic. It can scale reporting or query workloads and may be promoted when a separate writable database is needed.

Replication lag means a replica may not contain the latest committed data. A read replica is therefore a scaling feature distinct from synchronous Multi-AZ failover, even though replicas can also participate in recovery strategies.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
