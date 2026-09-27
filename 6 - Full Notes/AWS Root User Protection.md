2026-09-27 18:58

Status: #baby

Tags: [[AWS Account Governance and Identity]]

# AWS Root User Protection

The AWS root user has unrestricted account authority and can perform account-level tasks unavailable to ordinary identities. It should not be used for daily administration, application access, or automation.

Protection includes a unique strong password, multi-factor authentication, no root access keys, securely controlled recovery channels, and use only for exceptional tasks. Administrative work should occur through named or federated roles so actions are scoped and auditable.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
