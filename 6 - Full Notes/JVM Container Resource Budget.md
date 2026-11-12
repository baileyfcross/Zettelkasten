2026-11-11 19:33

Status: #baby

Tags: [[Java Garbage Collection and Memory Management]] [[Docker Runtime and Container Lifecycle]]

# JVM Container Resource Budget

A JVM container resource budget aligns the container's CPU and memory limits with the JVM's heap, garbage collector, and observed workload. Docker limits such as `--memory` and `--cpus` bound the whole container, while JVM arguments such as `-Xms`, `-Xmx`, and collector selection govern only the Java process's managed runtime behavior.

The heap should not consume the complete container memory allowance because the process and workload need room beyond the requested heap. The source's example gives a workload needing roughly 700 MB a 1 GB container limit and configures a 700 MB heap plus G1. Profiling, [[Java Runtime Heap Statistics]], and continued monitoring should determine the initial values and later adjustments rather than allocating every container the same fixed budget.

# References

[[whendockermeetsjava_apracticalguidetodockerforjavaandspringbootapp.epub]]
