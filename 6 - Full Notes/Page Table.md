2026-09-30 01:38

Status: #baby

Tags: [[Linux Virtual Memory Internals]]

# Page Table

A page table is the hierarchical translation structure that maps virtual pages to physical page frames and records access attributes. Entries can encode presence, read/write permission, executability, user accessibility, accessed state, and dirty state as supported by the architecture.

Multi-level tables avoid allocating a flat entry array for unused portions of a sparse address space. Linux supplies architecture-independent traversal concepts while architecture code defines the exact levels, entry formats, and page sizes used by [[Address Translation]].

# References

[[linuxkernelprogramming_secondedition.pdf]]
