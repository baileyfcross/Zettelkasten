2026-10-01 00:39

Status: #baby

Tags: [[Game Linear Algebra]]

# Matrix Composition for Graphics

Matrix composition replaces a sequence of geometric transformations with one resultant matrix. If row vectors are used and an object is scaled and then rotated, the point is multiplied by the scaling matrix followed by the rotation matrix. The product can be computed once and reused for every point.

Order matters because matrix multiplication is not commutative: translating and then rotating generally differs from rotating and then translating. The composite's inverse must also reverse the factor order. Careful ordering is what lets transformations express fixed-point scaling, arbitrary-axis rotation, viewing, and nested coordinate frames.

# References

[[mathematicsforcomputergraphicsandgameprogramming.pdf]]
