2026-09-27 22:21

Status: #baby

Tags: [[Azure Kubernetes Service Operations]]

# Helm Release

A Helm release is one installed instance of a [[Helm Chart]] in a Kubernetes cluster. The same chart can be installed more than once with different release names and values, producing separately managed application instances.

Helm records release revisions so an upgrade can be inspected and a faulty change can be rolled back. The release abstraction manages the chart-generated resources as a unit, but it does not remove the need to observe workload health or validate environment-specific values before promotion.

# References

[[clouddevopsengineersguide.pdf]]

