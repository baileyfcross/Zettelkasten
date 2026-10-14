2026-10-01 00:39

Status: #baby

Tags: [[2D Game Rendering]]

# Digital Differential Analyzer Line Rasterization

The digital differential analyzer rasterizes a line by incrementally advancing from one endpoint to the other. It chooses the larger of the absolute horizontal and vertical differences as the step count, then adds fixed increments of dx divided by that count and dy divided by that count to the current coordinates.

Each accumulated floating-point position is rounded to select a pixel. Reusing the preceding result avoids repeatedly evaluating the line equation, so the method replaces much multiplication with addition. Its fractional arithmetic and rounding distinguish it from [[Bresenham Line Rasterization]], which maintains an integer decision parameter.

# References

[[mathematicsforcomputergraphicsandgameprogramming.pdf]]
