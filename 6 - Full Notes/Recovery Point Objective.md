2026-09-09 00:00

Status: #baby

Tags: [[Cloud Security Monitoring and Resilience]]

# Recovery Point Objective

A recovery point objective is the maximum targeted age of data that may be lost when a system is restored after disruption. It describes how far back in time the recovered state may be compared with the moment of failure.

The objective determines how frequently data must be replicated or backed up. It is distinct from [[Recovery Time Objective]], which measures the acceptable duration of the outage rather than the acceptable amount of lost history.

A smaller RPO requires more frequent capture or continuous replication, but replication can copy corruption as readily as valid changes. Recovery design therefore combines replication with versioned or isolated backups and proves restoration from a known point. Different data sets may justify different objectives according to business impact.

# References

[[cloudcomputing_mit.epub]]
[[clouddevopsengineersguide.pdf]]
