2026-10-30 15:57

Status: #baby

Tags: [[Java Garbage Collection and Memory Management]]

# Java ZGC and Shenandoah Collectors

ZGC and Shenandoah are HotSpot collectors designed to keep pauses low by moving substantial tracing and compaction work into phases concurrent with application threads. ZGC targets scalable low latency over very large heaps, while Shenandoah emphasizes pause times that do not grow directly with heap size.

Concurrent collection trades shorter pauses for background CPU, memory, and coordination cost. A workload with tight latency objectives may benefit, but the decision requires measuring application throughput and resource headroom rather than selecting a collector solely from its pause description.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
