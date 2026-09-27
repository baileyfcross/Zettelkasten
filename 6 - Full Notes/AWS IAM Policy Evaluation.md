2026-09-27 18:58

Status: #baby

Tags: [[AWS Account Governance and Identity]]

# AWS IAM Policy Evaluation

AWS IAM policy evaluation compares a principal's request with applicable identity policies, resource policies, permissions boundaries, organization guardrails, and session constraints. Requests begin with an implicit deny, require an applicable allow, and remain denied if any relevant policy contains an explicit deny.

A policy statement specifies effect, actions, resources, and optional conditions. The IAM Policy Simulator can test expected outcomes, but production access must also account for trust policies and the exact request context.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
