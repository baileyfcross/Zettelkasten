2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Memory Allocation]]

# Kernel Page Allocator

The kernel page allocator requests one or more physically contiguous pages from the [[Linux Buddy Allocator]]. An order n allocation contains two to the power n pages, so higher-order requests need increasingly large aligned free blocks and are more vulnerable to fragmentation.

Allocation APIs combine an order with [[GFP Flags]] that describe permitted zones and recovery behavior. Callers must eventually release the same allocation correctly, and they should request only as much physical contiguity as the operation actually requires.

# References

[[linuxkernelprogramming_secondedition.pdf]]
