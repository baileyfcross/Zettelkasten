2026-09-20 23:34

Status: #baby

Tags: [[Game Physics and Collision]]

# Point-in-AABB Test

A point-in-AABB test checks whether each point coordinate lies between the corresponding minimum and maximum values of an [[Axis-Aligned Bounding Box]]. The point is contained only when all axis intervals contain it.

The test requires no square roots or rotations and is therefore inexpensive. Inclusive comparisons treat points on the boundary as contained, which is usually desirable for collision queries.

# References

[[gameprogrammingincplusplus.pdf]]
