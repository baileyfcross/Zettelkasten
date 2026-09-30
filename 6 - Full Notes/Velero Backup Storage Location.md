2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Backup and Restore Operations]]

# Velero Backup Storage Location

A Velero BackupStorageLocation describes the object store and provider configuration used to retain Kubernetes backup metadata and resources. An S3-compatible service such as MinIO can serve this role for a lab, while production systems normally require durable, access-controlled storage outside the protected cluster.

The location must remain reachable during disaster recovery and should not depend on the same failure domain as the workloads it protects. Credentials, retention, immutability, encryption, and cross-region or cross-provider availability determine whether the stored backup survives the event that requires it.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

