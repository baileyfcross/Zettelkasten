2026-09-27 22:21

Status: #baby

Tags: [[Cloud-Native DevSecOps Controls]]

# CI Security Quality Gate

A CI security quality gate converts security findings into a repeatable promotion decision. It can prevent a build or deployment when a scan reports a disallowed severity, an exposed secret, a policy violation, or another condition the team has defined as unacceptable.

The gate should combine clear thresholds with an auditable exception path; otherwise teams may bypass a control that blocks work without explaining how to recover. It can aggregate [[Static Application Security Testing]], dependency, image, secret, and infrastructure scan results, while production authorization may also require a [[Manual Deployment Approval]].

# References

[[clouddevopsengineersguide.pdf]]
