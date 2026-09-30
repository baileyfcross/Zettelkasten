2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Backup and Restore Operations]]

# Cross-Cluster Velero Migration

A cross-cluster Velero migration builds a destination cluster, connects it to the backup location, and restores selected workloads and volume data from the source environment. The process tests whether application state is portable beyond the original control plane.

Successful migration depends on compatible API versions, custom resources, storage classes, networking, image access, secrets, and external services. Building the destination before restoration also separates infrastructure reconstruction from workload recovery and exposes hidden provider assumptions.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]
