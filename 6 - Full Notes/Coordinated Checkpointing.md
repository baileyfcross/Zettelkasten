2026-09-06 22:42

Status: #baby

Tags: [[Parallel Workload Resource Management]]

# Coordinated Checkpointing

Coordinated checkpointing records a consistent recovery state across the processes of a parallel application. After a failure, the application can resume from that saved state rather than restart from the beginning.

Frequent checkpoints reduce lost computation but add more storage and synchronization overhead. The useful interval depends on failure rate and checkpoint cost.

# References

[[bigdatamanagementandprocessing.pdf]]
