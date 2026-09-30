2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Backup and Restore Operations]]

# Velero Persistent Volume Backup

A Velero persistent-volume backup protects workload data in addition to Kubernetes object definitions. Depending on the environment, it can coordinate storage snapshots or move file-system data through a node-level backup mechanism.

Application consistency is not guaranteed merely because bytes were copied. Databases may require quiescing, hooks, or native backups, and a restore needs compatible storage classes, access modes, capacity, and encryption keys in the destination cluster.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

