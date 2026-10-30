2026-10-30 15:57

Status: #baby

Tags: [[Java Garbage Collection and Memory Management]]

# Java OutOfMemoryError

`OutOfMemoryError` is a `VirtualMachineError`, not an ordinary exception, and indicates that the JVM cannot satisfy a required allocation or related memory demand. Causes can include an exhausted Java heap, metaspace pressure, oversized arrays, direct-buffer limits, native-thread creation, or collector overhead.

Increasing the heap can postpone failure without correcting retained objects or unbounded work. Diagnosis begins with the error detail, heap or class histograms, dumps, GC logs, and allocation recordings, followed by a distinction between insufficient capacity and a reference path that unintentionally keeps data alive.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
