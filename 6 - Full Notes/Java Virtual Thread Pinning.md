2026-10-30 16:54

Status: #baby

Tags: [[Java Concurrency and Reactive Streams]]

# Java Virtual Thread Pinning

Virtual-thread pinning occurs when a blocking virtual thread cannot be unmounted from its carrier thread, so the carrier remains unavailable for other virtual tasks. The book identifies synchronized blocking as an important source of this restriction through Java 23 and notes that native calls can also hold the carrier.

Java 24's synchronized-without-pinning change allows a virtual thread blocked in a synchronized method or block to detach from its carrier. This improves scalability for existing synchronized code, although blocking native operations and CPU-bound work can still constrain carrier availability.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]

