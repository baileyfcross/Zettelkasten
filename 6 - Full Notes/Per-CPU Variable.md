2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Lock-Free Synchronization]]

# Per-CPU Variable

A per-CPU variable gives every processor its own instance of a value, allowing frequent local updates without forcing all CPUs to contend for one cache line. Counters, queues, and temporary state often scale better when partitioned this way and aggregated only when needed.

Correct access must prevent migration or otherwise address a specified CPU, because an ordinary read-modify-write sequence cannot safely continue on a different processor's instance. Remote access and aggregation still need synchronization against concurrent local updates.

# References

[[linuxkernelprogramming_secondedition.pdf]]
