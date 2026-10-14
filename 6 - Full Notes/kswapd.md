2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Memory Allocation]]

# kswapd

kswapd is the per-node kernel thread that performs background [[Kernel Memory Reclaim]]. It wakes when a memory zone falls below its low watermark and works to restore free pages toward the high watermark before allocation pressure becomes critical.

Background reclaim spreads the cost outside latency-sensitive allocation paths, although allocating tasks may still perform direct reclaim when reserves are insufficient. On NUMA systems, per-node operation lets reclaim respond to local pressure rather than treating all physical memory as one pool.

# References

[[linuxkernelprogramming_secondedition.pdf]]
