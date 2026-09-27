2026-09-27 18:58

Status: #baby

Tags: [[AWS Account Governance and Identity]]

# AWS Temporary Credentials

AWS temporary credentials are time-limited access key, secret key, and session token values issued through AWS Security Token Service when a role or federated session is assumed. They expire automatically and inherit the permissions and constraints of that session.

Their limited lifetime reduces exposure compared with permanent keys, but they still require secure delivery and must not be logged. Workloads should obtain them from an assigned role rather than embedding credentials in source code or machine images.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
