2026-09-27 00:11

Status: #baby

Tags: [[.NET Concurrent Collections and Lazy Initialization]]

# Concurrent Collections in .NET

The `System.Collections.Concurrent` namespace supplies collection types whose individual operations are safe under access from multiple threads. Their algorithms use fine-grained synchronization or atomic transitions so callers do not need one broad external lock for ordinary enqueue, dequeue, push, pop, or key-update operations.

Thread safety does not make a sequence of separate calls atomic. A compound invariant still needs an operation such as `GetOrAdd`, explicit coordination, or a design that avoids shared mutation.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
