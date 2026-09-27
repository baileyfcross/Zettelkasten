2026-09-27 00:11

Status: #baby

Tags: [[.NET Concurrent Collections and Lazy Initialization]]

# LazyInitializer

`LazyInitializer` supplies static helper methods that initialize a field on first use without requiring the field itself to have type `Lazy<T>`. It is useful when a type must expose the eventual value directly or when changing its field shape is impractical.

Overloads vary in their synchronization state and factory requirements. The containing type must retain the initialization flag or lock objects consistently so all callers participate in the same one-time publication protocol.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
