2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Memory Allocation]]

# Linux Buddy Allocator

The Linux buddy allocator manages free physical pages in blocks whose sizes are powers of two. When satisfying an order-based request, it can split a larger block into buddies; when a block is released, it can coalesce it with its free buddy to recreate a larger contiguous extent.

Separate free lists by zone, migration type, and order help the allocator balance locality, fragmentation, and reclaim constraints. The [[Kernel Page Allocator]] exposes this machinery, while small object allocation is usually served through the [[Linux Slab Allocator]].

# References

[[linuxkernelprogramming_secondedition.pdf]]
