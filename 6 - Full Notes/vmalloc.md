2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Memory Allocation]]

# vmalloc

vmalloc reserves a virtually contiguous range in the [[Kernel Virtual Address Space]] and maps potentially noncontiguous physical pages into it. This makes large allocations more feasible when the CPU needs contiguous addresses but a device or algorithm does not require physically adjacent memory.

Creating and accessing the mapping has more translation and management overhead than direct-mapped [[kmalloc]] memory. The result must be released with its matching vfree interface and generally should not be supplied directly where physical contiguity or simple DMA addressing is required.

# References

[[linuxkernelprogramming_secondedition.pdf]]
