2026-09-09 00:00

Status: #baby

Tags: [[Backup and Recovery Strategies]]

# Backup Fileset

A backup fileset is the selected collection of files and directories included in a backup job. It partitions a file-system hierarchy more narrowly than backing up every object on the volume.

Defining the fileset makes backup scope explicit and allows different data to receive different schedules, permissions, and retention. Recovery will be incomplete if an important dependency was never included, so the selection must follow the system's actual data relationships.

# References

[[cloudcomputing_mit.epub]]
