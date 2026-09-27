2026-09-27 00:11

Status: #baby

Tags: [[.NET Parallel Diagnostics and Testing]]

# Async Unit Testing

An asynchronous unit test should return a task and await the operation under test. This allows the test runner to associate completion and failure with the test instead of reporting success while unobserved work continues.

Tests should control external timing with deterministic fakes or completion sources rather than arbitrary sleeps. They also need to cover cancellation and concurrency invariants without depending on one favorable scheduler interleaving.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
