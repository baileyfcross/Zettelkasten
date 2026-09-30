2026-09-30 01:38

Status: #baby

Tags: [[Linux Virtual Memory Internals]]

# Virtual Memory Split

The virtual memory split divides an architecture's virtual address range between user mappings and kernel mappings. The exact boundary depends on architecture and configuration; on 32-bit systems the choice is especially visible because user and kernel space compete for a limited address range.

User code cannot access the privileged portion even when kernel mappings are present in the active translation structures. The split shapes maximum process address space, direct physical-memory mapping, and how the [[Kernel Virtual Address Space]] is organized.

# References

[[linuxkernelprogramming_secondedition.pdf]]
