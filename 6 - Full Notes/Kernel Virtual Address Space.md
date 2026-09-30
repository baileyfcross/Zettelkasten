2026-09-30 01:38

Status: #baby

Tags: [[Linux Virtual Memory Internals]]

# Kernel Virtual Address Space

The kernel virtual address space contains privileged mappings used for kernel text and data, direct access to portions of physical RAM, dynamically allocated virtual ranges, modules, and architecture-specific facilities. Its organization is distinct from each process's user mappings.

Some regions provide a predictable [[Kernel Logical Address]] for directly mapped RAM, while [[vmalloc]] constructs virtually contiguous mappings from pages that need not be physically adjacent. [[Kernel Address Space Layout Randomization]] varies important locations to make exploitation harder.

# References

[[linuxkernelprogramming_secondedition.pdf]]
