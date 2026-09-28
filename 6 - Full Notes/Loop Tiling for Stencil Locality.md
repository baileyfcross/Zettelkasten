2026-09-28 03:43

Status: #baby

Tags: [[Stencil Processor Optimization]]

# Loop Tiling for Stencil Locality

Loop tiling partitions a stencil's iteration space into blocks that can reuse data in a faster memory before eviction. A well-sized tile retains neighboring planes or rows long enough for several updates to share them.

Tile dimensions interact with cache capacity, associativity, line size, and [[Array Padding for Cache Conflicts]]. In the book's evaluation, tiling and cache configuration produced the largest early improvement, while later techniques refined bandwidth and computation within that locality-friendly baseline.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

