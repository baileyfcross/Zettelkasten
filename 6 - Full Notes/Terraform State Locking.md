2026-09-27 22:21

Status: #baby

Tags: [[Terraform Infrastructure as Code]]

# Terraform State Locking

Terraform state locking ensures that only one operation can modify a shared state at a time. Without a lock, two pipeline runs can read the same starting state, make conflicting infrastructure changes, and overwrite one another's records.

The book pairs an S3 [[Terraform Remote Backend]] with a DynamoDB lock table. A run acquires a lock before planning or applying and releases it after the state has been written. A failed run can leave a stale lock that requires careful removal, but deleting a live lock merely to unblock another job risks state corruption.

# References

[[clouddevopsengineersguide.pdf]]

