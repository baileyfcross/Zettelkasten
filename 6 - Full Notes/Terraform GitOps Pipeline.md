2026-09-30 23:18

Status: #baby

Tags: [[Terraform Delivery and Production Operations]]

# Terraform GitOps Pipeline

A Terraform GitOps pipeline makes the repository the authoritative path for infrastructure change. A feature branch changes HCL, a pull request exposes validation and a [[Terraform Plan]], and merging an approved change triggers or authorizes [[Terraform Apply]] against the intended environment.

Declarative import and state-move blocks keep exceptional operations in the same review history instead of relying on an operator's undocumented command. Credentials and backend configuration remain pipeline concerns rather than source files. Unlike continuous reconciliation by a [[GitOps Operator]], ordinary Terraform runs are event-driven, so drift detection and scheduled validation must be added deliberately when the organization needs continuous assurance.

# References

[[masteringterraform.pdf]]

