2026-09-27 18:58

Status: #baby

Tags: [[AWS Managed Database Services]]

# Amazon RDS

Amazon Relational Database Service operates supported relational database engines while AWS manages tasks such as provisioning, patching, monitoring, and backup mechanisms. Applications still use familiar SQL engines and schemas.

The customer chooses engine, instance capacity, storage, network placement, credentials, availability mode, and retention. Managed operation reduces undifferentiated administration but does not replace data modeling, query tuning, authorization, or recovery testing.

A Multi-AZ deployment maintains a synchronized standby for availability, whereas a read replica serves read scaling and can have replication lag. Those features solve different problems. Connection-heavy applications can add [[Amazon RDS Proxy]] so bursts of short-lived clients do not exhaust database connections.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]

[[awsforsolutionsarchitectsthirdedition.pdf]]
