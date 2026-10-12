2026-10-01 00:39

Status: #baby

Tags: [[Parametric Curve and Surface Design]]

# Hermite Cubic Spline

A cubic Hermite spline segment is determined by four boundary conditions: the positions at its two endpoints and the tangent vectors at those endpoints. Solving those conditions determines the coefficients of a cubic vector polynomial in the segment parameter.

Multiple segments form a longer spline. Joining endpoint positions provides positional continuity, while coordinating adjacent tangent vectors provides a smooth first derivative across the join. The endpoint-and-tangent form gives direct control over how the curve enters and leaves each segment, making it useful when slope information is part of the design.

# References

[[mathematicsforcomputergraphicsandgameprogramming.pdf]]
