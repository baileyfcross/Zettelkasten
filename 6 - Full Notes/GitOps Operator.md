2026-09-27 22:21

Status: #baby

Tags: [[GitOps Deployment Operations]]

# GitOps Operator

A GitOps operator is a trusted agent running inside a managed environment that watches a [[GitOps Desired-State Repository]] and applies its definitions. Argo CD and Flux are examples for Kubernetes-oriented workflows.

The operator repeatedly compares repository state with live state, applies approved differences, reports synchronization health, and can remove objects deleted from Git or reverse unauthorized manual changes. Its permissions are powerful but localized: it needs authority in the environment it reconciles, while the broader CI system can remain outside the production credential boundary.

# References

[[clouddevopsengineersguide.pdf]]

