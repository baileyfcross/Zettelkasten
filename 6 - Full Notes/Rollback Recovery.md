2026-09-06 22:42

Status: #baby

Tags: [[Parallel Workload Resource Management]]

# Rollback Recovery

Rollback recovery restores an application to an earlier checkpoint after a failure. Computation performed since the checkpoint is lost and must be repeated, so recovery time includes both restart overhead and recomputation.

In a co-scheduled pack, one application's rollback can create load imbalance even when other applications continue normally.

# References

[[bigdatamanagementandprocessing.pdf]]
