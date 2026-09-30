2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Backup and Restore Operations]]

# Scheduled Velero Backup

A scheduled Velero backup creates recurring recovery points from a cron expression or supported shorthand schedule. The schedule holds the backup template, while each execution produces a separately inspectable backup object.

Frequency and retention should follow recovery-point objectives and data change rate rather than convenience. Monitoring must detect missed or partially failed runs, and periodic restore tests must prove that a long series of successful schedules still yields usable data.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

