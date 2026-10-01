2026-10-01 00:39

Status: #baby

Tags: [[Game Linear Algebra]]

# 3D Point Representation in Homogeneous Coordinates

A three-dimensional Cartesian point (x, y, z) is represented homogeneously as (x, y, z, 1). The added coordinate allows translations, scales, rotations, shears, and reflections to share a uniform 4 by 4 matrix representation.

The value one distinguishes an ordinary position from a direction vector, which can use a zero homogeneous coordinate because translation should not move a direction. After a general projective transform, a nonunit final coordinate is converted back to Cartesian form by dividing the first three coordinates by it.

# References

[[mathematicsforcomputergraphicsandgameprogramming.pdf]]
