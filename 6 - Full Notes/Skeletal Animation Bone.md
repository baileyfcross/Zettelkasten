2026-09-20 23:34

Status: #baby

Tags: [[Skeletal Animation Systems]]

# Skeletal Animation Bone

A skeletal animation bone is a rigid coordinate frame within a [[Skeleton Hierarchy]]. It stores a parent relationship and a local transform describing its position and orientation relative to that parent.

The bone does not render as visible geometry. Instead, vertices reference one or more bones through [[Skin Weight|skin weights]], allowing the animated hierarchy to deform the surrounding mesh.

# References

[[gameprogrammingincplusplus.pdf]]
