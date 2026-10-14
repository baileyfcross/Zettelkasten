2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Memory Allocation]]

# DAMON

DAMON is the Linux Data Access MONitor, a framework for observing memory access patterns with controlled overhead. It adaptively groups address ranges and samples them so tools and kernel policies can learn which regions are hot, cold, or changing without tracing every access.

The observations can support analysis and data-access-aware operations such as targeted reclaim. DAMON's sampling parameters trade precision for overhead, so its results are estimates designed for scalable policy decisions rather than a byte-perfect execution trace.

# References

[[linuxkernelprogramming_secondedition.pdf]]
