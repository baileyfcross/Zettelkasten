2026-10-30 15:57

Status: #baby

Tags: [[Java Concurrency and Reactive Streams]]

# Java Thread and Runnable

A Java `Thread` represents an independently scheduled path of execution, while `Runnable` describes work whose `run` method returns no result. A Runnable can be supplied to a Thread directly or as a lambda because it is a functional interface.

Calling `start` asks the JVM to schedule a new execution that invokes `run`; calling `run` directly is only an ordinary method call on the current thread. Separating the task from the thread lets executors and virtual-thread builders choose how the same work is scheduled.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
