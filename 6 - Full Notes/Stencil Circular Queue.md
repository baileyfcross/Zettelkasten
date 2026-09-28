2026-09-28 03:43

Status: #baby

Tags: [[Stencil Processor Optimization]]

# Stencil Circular Queue

A stencil circular queue keeps a moving set of grid planes in local memory. Incoming planes are streamed into the queue, neighborhood calculations consume the resident planes, and completed planes are streamed to the destination.

Only the planes required by the current neighborhood need to remain on chip. Combining the queue with [[DMA Computation Overlap]] and [[Double-Buffered Plane Streaming]] turns limited local memory into a reusable window over a much larger grid.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

