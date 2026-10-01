2026-10-01 00:39

Status: #baby

Tags: [[2D Game Rendering]]

# Midpoint Ellipse Rasterization

Midpoint ellipse rasterization generates one quadrant of an ellipse and uses symmetry about the coordinate axes to produce the other three. The first quadrant is divided into two regions because the magnitude of the tangent slope changes from less than one to greater than one.

The algorithm starts at an axis endpoint and uses an implicit ellipse decision function to choose between adjacent candidate pixels. At the point where the tangent slope reaches unit magnitude, it switches recurrences so that the dominant stepping direction changes. This two-region treatment preserves a continuous outline while relying on incremental arithmetic.

# References

[[mathematicsforcomputergraphicsandgameprogramming.pdf]]
