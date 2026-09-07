2026-09-06 22:42

Status: #baby

Tags: [[In-Memory Data Processing]]

# Parallel Nested Transaction

A parallel nested transaction runs independent or compatible inner transactions concurrently within one parent operation. The scheduler must preserve the nesting semantics while exposing enough internal structure to assign inner work to different workers.

Parallel nesting can shorten a complex transaction, but hidden dependencies may turn apparent concurrency into repeated aborts or serialization.

# References

[[bigdatamanagementandprocessing.pdf]]
