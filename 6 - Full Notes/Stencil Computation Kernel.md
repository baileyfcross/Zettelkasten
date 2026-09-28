2026-09-28 03:43

Status: #baby

Tags: [[Stencil Processor Optimization]]

# Stencil Computation Kernel

A stencil computation updates each point of a regular grid from a fixed neighborhood around that point. Its arithmetic pattern is regular, but repeated reads of neighboring grid values make memory bandwidth and locality central performance constraints.

The book studies seven-point and nineteen-point three-dimensional stencils as customization targets. Their repeated spatial access makes them useful for combining [[Loop Tiling for Stencil Locality]], [[SIMD Stencil Extension]], and [[DMA Computation Overlap]].

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

