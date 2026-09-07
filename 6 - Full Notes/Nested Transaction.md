2026-09-06 22:42

Status: #baby

Tags: [[In-Memory Data Processing]]

# Nested Transaction

A nested transaction decomposes a parent transaction into inner transactions with their own execution boundaries. The structure expresses internal parallelism, partial recovery, or modular composition while preserving rules about the parent's final outcome.

Nesting semantics determine when an inner result becomes visible and whether its effects are undone if the parent later aborts.

# References

[[bigdatamanagementandprocessing.pdf]]
