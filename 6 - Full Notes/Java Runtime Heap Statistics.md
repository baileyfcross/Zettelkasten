2026-10-30 15:57

Status: #baby

Tags: [[Java Garbage Collection and Memory Management]]

# Java Runtime Heap Statistics

The singleton `Runtime` object exposes maximum heap capacity, currently committed total memory, and free space within that committed amount. Used heap can be estimated from total minus free, while maximum describes the upper bound the JVM will attempt under the launch configuration.

`Runtime.gc` and `System.gc` only suggest that collection would be useful; they do not guarantee when or whether it occurs. Point-in-time numbers also do not explain allocation behavior, so repeated measurements, GC logs, or Flight Recorder events provide better evidence for a leak or capacity problem.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
