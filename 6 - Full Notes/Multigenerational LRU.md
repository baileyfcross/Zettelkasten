2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Memory Allocation]]

# Multigenerational LRU

The multigenerational LRU is a Linux page-reclaim policy that groups pages into generations based on observed recency. Aging promotes evidence about recently accessed pages, while eviction favors older generations that are less likely to be needed again soon.

This approach estimates working sets more efficiently than repeatedly scanning a simple active/inactive organization on many workloads. It informs [[Kernel Memory Reclaim]] but still operates within constraints such as memory type, NUMA node, control group, and reclaim eligibility.

# References

[[linuxkernelprogramming_secondedition.pdf]]
