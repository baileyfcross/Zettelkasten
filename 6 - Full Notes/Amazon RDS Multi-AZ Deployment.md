2026-09-27 18:58

Status: #baby

Tags: [[AWS Managed Database Services]]

# Amazon RDS Multi-AZ Deployment

An Amazon RDS Multi-AZ deployment maintains a synchronized standby or cluster members in separate availability zones. When the primary fails, RDS can fail over the database endpoint to healthy capacity without requiring the application to select a new address.

The standby in a traditional Multi-AZ instance deployment serves availability rather than read scaling. Multi-AZ reduces a zone-level single point of failure, but applications still need retry behavior and tested recovery for region-wide or logical data failures.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
