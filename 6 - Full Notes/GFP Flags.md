2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Memory Allocation]]

# GFP Flags

GFP flags tell Linux what an allocation may do and which memory zones it may use. A process-context request may permit reclaim and sleeping, while an atomic-context request must avoid blocking and may draw from limited emergency reserves.

Choosing flags is a statement about execution context, not merely a preference for speed. Flags also express constraints such as DMA reachability, zeroing, accounting, or suppression of warnings, and an incorrect choice can introduce deadlocks or needless allocation failures.

# References

[[linuxkernelprogramming_secondedition.pdf]]
