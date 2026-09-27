2026-09-27 00:11

Status: #baby

Tags: [[.NET Synchronization and Thread Coordination]]

# SpinLock

`SpinLock` protects a critical section by waiting actively rather than immediately blocking the thread. It can reduce scheduler overhead when contention is rare and the holder releases the lock in only a few instructions.

Because it is a value type, copying it can accidentally create independent locks, and thread-owner tracking adds diagnostic cost. Long work, I/O, or unpredictable scheduling inside the protected region makes spinning wasteful and favors a blocking lock.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
