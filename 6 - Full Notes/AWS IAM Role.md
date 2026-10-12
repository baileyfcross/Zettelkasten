2026-09-27 18:58

Status: #baby

Tags: [[AWS Account Governance and Identity]]

# AWS IAM Role

An AWS IAM role is an identity with permissions that an authorized person, service, or workload can assume. It has a trust policy defining who may assume it and permission policies defining what the resulting session may do.

Roles issue temporary credentials instead of requiring a password or permanent access key. They are the preferred mechanism for EC2 applications, AWS services, federation, and cross-account access because access can be narrowly scoped and expires with the session.

Pipeline stages should assume distinct roles rather than share one broad deployment identity. A build role may read source and publish an artifact, while a production role may modify only the resources required for release. Separating trust from permissions and scoping each session limits the blast radius of a compromised job.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
[[clouddevopsengineersguide.pdf]]
