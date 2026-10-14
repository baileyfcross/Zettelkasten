2026-09-08 21:16

Status: #baby

Tags: [[.NET Task Parallelism and Asynchrony]] [[.NET Synchronization and Thread Coordination]] [[Linux Kernel Locking]]

# Mutual Exclusion Lock

A mutual-exclusion lock permits only one thread at a time to enter a protected critical section. In C#, the `lock` statement uses monitor semantics to acquire an object before the body and release it reliably afterward.

The protected region should be small, and all accesses to the shared invariant must follow the same locking discipline. Locking publicly accessible objects or performing slow and blocking operations while holding a lock increases contention and deadlock risk.

A monitor-backed C# lock is process-local, while a named mutex can coordinate ownership across process boundaries at greater operating-system cost. The scope of the protected resource determines which form of mutual exclusion is appropriate.

A Linux kernel mutex is a sleeping lock for process context: contention can deschedule the waiter, and only the owner may unlock it. It cannot be acquired in interrupt or other atomic context, where a [[SpinLock]] or a lock-free technique must protect the state without sleeping.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
[[linuxkernelprogramming_secondedition.pdf]]
