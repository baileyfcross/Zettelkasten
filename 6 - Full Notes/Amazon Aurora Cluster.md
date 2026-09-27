2026-09-27 18:58

Status: #baby

Tags: [[AWS Managed Database Services]]

# Amazon Aurora Cluster

An Amazon Aurora cluster uses MySQL- or PostgreSQL-compatible database instances over distributed storage that maintains multiple copies across three availability zones. A writer handles changes while reader instances can scale reads and support failover.

Separating compute from clustered storage allows replicas to share one durable storage system and supports self-healing behavior. Compatibility reduces migration effort but does not guarantee that every engine feature or operational assumption is identical.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
