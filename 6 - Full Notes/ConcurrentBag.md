2026-09-27 00:11

Status: #baby

Tags: [[.NET Concurrent Collections and Lazy Initialization]]

# ConcurrentBag

`ConcurrentBag<T>` is an unordered concurrent collection optimized for cases in which the same thread often adds and later removes items. Per-thread storage can make local reuse inexpensive while still allowing other threads to take available items.

The type does not promise FIFO or LIFO ordering. It is therefore suitable for pools and interchangeable work items, not for algorithms whose correctness or fairness depends on a global retrieval sequence.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
