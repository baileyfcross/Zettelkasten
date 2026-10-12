2026-09-27 00:11

Status: #baby

Tags: [[.NET Task Parallelism and Asynchrony]]

# SynchronizationContext and ConfigureAwait

A synchronization context can capture where an awaited method should resume, such as a user-interface thread that owns controls. This preserves thread-affine behavior but adds scheduling work and can participate in deadlock when a caller blocks that same context waiting for completion.

`ConfigureAwait(false)` tells an await not to require the captured context for its continuation. It is useful in reusable library code that does not need thread-affine state, while application code must retain the context when subsequent work actually depends on it.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
