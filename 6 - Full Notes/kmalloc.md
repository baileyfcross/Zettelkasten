2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Memory Allocation]]

# kmalloc

kmalloc allocates a physically contiguous kernel memory object of at least the requested size from general-purpose slab caches. The returned region is also virtually contiguous in the direct mapping, making it appropriate for many ordinary kernel data structures and some hardware-facing uses.

The call takes [[GFP Flags]], and its contents are uninitialized unless the caller explicitly clears them or uses [[kzalloc]]. Large requests become harder to satisfy as physical memory fragments, so [[vmalloc]] or [[kvmalloc]] may be better when physical contiguity is unnecessary.

# References

[[linuxkernelprogramming_secondedition.pdf]]
