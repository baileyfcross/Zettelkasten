2026-09-27 00:11

Status: #baby

Tags: [[.NET Synchronization and Thread Coordination]] [[Linux Kernel Locking]]

# Semaphore Synchronization

A semaphore maintains a count of available permits and allows at most that many participants through a protected region. Acquiring consumes a permit; releasing returns it, making the mechanism suitable for limiting concurrent access to a finite-capacity resource.

A named semaphore can coordinate across processes, while `SemaphoreSlim` is a lighter in-process alternative. Every successful acquisition must have a corresponding release, normally protected by structured cleanup, or lost permits can permanently reduce capacity.

The Linux kernel also provides sleeping semaphores, but a binary semaphore is usually less expressive than a [[Mutual Exclusion Lock|mutex]] because it does not encode strict owner-unlock semantics. Semaphores remain appropriate when the count represents multiple interchangeable resources rather than ownership of one critical section.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
[[linuxkernelprogramming_secondedition.pdf]]
