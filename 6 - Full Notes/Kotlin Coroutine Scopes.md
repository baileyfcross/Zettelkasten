2026-10-31 13:27

Status: #baby

Tags: [[Kotlin Coroutines Reactive and Testing]]

# Kotlin Coroutine Scopes

A coroutine scope provides the context in which child coroutines are launched and completed. Both `runBlocking` and `coroutineScope` wait for their children before returning, but they wait in different ways.

`runBlocking` occupies and blocks the current thread, whereas `coroutineScope` suspends its caller so the thread can perform other work. Extracted coroutine work can be placed in a `suspend` function, which may call other suspending functions while remaining governed by the surrounding scope.

# References

[[masteringkotlinforjavadevelopers.epub]]
