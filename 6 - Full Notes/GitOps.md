2026-09-27 22:21

Status: #baby

Tags: [[GitOps Deployment Operations]] [[Platform Delivery and Artifact Automation]]

# GitOps

GitOps is an operational framework that treats Git as the authoritative record of a system's desired application and infrastructure state. Production changes begin as reviewed repository changes rather than direct commands against the running environment.

[[Continuous Integration]] still builds artifacts, runs tests and scans, and validates manifests, but it does not push those manifests into production. An in-environment [[GitOps Operator]] pulls approved definitions and continuously compares them with actual state. This arrangement makes changes auditable and reversible while shifting production credentials away from the general CI system.

Within a platform release process, GitOps joins an immutable artifact to version-controlled deployment definitions and target-specific configuration. Promotion becomes a reviewed change to desired state, while synchronization events provide evidence for pre-deployment, post-deployment, and lifecycle orchestration.

For Kubernetes container delivery, this separates image production from deployment reconciliation: CI publishes a tested image, a reviewed manifest change selects its immutable version, and an in-cluster agent converges the running workload. Drift becomes visible as a difference from the repository instead of an undocumented production fact.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]

[[clouddevopsengineersguide.pdf]]

[[platformengineeringforarchitects.pdf]]
