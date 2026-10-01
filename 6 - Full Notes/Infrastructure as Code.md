2026-09-27 22:21

Status: #baby

Tags: [[Terraform Cloud Deployment Patterns]]

# Infrastructure as Code

Infrastructure as Code manages compute, storage, networking, and other platform resources through machine-readable definitions instead of repeated console operations. The definitions can enter a [[Source Code Repository]], where their history, review, and automated execution receive the same discipline as application code.

This practice replaces slow and inconsistent click-ops with repeatable provisioning. It reduces configuration differences among environments, makes an infrastructure change visible in a [[Pull Request]], and permits temporary test environments to be created and destroyed when they are no longer needed. The code does not remove operational risk; it makes the intended state inspectable and reproducible.

Terraform applies this discipline across cloud platforms through a common workflow while allowing each provider to expose its platform's distinctive resources. Reuse therefore comes from stable architectural boundaries and [[Terraform Module|modules]], not from pretending that AWS, Azure, and Google Cloud have identical network or identity models.

# References

[[clouddevopsengineersguide.pdf]]
[[masteringterraform.pdf]]
