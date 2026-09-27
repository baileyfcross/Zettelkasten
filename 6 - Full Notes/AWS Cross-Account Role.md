2026-09-27 18:58

Status: #baby

Tags: [[AWS Account Governance and Identity]]

# AWS Cross-Account Role

An AWS cross-account role grants a principal from one account a temporary session in another. The target role's trust policy accepts the external principal, while its permission policy limits what the assumed session can do.

This pattern avoids copying users and long-lived credentials into every account. Both sides participate: the source principal needs permission to assume the role, and the target role must trust it. Logging the role session preserves the cross-account path.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
