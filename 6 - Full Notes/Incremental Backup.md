2026-09-09 00:00

Status: #baby

Tags: [[Backup and Recovery Strategies]]

# Incremental Backup

An incremental backup copies new or changed files since the previous incremental backup. The first set establishes a complete baseline, and each subsequent set records only the next changes.

Incrementals reduce backup time and storage and can preserve several versions across sets. Complete restoration requires the baseline and every necessary increment in order, so a missing or damaged set can interrupt the recovery chain.

# References

[[cloudcomputing_mit.epub]]
