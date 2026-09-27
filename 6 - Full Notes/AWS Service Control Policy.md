2026-09-27 18:58

Status: #baby

Tags: [[AWS Account Governance and Identity]]

# AWS Service Control Policy

An AWS Service Control Policy sets the maximum permissions available to accounts in an organization or organizational unit. It can deny unwanted services, regions, or actions even when an IAM policy inside the account would otherwise allow them.

An SCP does not grant permission by itself. A principal still needs an identity or resource policy that permits the action, and an explicit SCP denial wins. This makes SCPs organization-wide guardrails rather than substitutes for least-privilege IAM design.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
