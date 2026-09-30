2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Lock-Free Synchronization]]

# Marked Memory Access

A marked memory access uses Linux access annotations such as READ_ONCE and WRITE_ONCE to make an intentional shared load or store visible to the compiler as one specific access. The annotations prevent transformations such as inventing, merging, or duplicating accesses that would break a concurrent protocol.

They do not by themselves make a multiword operation atomic or impose full inter-CPU ordering. A correct lock-free design combines marked accesses with dependencies, acquire-release operations, or [[Memory Reordering and Barriers]] according to the protocol's publication requirements.

# References

[[linuxkernelprogramming_secondedition.pdf]]
