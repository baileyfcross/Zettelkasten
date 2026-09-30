2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Memory Allocation]]

# Kernel Memory Reclaim

Kernel memory reclaim frees reusable pages when available memory falls below desired levels. It can discard clean file cache, write back dirty pages, and move anonymous data to swap so allocations can proceed without immediately invoking the [[Out-of-Memory Killer]].

Reclaim can occur directly in an allocating task or in the background through [[kswapd]]. Its decisions are guided by [[Zone Watermarks]], page recency information such as the [[Multigenerational LRU]], allocation constraints, and whether the current context is allowed to block.

# References

[[linuxkernelprogramming_secondedition.pdf]]
