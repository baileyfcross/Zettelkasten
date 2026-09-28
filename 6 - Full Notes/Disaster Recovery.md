2026-09-09 00:00

Status: #baby

Tags: [[Cloud Security Monitoring and Resilience]]

# Disaster Recovery

Disaster recovery restores data and computing services after a disruptive event. It is the technical recovery portion of a broader [[Business Continuity Plan]] and should be guided by a [[Recovery Time Objective]] and [[Recovery Point Objective]].

A secondary cloud or data center can provide recovery capacity, but recovery depends on current copies, compatible services, secure access, and practiced procedures. Merely possessing a backup does not prove that the complete application can be restored in time.

Common cloud strategies trade recovery speed against standing cost: backup-and-restore creates most capacity after the event, pilot light keeps critical foundations running, warm standby maintains a scaled-down environment, and multi-site operation keeps multiple locations ready. The chosen strategy must satisfy both [[Recovery Time Objective]] and [[Recovery Point Objective]] under an exercised runbook.

# References

[[cloudcomputing_mit.epub]]
[[clouddevopsengineersguide.pdf]]
