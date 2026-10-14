2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Memory Allocation]]

# SLUB Allocator

The SLUB allocator is the common modern implementation of the Linux slab-allocation interface. It organizes objects into slabs backed by pages and favors relatively simple per-CPU freelists for fast allocation and freeing with less metadata than older slab designs.

Partially occupied slabs can be shared at the node level, while debugging options detect overwrites, use-after-free patterns, and incorrect object handling. Callers usually interact with [[kmalloc]] or a [[Custom Slab Cache]] rather than depending on SLUB internals.

# References

[[linuxkernelprogramming_secondedition.pdf]]
