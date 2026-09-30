2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Memory Allocation]]

# Custom Slab Cache

A custom slab cache stores objects of one kernel-defined type with chosen alignment, flags, and optional construction behavior. Reusing type-specific objects can reduce initialization cost and makes allocator statistics and debugging more informative than a generic size cache.

The cache must outlive every object allocated from it and must be emptied before destruction. A custom cache is justified for frequent, stable object types; ordinary or infrequent allocations are often simpler through [[kmalloc]] and the general [[Linux Slab Allocator]].

# References

[[linuxkernelprogramming_secondedition.pdf]]
