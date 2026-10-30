2026-10-30 15:57

Status: #baby

Tags: [[Java Concurrency and Reactive Streams]]

# Java Executor Service and Future

`ExecutorService` separates task submission from thread creation and reuse. Factory methods can create fixed or adaptive platform-thread pools or an executor that starts a virtual thread per task. `Runnable` tasks produce no value, while `Callable<V>` tasks can return a value or throw.

Submitting a task returns a `Future<V>` that represents pending completion and supports waiting, result retrieval, cancellation, and status checks. The executor is itself a managed resource: it must be shut down or closed so worker threads do not outlive their intended scope.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
