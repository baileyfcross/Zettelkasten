2026-09-27 22:21

Status: #baby

Tags: [[GitOps Deployment Operations]]

# GitOps

GitOps is an operational framework that treats Git as the authoritative record of a system's desired application and infrastructure state. Production changes begin as reviewed repository changes rather than direct commands against the running environment.

[[Continuous Integration]] still builds artifacts, runs tests and scans, and validates manifests, but it does not push those manifests into production. An in-environment [[GitOps Operator]] pulls approved definitions and continuously compares them with actual state. This arrangement makes changes auditable and reversible while shifting production credentials away from the general CI system.

# References

[[clouddevopsengineersguide.pdf]]

