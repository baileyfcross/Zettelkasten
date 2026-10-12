2026-10-01 00:39

Status: #baby

Tags: [[Game Linear Algebra]]

# 2D Point Representation in Homogeneous Coordinates

A two-dimensional Cartesian point (x, y) is embedded in homogeneous coordinates as (x, y, 1) under the book's row-vector convention. More generally, (hx, hy, h) represents the same finite Cartesian point whenever h is nonzero, after division by h.

The extra coordinate raises planar affine transforms to 3 by 3 matrices. Scaling and rotation occupy the upper coordinate block, while translation is stored in the added row or column according to vector convention. This makes all elementary transforms compatible with [[Matrix Composition for Graphics]].

# References

[[mathematicsforcomputergraphicsandgameprogramming.pdf]]
