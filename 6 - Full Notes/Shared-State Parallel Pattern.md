2026-09-27 00:11

Status: #baby

Tags: [[.NET Server Concurrency and Parallel Patterns]]

# Shared-State Parallel Pattern

The shared-state parallel pattern lets concurrent workers read or update a common in-memory object. It avoids message-copying overhead and can make rapidly changing state immediately visible across participants.

Every invariant spanning that state requires an ownership or synchronization rule. Locks, concurrent collections, immutability, partitioning, or atomic operations can supply the rule, but unstructured shared writes create races whose results depend on timing.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
