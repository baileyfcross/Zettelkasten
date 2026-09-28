2026-09-27 22:21

Status: #baby

Tags: [[GitOps Deployment Operations]]

# GitOps Secret Management Constraint

GitOps requires desired state to be reviewable in Git, but plaintext credentials must not be stored in that permanent history. Removing a secret from a later commit does not erase it from earlier clones or revisions.

A GitOps design therefore needs a separate mechanism that lets declarative manifests reference protected values without exposing them. The mechanism must work during reconciliation and recovery, preserve environment separation, and give the operator only the access it needs. [[Dynamic Secret|Short-lived credentials]] further reduce the impact of disclosure when the external system supports them.

# References

[[clouddevopsengineersguide.pdf]]

