2026-10-30 15:57

Status: #baby

Tags: [[Java Concurrency and Reactive Streams]]

# Java Thread Lifecycle and Coordination

A Java thread moves through states such as new, runnable, blocked, waiting, timed waiting, and terminated as it starts, competes for monitors, waits, sleeps, joins, and completes. Its scheduler order is not a correctness guarantee.

`join` lets one thread wait for another to finish, `sleep` pauses the current thread for at least a requested time, and interruption is a cooperative signal rather than forced termination. Coordination should make ownership and completion explicit instead of depending on timing or thread priority.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
