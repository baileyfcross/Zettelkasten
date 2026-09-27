2026-09-27 00:11

Status: #baby

Tags: [[.NET Task Parallelism and Asynchrony]]

# Task Cancellation Tokens

A `CancellationTokenSource` issues a cooperative cancellation request, and its token lets operations poll the request or register a callback. Passing the same token through a task graph gives callers a consistent way to state that unfinished work is no longer needed.

Cancellation does not forcibly stop arbitrary code. The operation must reach a safe observation point, release resources, and report cancellation distinctly from failure. This cooperation preserves invariants that abrupt thread termination could leave broken.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
