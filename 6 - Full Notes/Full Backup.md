2026-09-09 00:00

Status: #baby

Tags: [[Backup and Recovery Strategies]]

# Full Backup

A full backup copies the entire selected fileset each time the backup job runs. Every resulting backup set contains both unchanged and changed items from that scope.

Restoration is straightforward because one set contains the complete snapshot, but repeatedly copying everything consumes more time and storage than change-based schemes. The simplicity can be valuable when fast, dependable recovery matters more than backup efficiency.

# References

[[cloudcomputing_mit.epub]]
