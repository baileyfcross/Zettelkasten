2026-09-27 22:21

Status: #baby

Tags: [[GitOps Deployment Operations]]

# GitOps Declarative Disaster Recovery

GitOps supports declarative disaster recovery by keeping the reviewed environment definition outside the cluster it controls. If a cluster is lost, a replacement can be created, connected to the [[GitOps Desired-State Repository]], and reconciled toward the recorded application and infrastructure state.

This improves repeatability but does not make Git a complete [[Disaster Recovery]] system. Persistent business data, external identities, encryption keys, registries, and the repository itself need their own backup and restoration strategies. Recovery drills must prove that those dependencies and credentials are available to the replacement operator.

# References

[[clouddevopsengineersguide.pdf]]

