2026-09-27 00:11

Status: #baby

Tags: [[.NET Concurrent Collections and Lazy Initialization]]

# ConcurrentStack

`ConcurrentStack<T>` provides thread-safe last-in-first-out push and pop operations. It suits concurrent work whose most recently added item should be retrieved first and includes batch operations that can reduce repeated coordination.

As with other concurrent collections, a prior `IsEmpty` check cannot reserve the next item. Code should use the result of `TryPop` as the authoritative outcome and avoid inferring a stable snapshot from a racing collection.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
