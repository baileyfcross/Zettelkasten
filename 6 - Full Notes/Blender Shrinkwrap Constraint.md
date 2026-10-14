2026-10-02 18:09

Status: #baby

Tags: [[Blender Constraint Systems]]

# Blender Shrinkwrap Constraint

The Blender Shrinkwrap constraint moves an owner's origin to a computed position on or near a target mesh. It can choose the nearest surface point, project along an axis, use the nearest vertex, or project along interpolated target normals, with a distance offset controlling separation from the surface.

Snap modes determine whether the result remains on, inside, outside, or above the target surface, and an owner axis can be aligned to the target normal. Because the constraint moves the object origin rather than deforming its mesh, it differs from the Shrinkwrap modifier. It is suited to attachments and controls that must follow changing surface geometry.

# References

[[modelingandanimationusingblender.pdf]]
