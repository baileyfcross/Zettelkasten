2026-10-01 00:39

Status: #baby

Tags: [[Game Linear Algebra]]

# Coordinate Frame Conjugation

A transformation defined in a convenient coordinate frame can be applied in another frame by temporarily aligning the frames. The object and reference geometry are first transformed into the convenient frame, the elementary operation is applied there, and the alignment transform is inverted.

This produces the pattern A, then T, then A inverse under the appropriate vector convention. It explains rotation about a fixed point, scaling about a nonorigin center, reflection about an arbitrary line or plane, and [[Rotation About an Arbitrary 3D Line]]. The alignment is not part of the desired motion; it changes the coordinate description so the simple transform has the intended geometric meaning.

# References

[[mathematicsforcomputergraphicsandgameprogramming.pdf]]
