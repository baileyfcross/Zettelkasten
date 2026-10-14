2026-09-30 01:38

Status: #baby

Tags: [[Linux Virtual Memory Internals]]

# Linux Virtual Address Space

A Linux virtual address space is the range of addresses interpreted through a task's page tables rather than as direct physical locations. It gives a process a private view containing executable code, data, heap, mappings, shared libraries, and stacks while allowing selected physical pages to be shared.

The hardware memory-management unit performs [[Address Translation]], and the kernel controls mappings and permissions. Part of the architectural range is reserved for the [[Kernel Virtual Address Space]], creating the user/kernel division described by the [[Virtual Memory Split]].

# References

[[linuxkernelprogramming_secondedition.pdf]]
