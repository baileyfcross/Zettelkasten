2026-09-27 22:21

Status: #baby

Tags: [[GitOps Deployment Operations]]

# GitOps Production Credential Boundary

The GitOps production credential boundary separates artifact preparation from permission to change the live environment. CI needs access to source, tests, scanners, and artifact registries, while the [[GitOps Operator]] inside the environment holds the narrower authority required to reconcile production resources.

This reduces the blast radius of a compromised build system because a successful CI job cannot directly issue administrative cluster commands. The boundary is not absolute protection: a malicious artifact or manifest can still travel through the approved path, so code review, policy checks, signature verification, and least-privilege operator permissions remain necessary.

# References

[[clouddevopsengineersguide.pdf]]

