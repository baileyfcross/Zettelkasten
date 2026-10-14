2026-10-01 00:39

Status: #baby

Tags: [[2D Game Rendering]]

# Raster Scan Display System

A raster scan display divides the screen into a rectangular matrix of picture elements, or pixels. The frame buffer stores the value associated with each pixel, and the display controller repeatedly reads that memory while scanning the screen line by line. A visible line or curve is therefore an approximation made by selecting a sequence of discrete pixels.

Raster systems are point-based rather than line-based. Color depth depends on how many bits are stored for each pixel: additional bit planes allow more intensity or color combinations. This discrete representation makes rasterization algorithms such as [[Digital Differential Analyzer Line Rasterization]] and [[Bresenham Line Rasterization]] central to drawing geometric entities.

# References

[[mathematicsforcomputergraphicsandgameprogramming.pdf]]
