2026-09-08 21:16

Status: #baby

Tags: [[.NET Task Parallelism and Asynchrony]]

# Task Continuation

A task continuation schedules work that depends on an earlier task's completion. It can inspect the antecedent's result, cancellation, or exception and can be configured to run only under selected completion conditions.

Continuations expose the dependency graph directly, but long chains can become difficult to read and reason about. For naturally asynchronous workflows, C# `async` and `await` usually express the same sequencing with clearer control flow and exception handling.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
