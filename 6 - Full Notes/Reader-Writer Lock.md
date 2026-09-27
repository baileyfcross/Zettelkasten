2026-09-27 00:11

Status: #baby

Tags: [[.NET Synchronization and Thread Coordination]]

# Reader-Writer Lock

A reader-writer lock permits several readers to hold the protected resource concurrently while giving a writer exclusive access. It can improve throughput when reads are common, writes are infrequent, and the protected operations are long enough to justify the more complex lock.

Upgrade, recursion, and fairness policies affect contention and starvation. `ReaderWriterLockSlim` reduces overhead for in-process coordination, but an ordinary mutual-exclusion lock is often clearer when the workload does not exhibit genuine read concurrency.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
