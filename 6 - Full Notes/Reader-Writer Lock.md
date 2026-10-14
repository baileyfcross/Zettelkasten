2026-09-27 00:11

Status: #baby

Tags: [[.NET Synchronization and Thread Coordination]] [[Linux Kernel Locking]]

# Reader-Writer Lock

A reader-writer lock permits several readers to hold the protected resource concurrently while giving a writer exclusive access. It can improve throughput when reads are common, writes are infrequent, and the protected operations are long enough to justify the more complex lock.

Upgrade, recursion, and fairness policies affect contention and starvation. `ReaderWriterLockSlim` reduces overhead for in-process coordination, but an ordinary mutual-exclusion lock is often clearer when the workload does not exhibit genuine read concurrency.

Linux offers a spin-based reader-writer lock for atomic contexts, but read-side updates to shared lock state can cause cache-line bouncing and sustained readers can delay writers. Read-mostly kernel structures often scale better with [[Read-Copy-Update]], while sleeping read sections can use a [[Reader-Writer Semaphore]].

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
[[linuxkernelprogramming_secondedition.pdf]]
