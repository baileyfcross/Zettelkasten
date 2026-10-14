2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Backup and Restore Operations]]

# Velero Opt-In Backup Policy

An opt-in Velero policy backs up persistent volumes only when the workload explicitly requests protection through the expected annotation or configuration. This limits storage consumption and avoids copying data whose application has another recovery mechanism.

The tradeoff is omission risk: a team may assume that its data is protected when it never added the marker. Admission checks, platform templates, inventory reports, and restore exercises should make the selection visible rather than relying on tribal knowledge.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

