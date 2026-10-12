2026-09-27 00:11

Status: #baby

Tags: [[.NET Synchronization and Thread Coordination]]

# SpinWait

`SpinWait` provides a progressive spinning strategy for very short waits. Repeated calls initially use processor-level spinning and can later yield so that a waiting loop does not monopolize the current execution time indefinitely.

It is a low-level building block, not a substitute for a condition variable or asynchronous wait. The expected wait must be short, and the loop must read state with the memory-order guarantees required to observe another thread's update.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
