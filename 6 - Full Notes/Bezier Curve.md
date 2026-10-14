2026-10-01 00:39

Status: #baby

Tags: [[Parametric Curve and Surface Design]]

# Bezier Curve

A cubic Bezier curve blends four control points with cubic Bernstein polynomials as the parameter varies from zero to one. The curve begins at the first control point and ends at the fourth; its endpoint tangents follow the first-to-second and third-to-fourth control segments.

The de Casteljau algorithm evaluates the curve through repeated linear interpolation and generalizes to any number of control points. The control polygon shapes the whole curve, so moving one control point has global influence rather than strictly local influence. Adjacent Bezier segments require coordinated endpoints and tangent directions for a smooth join.

# References

[[mathematicsforcomputergraphicsandgameprogramming.pdf]]
