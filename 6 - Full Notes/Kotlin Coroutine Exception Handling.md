2026-10-31 13:27

Status: #baby

Tags: [[Kotlin Coroutines Reactive and Testing]]

# Kotlin Coroutine Exception Handling

Coroutine failures move through the coroutine hierarchy rather than remaining isolated inside an arbitrary thread. A child exception can cancel related work through its parent scope, and several failures may be aggregated while one becomes the primary reported exception.

`CoroutineExceptionHandler` handles an uncaught exception at an appropriate root boundary; it does not replace structured ownership or local recovery. Cancellation is a normal cooperative termination signal, so suspending work and loops must reach points where they can observe and honor it.

# References

[[masteringkotlinforjavadevelopers.epub]]
