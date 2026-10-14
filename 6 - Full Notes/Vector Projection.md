2026-09-18 17:13

Status: #baby

Tags: [[Game Linear Algebra]] · [[Orthogonal Bases and Projections]]

# Vector Projection

Vector projection extracts the part of one vector that lies along another direction. With a normalized basis direction, the [[Dot Product]] gives the signed scalar amount along that direction, and multiplying the basis by that amount produces the projected vector.

Projection is useful for resolving motion or force along an axis, surface, or line. The remaining perpendicular component can be found by subtracting the projection from the original vector.

For a nonzero direction $u$, the projection is $\operatorname{proj}_u(v)=\frac{\langle v,u\rangle}{\langle u,u\rangle}u$. The denominator disappears only when $u$ has unit length.

# References

[[gameprogrammingalgorithmsandtechniques.pdf]]

[[linearalgebra.pdf]]
