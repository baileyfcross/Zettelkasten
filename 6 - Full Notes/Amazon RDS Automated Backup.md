2026-09-27 18:58

Status: #baby

Tags: [[AWS Managed Database Services]]

# Amazon RDS Automated Backup

Amazon RDS automated backup captures database storage and transaction logs during a configured retention period, enabling point-in-time restoration within that window. Manual snapshots persist until explicitly removed and can mark planned recovery points.

A restore creates another database instance rather than rewinding the running instance in place. Retention, backup windows, encryption, cross-region copies, and restore drills should follow recovery objectives rather than relying on the existence of a backup setting.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
