2026-09-27 00:11

Status: #baby

Tags: [[.NET Concurrent Collections and Lazy Initialization]]

# System Lazy Type

`Lazy<T>` wraps a value factory and exposes the constructed result through `Value`. It centralizes deferred creation and can coordinate first access so callers receive one safely published instance.

Thread-safety modes determine whether execution is locked, whether several factories may race with one result published, or whether the caller supplies all synchronization. Choosing a mode requires understanding whether duplicate construction and cached exceptions are acceptable.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]


