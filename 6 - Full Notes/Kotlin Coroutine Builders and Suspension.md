2026-10-31 13:27

Status: #baby

Tags: [[Kotlin Coroutines Reactive and Testing]]

# Kotlin Coroutine Builders and Suspension

Kotlin's `launch` builder starts a coroutine concurrently within an available coroutine scope. A suspending operation such as `delay` pauses that coroutine without blocking its thread, allowing other work to use the execution resource during the wait.

`runBlocking` supplies a bridge from ordinary code into a coroutine scope and blocks the calling thread until its work completes. It is useful at boundaries and examples, but its blocking behavior is distinct from the suspension used inside coroutine-oriented code.

# References

[[masteringkotlinforjavadevelopers.epub]]
