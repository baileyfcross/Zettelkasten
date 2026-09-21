2026-09-20 23:34

Status: #baby

Tags: [[Game Physics and Collision]]

# Line Segment Geometry

A line segment is the finite set of points between a start and an end. A parametric representation adds a fraction from zero to one of the end-minus-start vector to the start point.

Collision tests use that bounded parameter to reject intersections located behind the start or beyond the end. Segments support weapon traces, visibility checks, projectiles, and a [[Segment Cast]] against the physics world.

# References

[[gameprogrammingincplusplus.pdf]]
