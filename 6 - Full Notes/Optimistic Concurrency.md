2026-09-22 20:53

Status: #baby

Tags: [[Aggregate Consistency and Persistence]]

# Optimistic Concurrency

Optimistic concurrency allows work to proceed without holding a lock, then verifies at commit time that the persisted [[Aggregate]] has not changed since it was read. A version value is loaded with the aggregate and supplied as the expected version when saving. If another command committed first, the mismatch rejects the stale write instead of overwriting it. In [[Event Sourcing]], the number or revision of events in an [[Event Stream]] provides the aggregate version naturally.

# References

[[hands-ondomain-drivendesignwithnetcore.pdf]]
