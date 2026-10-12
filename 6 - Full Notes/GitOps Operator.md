2026-09-27 22:21

Status: #baby

Tags: [[GitOps Deployment Operations]] [[Platform Delivery and Artifact Automation]]

# GitOps Operator

A GitOps operator is a trusted agent running inside a managed environment that watches a [[GitOps Desired-State Repository]] and applies its definitions. Argo CD and Flux are examples for Kubernetes-oriented workflows.

The operator repeatedly compares repository state with live state, applies approved differences, reports synchronization health, and can remove objects deleted from Git or reverse unauthorized manual changes. Its permissions are powerful but localized: it needs authority in the environment it reconciles, while the broader CI system can remain outside the production credential boundary.

The operator can emit lifecycle notifications before, during, after, or upon failure of synchronization. Those events make the reconciliation step visible to release checks and application-lifecycle automation without giving the external build system direct deployment authority.

# References

[[clouddevopsengineersguide.pdf]]

[[platformengineeringforarchitects.pdf]]
