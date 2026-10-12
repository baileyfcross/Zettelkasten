2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Locking]]

# Lock Ordering

Lock ordering assigns a consistent acquisition order when code may need more than one lock. If all paths acquire locks according to the same partial or total order and release them in reverse, they eliminate the circular-wait condition behind a common class of deadlocks.

The order must include uncommon error and interrupt paths, not only the normal case. Documentation and assertions make the protocol reviewable, while [[Lockdep]] can detect observed dependency cycles and help enforce [[Deadlock Avoidance]] during testing.

# References

[[linuxkernelprogramming_secondedition.pdf]]
