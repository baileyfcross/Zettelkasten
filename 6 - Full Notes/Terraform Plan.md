2026-09-27 22:21

Status: #baby

Tags: [[Terraform Infrastructure as Code]]

# Terraform Plan

A Terraform plan is a preview of the actions Terraform proposes after comparing configuration, [[Terraform State]], and the current infrastructure. It identifies resources that would be created, changed in place, replaced, or destroyed without performing those operations.

The plan is both a safety mechanism and a review artifact. A CI workflow can publish it on a [[Pull Request]] so reviewers see infrastructure consequences rather than only source differences. Destructive actions, security-rule changes, and other high-risk effects should receive explicit attention before `terraform apply`, especially when a production [[Manual Deployment Approval]] follows.

# References

[[clouddevopsengineersguide.pdf]]

