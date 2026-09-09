2026-09-08 21:16

Status: #baby

Tags: [[.NET Task Parallelism and Asynchrony]]

# Deadlock Avoidance

A deadlock arises when participants wait permanently for resources held by one another. A classic case occurs when two threads acquire the same pair of locks in opposite orders and each waits for the lock held by the other.

Consistent lock ordering, smaller critical sections, time-bounded acquisition, and fewer shared resources reduce the risk. Asynchronous code should also avoid synchronously blocking on incomplete tasks, which can create a waiting cycle with a captured execution context.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
