2026-09-28 03:43

Status: #baby

Tags: [[Stencil Processor Optimization]]

# DMA Computation Overlap

DMA computation overlap lets a transfer engine move data between external memory and on-chip memory while the processor performs arithmetic on another block. The CPU need not execute every transfer instruction, and communication latency can be hidden behind useful work.

The technique requires explicit buffers, transfer sizes, and synchronization. In stencil processing it supports plane streaming through a [[Stencil Circular Queue]] and can reduce pressure on the data cache.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

