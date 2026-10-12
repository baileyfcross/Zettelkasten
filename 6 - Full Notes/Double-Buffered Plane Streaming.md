2026-09-28 03:43

Status: #baby

Tags: [[Stencil Processor Optimization]]

# Double-Buffered Plane Streaming

Double-buffered plane streaming alternates two local buffers between transfer and computation. While the processor consumes one buffer, DMA fills or drains the other; the roles swap for the next block.

This overlap prevents a single buffer from forcing computation to stop during every transfer. It succeeds only when buffer capacity, transfer granularity, and processing time are balanced so the next plane is ready before the current work finishes.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

