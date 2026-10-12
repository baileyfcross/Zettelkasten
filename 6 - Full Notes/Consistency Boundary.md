2026-09-22 20:53

Status: #baby

Tags: [[Aggregate Consistency and Persistence]]

# Consistency Boundary

A consistency boundary encloses the smallest set of state that must obey business rules immediately after an operation. Inside an [[Aggregate]], the root protects invariants across all child entities and value objects. State outside the boundary is not guaranteed to change atomically and may require messages or [[Eventual Consistency]]. Making this boundary explicit prevents a database-wide object graph from turning every update into a potentially conflicting transaction.

# References

[[hands-ondomain-drivendesignwithnetcore.pdf]]
