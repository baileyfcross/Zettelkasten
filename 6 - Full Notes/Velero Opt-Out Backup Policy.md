2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Backup and Restore Operations]]

# Velero Opt-Out Backup Policy

An opt-out Velero policy protects eligible persistent volumes by default unless a workload explicitly excludes them. It favors coverage and reduces the chance that newly created state is silently omitted from the backup set.

Default inclusion can increase cost and capture transient or reproducible data unnecessarily. Exclusions need ownership and review, while retention and restore tests should distinguish merely backed-up volumes from application states that are actually useful after recovery.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

