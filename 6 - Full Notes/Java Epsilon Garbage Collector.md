2026-10-30 15:57

Status: #baby

Tags: [[Java Garbage Collection and Memory Management]]

# Java Epsilon Garbage Collector

Epsilon is a no-op HotSpot garbage collector: it allocates memory but does not reclaim unreachable objects. When the available heap is exhausted, the JVM terminates with an allocation failure.

This behavior makes Epsilon useful for measuring allocation, testing VM interfaces, isolating collector overhead, or running a deliberately short-lived job whose maximum memory is known. It is not a general production memory strategy; the application must fit its complete allocation footprint within the configured heap.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
