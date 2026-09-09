2026-09-08 09:04

Status: #baby

Tags: [[Blender Add-On Development Workflow]]

# Hardcoded Add-On Data

Hardcoded add-on data stores vertices, faces, and related values directly in Python collections, then passes them into a new Blender mesh. This can tightly integrate a geometric template with the transformations and subsets an algorithm applies to it.

The same coupling is the method's weakness. Large numeric arrays clutter source code, are difficult for artists to replace, and can usually be read from an external interchange file instead. Hardcoding is most defensible when the data is small or inseparable from the algorithm, not merely because it avoids shipping another file.

# References

[[blenderpythonapi.pdf]]
