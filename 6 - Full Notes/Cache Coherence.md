2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Lock-Free Synchronization]]

# Cache Coherence

Cache coherence is the hardware property that keeps processors' cached views of a memory location consistent according to a coherence protocol. When one core obtains permission to modify a cache line, copies held elsewhere are invalidated or updated through protocol transactions.

Coherence does not imply that all independent memory operations become visible in program order; that is the separate concern of [[Memory Reordering and Barriers]]. Frequent writes to one shared line also cause ownership traffic, and [[False Sharing]] can produce that cost even when threads modify different variables.

# References

[[linuxkernelprogramming_secondedition.pdf]]
