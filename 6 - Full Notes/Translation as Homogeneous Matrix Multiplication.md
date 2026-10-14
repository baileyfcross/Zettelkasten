2026-10-01 00:39

Status: #baby

Tags: [[Game Linear Algebra]]

# Translation as Homogeneous Matrix Multiplication

In ordinary Cartesian coordinates, translation adds a displacement vector while scale and rotation multiply by matrices. Homogeneous coordinates remove that mismatch by placing the displacement components in an augmented transformation matrix.

Multiplying an embedded point with last coordinate one adds the displacement to its spatial coordinates and preserves the final one. The same matrix leaves a direction with last coordinate zero untranslated. Translation can therefore participate in a single composite product with every other affine transform, simplifying repeated object and camera transformations.

# References

[[mathematicsforcomputergraphicsandgameprogramming.pdf]]
