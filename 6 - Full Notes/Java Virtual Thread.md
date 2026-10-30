2026-10-30 15:57

Status: #baby

Tags: [[Java Concurrency and Reactive Streams]]

# Java Virtual Thread

A Java virtual thread is a lightweight `Thread` scheduled by the JVM over a smaller number of carrier platform threads. Java 21 finalized virtual threads so applications can use a straightforward thread-per-task style for large numbers of operations that spend much of their time waiting.

Virtual threads should generally be created per task rather than pooled as scarce resources. They improve concurrency density, not CPU speed, and blocking while pinned to a carrier can reduce scalability. Existing Thread APIs, interruption, and task-scoping rules still matter.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
