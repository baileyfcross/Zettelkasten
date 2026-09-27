2026-09-27 00:11

Status: #baby

Tags: [[.NET Parallel Diagnostics and Testing]]

# Mocking Async Dependencies

An asynchronous mock should return a completed, faulted, canceled, or deliberately controlled task that matches the dependency's real contract. Returning null for a task or hiding synchronous work behind a misleading asynchronous signature makes the test exercise behavior that production code should never see.

Controlled incomplete tasks can verify ordering and cancellation, while completed values keep ordinary tests concise. The mock should preserve important timing-independent semantics rather than imitate incidental implementation delays.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
