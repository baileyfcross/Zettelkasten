2026-10-31 13:27

Status: #baby

Tags: [[Kotlin Coroutines Reactive and Testing]]

# Kotlin Coroutine Jobs and Joining

A coroutine launched with `launch` returns a `Job` that represents the lifecycle of that work. The job can be retained when a caller needs to observe completion, request cancellation, or coordinate another operation with it.

Calling `join` suspends until the job finishes. This makes the dependency explicit without turning the coroutine into a value-producing computation: the caller waits for completion itself, while a result-bearing asynchronous computation uses a different contract.

# References

[[masteringkotlinforjavadevelopers.epub]]
