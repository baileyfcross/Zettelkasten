2026-10-01 00:39

Status: #baby

Tags: [[Game Linear Algebra]]

# Transformation Inversion by Reverse Order

The inverse of a composite transformation applies the inverse elementary operations in reverse order. Algebraically, the inverse of a product AB is B inverse A inverse. Geometrically, the last change made must be the first one undone.

For example, if an axis is translated to the origin, aligned by two rotations, and then used for an operation, restoration reverses the second alignment, the first alignment, and finally the translation. Reusing the forward order would generally fail because transformation matrices do not commute. This principle organizes both recovery of original coordinates and frame-alignment constructions.

# References

[[mathematicsforcomputergraphicsandgameprogramming.pdf]]
