2026-09-08 21:16

Status: #baby

Tags: [[.NET Files Streams and Serialization]]

# Deterministic Resource Disposal

Managed memory is reclaimed by garbage collection, but scarce operating-system resources such as file handles should be released as soon as their work is complete. Types that own such resources commonly implement `IDisposable` and expose a `Dispose` method.

A C# `using` statement or declaration guarantees disposal when control leaves its scope, including when an exception occurs. This produces predictable resource lifetimes and prevents open streams or handles from lingering until nondeterministic finalization.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
