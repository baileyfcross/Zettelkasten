2026-09-28 04:01

Status: #baby

Tags: [[Digital Image Representation and Quality]]

# Raster and Vector Image Tradeoffs

A raster image stores samples on a fixed pixel grid, making it well suited to photographs and other irregular detail. Enlarging it beyond its sampling resolution exposes blur or pixelation, and increasing its intended display size generally requires more samples.

A vector image stores geometric instructions such as paths, shapes, and fills. It can scale without a proportional increase in source data, but complex photographic detail may require so many primitives that the representation loses its advantage. The appropriate choice depends on content, not merely on file extension. See [[Raster Scaling and Resolution Dependence]].

# References

[[highperformanceimages.pdf]]
