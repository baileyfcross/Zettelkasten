2026-09-08 09:04

Status: #baby

Tags: [[Portable 3D Model Data]]

# Mesh Normal Orientation

A mesh normal indicates which way a surface faces and influences lighting, shading, and visibility. Face index order helps determine orientation, so reversing that order can flip the normal and make a one-sided exported surface disappear when viewed from the expected side.

Flat shading retains distinct face normals for hard boundaries, while smooth shading blends the normals of adjacent faces to suggest a continuous surface. Normals can even make coarse geometry appear curved, but they do not change the underlying silhouette. Blender tools can flip or recalculate inconsistent normals before export.

# References

[[blenderpythonapi.pdf]]
