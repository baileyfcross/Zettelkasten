2026-09-08 21:16

Status: #baby

Tags: [[.NET Task Parallelism and Asynchrony]]

# Mutual Exclusion Lock

A mutual-exclusion lock permits only one thread at a time to enter a protected critical section. In C#, the `lock` statement uses monitor semantics to acquire an object before the body and release it reliably afterward.

The protected region should be small, and all accesses to the shared invariant must follow the same locking discipline. Locking publicly accessible objects or performing slow and blocking operations while holding a lock increases contention and deadlock risk.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
