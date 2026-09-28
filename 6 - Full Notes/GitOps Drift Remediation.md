2026-09-27 22:21

Status: #baby

Tags: [[GitOps Deployment Operations]]

# GitOps Drift Remediation

GitOps drift remediation restores an environment when its actual state no longer matches the reviewed definition in Git. Drift can result from a manual command, another controller, or a failed partial change, and it is detected by [[GitOps Continuous Reconciliation]].

With self-healing enabled, the operator reapplies repository state instead of allowing an undocumented fix to become the new authority. This makes direct emergency changes temporary unless they are codified through a [[Pull Request]]. Automatic correction should still expose status and failures because a repeatedly reintroduced drift may indicate competing controllers or an invalid desired state.

# References

[[clouddevopsengineersguide.pdf]]

