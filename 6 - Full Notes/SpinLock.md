2026-09-27 00:11

Status: #baby

Tags: [[.NET Synchronization and Thread Coordination]] [[Linux Kernel Locking]]

# SpinLock

`SpinLock` protects a critical section by waiting actively rather than immediately blocking the thread. It can reduce scheduler overhead when contention is rare and the holder releases the lock in only a few instructions.

Because it is a value type, copying it can accidentally create independent locks, and thread-owner tracking adds diagnostic cost. Long work, I/O, or unpredictable scheduling inside the protected region makes spinning wasteful and favors a blocking lock.

In Linux kernel code, acquiring a spinlock disables preemption while it is held, and the protected path must neither sleep nor perform unbounded work. Data also reachable from an interrupt handler needs the appropriate [[Spinlock Interrupt Variants|interrupt-aware variant]] so the local handler cannot deadlock by preempting the lock holder.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
[[linuxkernelprogramming_secondedition.pdf]]
