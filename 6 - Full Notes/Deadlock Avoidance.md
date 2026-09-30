2026-09-08 21:16

Status: #baby

Tags: [[.NET Task Parallelism and Asynchrony]] [[.NET Synchronization and Thread Coordination]] [[Linux Kernel Locking]]

# Deadlock Avoidance

A deadlock arises when participants wait permanently for resources held by one another. A classic case occurs when two threads acquire the same pair of locks in opposite orders and each waits for the lock held by the other.

Consistent lock ordering, smaller critical sections, time-bounded acquisition, and fewer shared resources reduce the risk. Asynchronous code should also avoid synchronously blocking on incomplete tasks, which can create a waiting cycle with a captured execution context.

Linux kernel code formalizes this discipline through [[Lock Ordering]], avoids reacquiring non-recursive locks, and accounts for interrupt paths that can deadlock with interrupted code. [[Lockdep]] records observed dependency classes and reports potential cycles during testing before the rare interleaving becomes a production hang.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
[[linuxkernelprogramming_secondedition.pdf]]
