2026-09-30 01:38

Status: #baby

Tags: [[Linux Virtual Memory Internals]]

# Direct-Mapped Kernel Memory

Direct-mapped kernel memory is the region where a range of physical RAM is permanently represented at a predictable kernel virtual offset. A [[Kernel Logical Address]] in this region can be translated to its physical counterpart without walking an arbitrary mapping structure in software.

The direct map makes access to ordinary page allocations efficient, but its extent depends on architecture and address-space constraints. Virtually contiguous allocations made by [[vmalloc]] occupy a different region and may assemble unrelated physical frames.

# References

[[linuxkernelprogramming_secondedition.pdf]]
