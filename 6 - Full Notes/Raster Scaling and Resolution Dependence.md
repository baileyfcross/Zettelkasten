2026-09-28 04:01

Status: #baby

Tags: [[SVG Authoring and Optimization]]

# Raster Scaling and Resolution Dependence

A raster asset has a fixed sample grid. Displaying it larger asks a limited set of samples to cover more screen pixels, while preparing a sharper large version increases both encoded and decoded data.

SVG describes geometry independently of a particular output grid, so simple graphics can scale without one source file per resolution. This advantage weakens when the scene requires enormous path complexity or photographic texture. See [[Raster and Vector Image Tradeoffs]] and [[SVG Complexity Reduction]].

# References

[[highperformanceimages.pdf]]
