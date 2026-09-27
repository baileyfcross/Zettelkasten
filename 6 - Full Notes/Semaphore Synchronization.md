2026-09-27 00:11

Status: #baby

Tags: [[.NET Synchronization and Thread Coordination]]

# Semaphore Synchronization

A semaphore maintains a count of available permits and allows at most that many participants through a protected region. Acquiring consumes a permit; releasing returns it, making the mechanism suitable for limiting concurrent access to a finite-capacity resource.

A named semaphore can coordinate across processes, while `SemaphoreSlim` is a lighter in-process alternative. Every successful acquisition must have a corresponding release, normally protected by structured cleanup, or lost permits can permanently reduce capacity.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
