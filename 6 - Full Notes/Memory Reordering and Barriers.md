2026-09-27 00:11

Status: #baby

Tags: [[.NET Synchronization and Thread Coordination]] [[Linux Kernel Lock-Free Synchronization]]

# Memory Reordering and Barriers

Compilers and processors may reorder independent loads and stores when the change preserves single-threaded behavior. Another thread can nevertheless observe those operations in an order the source code did not suggest, making an apparently simple publication protocol unsafe.

A memory barrier constrains movement of reads, writes, or both across a boundary. .NET synchronization operations commonly provide the ordering needed for their contracts; manually placing barriers requires a precise proof of which observations must happen before others.

The Linux kernel exposes read, write, and full memory barriers plus acquire-release and device-facing variants. The correct primitive depends on whether ordering is required between CPUs, compiler accesses, or memory-mapped I/O; [[Marked Memory Access|READ_ONCE and WRITE_ONCE]] stabilize individual accesses but do not automatically provide a full barrier.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
[[linuxkernelprogramming_secondedition.pdf]]
