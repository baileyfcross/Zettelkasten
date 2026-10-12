2026-09-30 01:38

Status: #baby

Tags: [[Linux Virtual Memory Internals]]

# Virtual Memory Area

A virtual memory area is a contiguous interval in a process address space whose pages share permissions, backing, and mapping behavior. VMAs describe regions such as an executable segment, anonymous heap allocation, shared library, or memory-mapped file.

The process memory descriptor organizes VMAs so faults and mapping operations can find the region governing an address. A VMA is metadata about a range, whereas a [[Page Table]] records the current page-level translations and may leave individual pages nonresident until first use.

# References

[[linuxkernelprogramming_secondedition.pdf]]
