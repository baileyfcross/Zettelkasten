2026-10-02 18:09

Status: #baby

Tags: [[Blender Constraint Systems]]

# Blender Copy Transform Constraints

Blender copy transform constraints make an owner follow a target's location, rotation, scale, or complete transform. Axis switches restrict copying to selected components, inversion reverses chosen values, and offset options combine the copied result with the owner's existing transform instead of replacing it directly.

Coordinate-space selection is essential because the same numeric transform has different meanings in world, local, pose, or other spaces. The full Copy Transforms constraint transfers the combined transform, while specialized copy constraints provide finer control. Influence blends the constrained result with the owner's unconstrained state and can itself be animated.

# References

[[modelingandanimationusingblender.pdf]]
