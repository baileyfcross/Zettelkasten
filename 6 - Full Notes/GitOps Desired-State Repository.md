2026-09-27 22:21

Status: #baby

Tags: [[GitOps Deployment Operations]]

# GitOps Desired-State Repository

A GitOps desired-state repository contains the declarative manifests that define what an application environment should run. Its history records who proposed and approved each production change, while reverting a commit provides a controlled way to return the declared state to an earlier version.

The repository is distinct from whatever happens to be running at the moment: it is the authority that the [[GitOps Operator]] uses during reconciliation. A useful layout separates application manifests from cluster-wide infrastructure and separates shared bases from environment-specific overlays. Plaintext secrets do not belong in this history.

# References

[[clouddevopsengineersguide.pdf]]

