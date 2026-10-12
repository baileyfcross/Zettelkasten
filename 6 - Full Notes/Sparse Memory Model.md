2026-09-30 01:38

Status: #baby

Tags: [[Linux Virtual Memory Internals]]

# Sparse Memory Model

The sparse memory model organizes Linux physical-memory metadata in sections so systems do not need a densely allocated descriptor array for every possible [[Page Frame Number]]. This accommodates large physical address spaces containing substantial holes and supports memory hotplug configurations.

Only present sections need backing metadata, while section granularity provides a manageable unit for mapping PFNs to page descriptors. The model is especially useful on large NUMA machines whose physical address layout is neither small nor contiguous.

# References

[[linuxkernelprogramming_secondedition.pdf]]
