2026-09-27 18:58

Status: #baby

Tags: [[AWS Account Governance and Identity]]

# AWS IAM Role

An AWS IAM role is an identity with permissions that an authorized person, service, or workload can assume. It has a trust policy defining who may assume it and permission policies defining what the resulting session may do.

Roles issue temporary credentials instead of requiring a password or permanent access key. They are the preferred mechanism for EC2 applications, AWS services, federation, and cross-account access because access can be narrowly scoped and expires with the session.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
