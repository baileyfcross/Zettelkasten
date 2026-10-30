2026-10-30 16:54

Status: #baby

Tags: [[Java Concurrency and Reactive Streams]]

# Java Virtual Thread Carrier

A carrier thread is the platform thread on which the JVM temporarily mounts a Java virtual thread so that the virtual thread can execute. Many virtual threads can take turns on a smaller pool of carriers, letting an application retain a thread-per-task programming style without requiring one operating-system thread for every waiting task.

When a virtual thread reaches a supported blocking operation, the JVM can unmount it and let the carrier run other work. The carrier is therefore an execution resource rather than the virtual thread's permanent identity; thread-local reasoning, cancellation, and task ownership should stay attached to the virtual task instead.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]

