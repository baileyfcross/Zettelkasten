2026-10-01 00:39

Status: #baby

Tags: [[Parametric Curve and Surface Design]]

# B-Spline Curve

A B-spline curve is a weighted sum of control points using piecewise-polynomial basis functions defined over a knot vector. Each basis function has limited support, so changing one control point affects only a local portion of the curve.

Degree, knot spacing, and knot multiplicity control smoothness and interpolation behavior. Uniform splines use regularly spaced knots, open-uniform splines repeat endpoint knots, and nonuniform splines allow arbitrary nondecreasing spacing. At a distinct knot, derivatives remain continuous up to an order determined by the degree; repeated knots reduce that continuity.

# References

[[mathematicsforcomputergraphicsandgameprogramming.pdf]]
