2026-10-30 16:54

Status: #baby

Tags: [[Java Structured Concurrency and Scoped Context]]

# Java Structured Cancellation Propagation

Structured cancellation propagation interrupts sibling subtasks when their enclosing scope no longer needs them because of failure, success under an invoke-any policy, or timeout. Cancellation follows the task hierarchy instead of leaving independent background work behind.

Java interruption is cooperative. A CPU loop must check the current thread's interrupted status between reasonable units of work, while blocking code should use interruptible operations such as sleep. Ignoring interruption can prevent a [[Java Structured Task Scope]] from closing promptly.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
