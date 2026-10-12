2026-09-30 01:38

Status: #baby

Tags: [[Linux Virtual Memory Internals]]

# Kernel Logical Address

A kernel logical address is a virtual address in the direct mapping of physical RAM. Within the directly mapped range, Linux can convert between the logical address and its corresponding physical address using a fixed architecture-specific offset.

This convenient relationship does not apply to every kernel virtual address. Memory returned by [[vmalloc]], device mappings, and high-memory mechanisms can be virtually mapped without belonging to the [[Direct-Mapped Kernel Memory]] region.

# References

[[linuxkernelprogramming_secondedition.pdf]]
