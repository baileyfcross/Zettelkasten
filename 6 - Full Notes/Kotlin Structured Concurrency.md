2026-10-31 13:27

Status: #baby

Tags: [[Kotlin Coroutines Reactive and Testing]]

# Kotlin Structured Concurrency

Structured concurrency requires new coroutines to belong to a scope whose lifetime contains their work. The enclosing scope waits for its children, so launched operations do not become untracked tasks that silently outlive the operation that started them.

The same hierarchy gives cancellation and failure a visible path. A parent can cancel child work, and the scope can complete only after its children reach a terminal state. This ties asynchronous execution to a program structure that can own its cleanup and errors.

# References

[[masteringkotlinforjavadevelopers.epub]]
