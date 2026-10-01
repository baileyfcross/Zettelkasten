2026-09-06 22:42

Status: #baby

Tags: [[Parallel Workload Resource Management]] [[Modern Software Delivery Foundations]]

# Rollback Recovery

Rollback recovery restores an application to an earlier checkpoint after a failure. Computation performed since the checkpoint is lost and must be repeated, so recovery time includes both restart overhead and recomputation.

In a co-scheduled pack, one application's rollback can create load imbalance even when other applications continue normally.

For production change assurance, rollback readiness includes supported version switching, verified procedures, responsible owners, and observability that reveals when recovery is needed. A nominal rollback option is not sufficient if state or dependency changes make the previous version unusable.

# References

[[llmsformodernsoftwaredeliveryanddevops.pdf]]

[[bigdatamanagementandprocessing.pdf]]
