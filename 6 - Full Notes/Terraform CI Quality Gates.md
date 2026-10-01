2026-09-30 23:18

Status: #baby

Tags: [[Terraform Delivery and Production Operations]]

# Terraform CI Quality Gates

Terraform continuous integration checks configuration before it can modify infrastructure. Formatting and `terraform validate` establish basic consistency, TFLint detects Terraform and provider problems, documentation generation keeps module interfaces visible, and [[Infrastructure as Code Security Scanning]] evaluates the proposed resources against policy.

These checks become quality gates when a failed result blocks merge or deployment rather than merely producing a report. A [[Terraform Plan Artifact]] then shows the combined consequence of configuration and provider behavior. The gate should be proportional to risk: destructive actions, identity changes, public exposure, and production targets deserve stronger review than a disposable development environment.

# References

[[masteringterraform.pdf]]

