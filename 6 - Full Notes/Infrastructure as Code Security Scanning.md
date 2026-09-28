2026-09-27 22:21

Status: #baby

Tags: [[Cloud-Native DevSecOps Controls]]

# Infrastructure as Code Security Scanning

Infrastructure as code security scanning evaluates declarative cloud and cluster configuration before it creates resources. Rules can flag public storage, overly broad network access, missing encryption, privileged containers, or permissive identity policies while the proposed change is still reviewable.

The scan complements a [[Terraform Plan]] because the plan explains the infrastructure change while the security rules judge selected properties of it. Results should be visible in code review and enforced through a proportionate [[CI Security Quality Gate]]. Runtime posture monitoring is still needed for drift and changes made outside the declared workflow.

# References

[[clouddevopsengineersguide.pdf]]
