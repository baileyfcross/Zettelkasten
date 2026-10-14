2026-09-28 04:01

Status: #baby

Tags: [[Image Request Consolidation]]

# Raster CSS Sprite

A raster CSS sprite packs several interface graphics into one bitmap. Elements display a selected rectangle by sizing a box and shifting the shared background image.

The technique reduces requests and can compress repeated colors efficiently. Its costs include coordinate maintenance, coupled cache invalidation, unused transferred regions, and the decoded-memory amplification of loading the whole sheet for one icon. See [[CSS Sprite Coordinate Mapping]] and [[Sprite Memory Amplification]].

# References

[[highperformanceimages.pdf]]
