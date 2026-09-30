2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Memory Allocation]]

# Linux Slab Allocator

The Linux slab allocator builds object caches on top of page allocation so the kernel can obtain small objects without wasting a whole page for each one. Caches group similarly sized or typed objects and can preserve initialized state, alignment, and constructor behavior.

The design reduces fragmentation and repeated setup work while using per-CPU fast paths for common allocations. Modern Linux commonly implements the slab interface with the [[SLUB Allocator]], and general-purpose caches serve [[kmalloc]] requests.

# References

[[linuxkernelprogramming_secondedition.pdf]]
