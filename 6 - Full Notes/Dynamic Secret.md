2026-09-27 22:21

Status: #baby

Tags: [[Cloud-Native DevSecOps Controls]]

# Dynamic Secret

A dynamic secret is generated on demand for a specific workload, identity, or session and expires after a short lease. Unlike a long-lived shared credential, it can be scoped to the immediate task and becomes unusable automatically after its lifetime ends.

Dynamic issuance reduces the value of a leaked credential and avoids distributing one static value across many systems. It requires a trusted broker, authenticated workload identity, renewal behavior for long-running processes, and a plan for broker availability. It complements rather than replaces [[Repository Secret Scanning]] because applications can still expose issued values accidentally.

# References

[[clouddevopsengineersguide.pdf]]
