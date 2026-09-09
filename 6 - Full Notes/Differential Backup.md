2026-09-09 00:00

Status: #baby

Tags: [[Backup and Recovery Strategies]]

# Differential Backup

A differential backup copies files that changed since the most recent [[Full Backup]]. Each later differential grows to include every change accumulated after that common full snapshot.

Restoring the complete fileset generally requires the last full backup and the latest differential. This uses less storage than repeated full backups and fewer sets than a long incremental chain, while making individual-file location more complex than a single full set.

# References

[[cloudcomputing_mit.epub]]
