2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Memory Allocation]]

# Linux Memory Overcommit

Linux memory overcommit allows virtual allocation commitments to exceed immediately available RAM and swap on the assumption that not every process will use every promised page simultaneously. Configurable policies range from heuristic acceptance to stricter accounting against a commit limit.

Overcommit improves flexibility for sparse and copy-on-write workloads but separates allocation success from the later ability to fault in a page. If aggregate demand materializes and reclaim cannot provide enough memory, the [[Out-of-Memory Killer]] may be required to recover the system.

# References

[[linuxkernelprogramming_secondedition.pdf]]
