2026-09-27 22:21

Status: #baby

Tags: [[GitOps Deployment Operations]]

# GitOps Continuous Reconciliation

GitOps continuous reconciliation is the loop that compares the desired state in Git with the actual state of the managed environment and acts when they differ. The loop turns a merged definition into deployment and continues operating after deployment rather than treating one successful apply as permanent correctness.

Reconciliation can create, update, or prune resources and report whether the result became healthy. It resembles the control behavior inside [[Kubernetes Reconciliation Loop|Kubernetes]], but its comparison crosses the boundary between a repository and the environment. This persistence enables [[GitOps Drift Remediation]] when an out-of-band change alters live state.

# References

[[clouddevopsengineersguide.pdf]]

