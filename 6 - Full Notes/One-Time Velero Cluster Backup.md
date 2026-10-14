2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Backup and Restore Operations]]

# One-Time Velero Cluster Backup

A one-time Velero backup captures a selected set of Kubernetes resources and volume data on demand. It is useful before a risky upgrade, migration, or configuration change because the recovery point is tied to a known operational event.

Selection can include or exclude namespaces, resource types, labels, and volumes. Operators should record the resulting backup status and errors, because a named backup object can exist even when some resources or volume operations did not complete successfully.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

