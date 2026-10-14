2026-10-02 18:09

Status: #baby

Tags: [[Blender Constraint Systems]]

# Blender Transform Cache Constraint

The Blender Transform Cache constraint streams object animation stored at the transformation-matrix level from an external cache such as an Alembic archive. The constraint identifies the cache file and object path, then applies the stored transform to its owner with an adjustable influence.

Sequence, frame override, and manual scale controls adapt the cache to the current scene and timeline. Mesh-related options determine which cached vertices, faces, UVs, or color data are read when available. Because the behavior depends on an external contract, file paths, object names, frame interpretation, and unit scale must remain consistent across the producing and consuming scenes.

# References

[[modelingandanimationusingblender.pdf]]
