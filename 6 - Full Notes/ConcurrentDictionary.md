2026-09-27 00:11

Status: #baby

Tags: [[.NET Concurrent Collections and Lazy Initialization]]

# ConcurrentDictionary

`ConcurrentDictionary<TKey,TValue>` supports thread-safe key lookup, insertion, update, and removal. Compound methods such as `GetOrAdd` and `AddOrUpdate` express common read-modify-write intentions more safely than separate dictionary calls.

Delegates supplied to these methods may be invoked more than once under contention even though only one resulting value is stored. Factories should therefore avoid irreversible side effects and should not assume that invocation means publication.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
