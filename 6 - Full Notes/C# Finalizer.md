2026-10-04 12:25

Status: #baby

Tags: [[.NET Files Streams and Serialization]]

# C# Finalizer

A C# finalizer is a type-defined cleanup method that the runtime may execute after an object becomes unreachable. The garbage collector places finalizable objects on a finalization path, so reclamation is nondeterministic and can require the object to survive longer than an otherwise equivalent object.

A finalizer is therefore a safety net for directly owned unmanaged resources, not the primary release mechanism. [[Deterministic Resource Disposal]] gives callers an explicit `Dispose` path, and a correctly disposed object can call `GC.SuppressFinalize` to avoid unnecessary finalization work. The finalizer must remain safe even when normal cleanup was not requested.

# References

[[programmingincexam70-483mcsdguide.pdf]]
