2026-09-27 00:11

Status: #baby

Tags: [[.NET Parallel Diagnostics and Testing]]

# Async Exception Testing

An exception from asynchronous code is generally stored in the returned task and becomes observable when that task is awaited. A test must therefore await an asynchronous assertion or catch around the await point rather than only around method invocation.

The assertion should distinguish the expected exception type and relevant state from unrelated faults. For multi-task operations, the test may also need to verify how several failures are aggregated or which cancellation outcome is promised.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
