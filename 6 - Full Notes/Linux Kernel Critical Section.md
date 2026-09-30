2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Locking]]

# Linux Kernel Critical Section

A Linux kernel critical section is a region that accesses shared state under a synchronization rule that prevents harmful concurrent execution. The required protection depends on whether competing access can come from another process, another CPU, an interrupt, or a deferred interrupt handler.

The smallest correct protection scope usually reduces contention and latency, but operations that form one invariant must not be split across independently protected steps. Choosing between a sleeping [[Mutual Exclusion Lock]], a [[SpinLock]], atomic operations, or [[Read-Copy-Update]] begins with identifying every possible context.

# References

[[linuxkernelprogramming_secondedition.pdf]]
